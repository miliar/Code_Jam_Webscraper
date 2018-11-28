#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

struct file {
    file(const char *in, const char *out)
        : _in(fopen(in, "r")), _out(fopen(out, "w")) {}

    template <typename ...Args>
    bool read(const char *format, Args &&... args) {
        return fscanf(_in, format, std::forward<Args>(args)...) > 0;
    }

    template <typename ...Args>
    void write(const char *format, Args &&... args) {
        fprintf(_out, format, std::forward<Args>(args)...);
    }

private:
    FILE *_in;
    FILE *_out;
};

static void solve(file &&f);

int main(int argc, char **argv) {
    if (argc < 3) {
        fprintf(stderr, "usage: a.out <in> <out>\n");
        return -1;
    }

    solve(file(argv[1], argv[2]));
    return 0;
}

static void solve(file &&f) {
    int T;
    f.read("%u\n", &T);

    uint64_t N;
    int c = 0;
    while (f.read("%lu", &N)) {
        bool d[10] = {};

        for (int i = 1; i < 100; ++i) {
            string xs = to_string(N * i);
            for (auto &&x : xs) {
                int n = x - 0x30;
                d[n] = true;
                if (all_of(begin(d), end(d), [](bool x) { return x == true; })) {
                    f.write("Case #%d: %s\n", ++c, xs.c_str());
                    goto next;
                }
            }
        }

        f.write("Case #%d: INSOMNIA\n", ++c);
next:
        continue;
    }
}
