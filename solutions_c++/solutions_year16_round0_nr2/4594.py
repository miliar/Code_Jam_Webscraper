#include <cstdio>
#include <string>
#include <algorithm>
#include <limits>

using namespace std;

struct file {
    file(const char *in, const char *out)
        : _in(fopen(in, "r")), _out(fopen(out, "w")) {}

    template <typename... Args>
    bool read(const char *format, Args &&... args) {
        return fscanf(_in, format, std::forward<Args>(args)...) > 0;
    }

    template <typename... Args>
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

static void flip(string &s, size_t pos) {
    for (size_t i = 0; i < pos; ++i) {
        s[i] = s[i] == '+' ? '-' : '+';
    }

    reverse(begin(s), begin(s) + pos);
}

static void solve(file &&f) {
    int T;
    f.read("%u\n", &T);

    char S[101];
    int c = 0;
    while (f.read("%s", S)) {
        string s(S);
        for (int i = 0;; ++i) {
            if (std::all_of(begin(s), end(s),
                            [](char x) { return x == '+'; })) {
                f.write("Case #%d: %d\n", ++c, i);
                goto next;
            }

            size_t p = s.find('+');

            if (p == 0) {
                p = s.find('-');
            }

            string prev = s;
            if (string::npos == p) {
                flip(s, s.size());
            } else if (p == 0) {
                flip(s, s.find('-'));
            } else {
                flip(s, p);
            }
        }
    next:
        continue;
    }
}
