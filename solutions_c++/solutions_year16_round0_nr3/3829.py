#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/algorithm/string/join.hpp>
#include <boost/multiprecision/miller_rabin.hpp>

using namespace std;
namespace al = boost::algorithm;
namespace mp = boost::multiprecision;
using uint128_t = mp::uint128_t;

struct file {
    file(const char *in, const char *out) : _in(fopen(in, "r")), _out(fopen(out, "w")) {}

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

template <typename T>
static T from_binary(const std::string &v) {
    T result = 0;

    for (auto &&x : v) {
        result <<= 1;
        result += x == '1' ? 1 : 0;
    }

    return result;
}

template <typename T>
static T from_string(const string &v, int base) {
    assert(base > 0 && base <= 16);

    const T b = base;
    T result = 0;
    string s(v);
    reverse(begin(s), end(s));

    for (size_t i = 0; i < s.size(); ++i) {
        auto p = mp::pow(b, i);
        result += static_cast<T>(s[i] - 0x30) * p;
    }

    return result;
}

template <typename T>
static string to_string(T v, int base) {
    static const char t[] = "0123456789ABCDEF";
    assert(base > 0 && base <= 16);
    string result;

    do {
        result += t[static_cast<int>(v % base)];
    } while ((v /= base) >= base);

    result += t[static_cast<int>(v)];
    reverse(begin(result), end(result));
    return result;
}

template <typename T>
static bool is_prime(const T &p) {
    if (p == 2) {
        return true;
    }

    static boost::random::mt19937 gen(clock());
    return mp::miller_rabin_test(p, 25, gen); // (1/4)^25?
}

template <typename T>
static T get_nontrivial_divisor(const T &v) {
    for (T i = 2; i < v; ++i) {
        if (v % i == 0) {
            return i;
        }
    }

    return 0;
}

static void solve(file &&f) {
    int T, N, J;
    f.read("%u", &T);
    f.read("%d %d", &N, &J);
    string ss(N, '0');
    ss.front() = '1';
    const uint128_t l = from_binary<uint128_t>(string(N, '1'));
    int ok_count = 0;
    f.write("Case #1:\n");

    for (uint128_t s = from_binary<uint128_t>(ss); ok_count < J && s <= l; ++s) {
        const string r1 = to_string(s, 2);
        if (r1.back() == '0') {
            continue;
        }
        vector<string> r2;
        r2.reserve(9);
        for (int b = 2; b <= 10; ++b) {
            auto v = from_string<uint128_t>(r1, b);
            if (is_prime(v)) {
                break;
            }
            r2.push_back(get_nontrivial_divisor(v).str());
        }

        if (r2.size() != r2.capacity()) {
            continue;
        }

        ++ok_count;
        const string joined = al::join(r2, " ");
        f.write("%s %s\n", r1.c_str(), joined.c_str());
    }
}
