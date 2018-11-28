#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <memory>
#include <cassert>
#include <set>
#include <numeric>
#include <functional>
#include <bitset>

using namespace std;

#define ALL(x) begin(x), end(x)

#define FORI(i,a,b)   for (decay_t<decltype(b)> i=a, _b=b; i <  _b; ++i)
#define FORLE(i,a,b)  for (decay_t<decltype(b)> i=a, _b=b; i <= _b; ++i)
#define FORD(i,a,b)   for (decay_t<decltype(a)> i=a, _b=b; i >  _b; --i)
#define FORGE(i,a,b)  for (decay_t<decltype(a)> i=a, _b=b; i >= _b; --i)
#define FREACH(x, A)  for (auto &x : A)

#define DISCARD_LINE do { char buf[32]; fin.getline(buf, 32); } while(0)

template <typename T> T read_var() { T var; fin >> var; return var; }

//#define READI(var)   int var;       fin >> var
//#define READLL(var)  long long var; fin >> var
//#define READSTR(var) string var;    fin >> var

#define READI(var)   auto var = read_var<int>()
#define READLL(var)  auto var = read_var<long long>()
#define READSTR(var) auto var = read_var<string>()

#define DPF(...) do { fprintf(fout, __VA_ARGS__); printf(__VA_ARGS__); } while(0)

/* memoization stuff */
template <class RetType, class... Args> struct Memoize { template <class... KeyArgs> static std::map<std::tuple<KeyArgs...>, RetType> make_memoize_cache(KeyArgs... args); }; template <class RetType, class... Args> Memoize<RetType, Args...> make_memoize(RetType(*func)(Args...));
#define MEMOIZATION_HEADER(isLocalCache, funcName, ...) using funcName##_Memoize_Cache = decltype(decltype(make_memoize(funcName))::make_memoize_cache(__VA_ARGS__)); static funcName##_Memoize_Cache _memoizeCache; static int _memoizeLevel = 0; if ((isLocalCache) && _memoizeLevel == 0) _memoizeCache.clear(); funcName##_Memoize_Cache::key_type _memoizeKey{ __VA_ARGS__ }; auto itr = _memoizeCache.find(_memoizeKey); if (itr != end(_memoizeCache)) return itr->second; ++_memoizeLevel; auto& _memoizeReturnValue = _memoizeCache[_memoizeKey]
#define MEMOIZATION_RETURN(retValue) { _memoizeReturnValue = retValue; --_memoizeLevel; return _memoizeReturnValue; }

using dword = unsigned int;
using qword = unsigned long long;

using int32 = int;
#define int long long

using lb = list<bool>;
using lc = list<char>;
using li = list<int>;
using ld = list<double>;
using ls = list<string>;

using vb = vector<bool>;
using vc = vector<char>;
using vi = vector<int>;
using vd = vector<double>;
using vs = vector<string>;
using vll = vector<long long>;

using vdw = vector<dword>;
using vqw = vector<qword>;

using pii = pair<int, int>;

FILE* fout; ifstream fin;
void parse_cmd_line(int32 argc, char *argv[]){ fin.open((argc < 2 ? "in.txt" : argv[1])); fopen_s(&fout, (argc < 3 ? "out.txt" : argv[2]), "w"); }
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

vi primes;

void preprocess()
{
    vb sieve(33'333'500);

    sieve[0] = sieve[1] = true;
    FORI(i, 2, sieve.size())
    {
        if (sieve[i] == true)
        {
            continue;
        }

        for (int j = i + i; j < sieve.size(); j += i)
        {
            sieve[j] = true;
        }
    }

    primes.reserve(10'000'000);
    FORI(i, 2, sieve.size())
    {
        if (sieve[i] == false)
        {
            primes.push_back(i);
        }
    }
}

int is_prime(int n)
{
    FREACH(p, primes)
    {
        if (p*p > n)
        {
            break;
        }

        if (n % p == 0)
            return p;
    }

    return 0;
}

int convert_from_base2(int n, int newBase)
{
    int ret = 0;
    FORGE(shift, 31, 0)
    {
        ret *= newBase;

        int dig = n >> shift;
        
        ret += dig & 1;
    }

    return ret;
}

void print_binary(int n)
{
    bool start = false;
    FORGE(shift, 31, 0)
    {
        int dig = (n >> shift) & 1;

        if (dig) start = true;

        if (start)
            DPF("%lld", dig);
    }
}

void process()
{
    READI(N);
    READI(J);

    int lo = (1 << (N - 1)) + 1;
    int hi = (1 << N) - 1;

    int cnt = 0;
    int divs[11] = {};

    for (int i = lo; i <= hi && cnt < J; i += 2)
    {
        bool jammin = true;
        FORLE(b, 2, 10)
        {
            int tmp = convert_from_base2(i, b);

            divs[b] = is_prime(tmp);

            if (divs[b] == 0)
            {
                jammin = false;
                break;
            }
        }

        if (jammin)
        {
            ++cnt;

            DPF("\n");

            print_binary(i);

            FORLE(b, 2, 10)
            {
                DPF(" %lld", divs[b]);
            }
        }
    }
}

int32 main(int32 argc, char *argv[])
{
    preprocess();

    parse_cmd_line(argc, argv);

    READI(nCases);
    DISCARD_LINE;

    FORLE(i, 1, nCases)
    {
        DPF("Case #%d:", i);

        process();

        DPF("\n");
    }

    return 0;
}