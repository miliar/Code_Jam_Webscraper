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


struct Papers
{
    vi vec;
    int piv = -1;
};

int check(int(&grid)[50][50], const Papers& p, int N)
{
    int ret = 3;
    int piv = p.piv;

    FORI(i, 0, N)
    {
        if (grid[piv][i] != 0 && p.vec[i] != grid[piv][i])
        {
            ret ^= 1;
            break;
        }
    }

    FORI(i, 0, N)
    {
        if (grid[i][piv] != 0 && p.vec[i] != grid[i][piv])
        {
            ret ^= 2;
            break;
        }
    }

    return ret;
}

void solve(vector<Papers>& solds, int (&grid)[50][50], int N)
{
    while (!solds.empty())
    {
        FREACH(x, solds)
        {
            int rowcol = check(grid, x, N);
            if (rowcol == 3)
            {
                continue;
            }

            if (rowcol == 1)
            {
                FORI(i, 0, N)
                {
                    grid[x.piv][i] = x.vec[i];
                }
            }
            else
            {
                FORI(i, 0, N)
                {
                    grid[i][x.piv] = x.vec[i];
                }
            }

            x.piv = -1;
        }

        solds.erase(partition(ALL(solds), [](Papers& a)
        {
            return a.piv != -1;
        }), end(solds));
    }

}

void process()
{
    READI(N);

    vector<Papers> solds(2 * N - 1);
    FREACH(x, solds)
    {
        x.vec.resize(N);
        FREACH(y, x.vec)
        {
            READI(tmp);
            y = tmp;
        }
    }

    int piv = -1;

    FORI(i, 0, N)
    {
        auto sEnd = partition(ALL(solds), [](Papers& a)
        {
            return a.piv == -1;
        });

        sort(begin(solds), sEnd, [&i](Papers&a, Papers&b)
        {
            return a.vec[i] < b.vec[i];
        });

        int sz = 0;

        if (distance(begin(solds), sEnd) >= 2)
        {
            int val = solds.front().vec[i];
            while (solds[sz].vec[i] == val) ++sz;
        }
        else
        {
            sz = 1;
        }

        FORI(j, 0, sz)
        {
            solds[j].piv = i;
        }

        if (sz == 1)
        {
            piv = i;
        }
    }


    int grid[50][50] = {};

    //float n2 = float(N) / 2;

    //FORI(i, 0, )

    partition(ALL(solds), [&piv](Papers& a)
    {
        return a.piv != piv;
    });

    auto other = solds.back();
    FORI(i, 0, N)
    {
        grid[piv][i] = other.vec[i];
    }

    solds.pop_back();

    sort(ALL(solds), [](Papers& a, Papers& b)
    {
        return a.piv < b.piv;
    });

    for (int i = 0; i < solds.size(); i += 2)
    {
        int p = solds[i].piv;
        grid[p][p] = solds[i].vec[p];

        if (equal(ALL(solds[i].vec), begin(solds[i + 1].vec)))
        {
            FORI(j, 0, N)
            {
                grid[p][j] = grid[j][p] = solds[i].vec[j];
            }

            solds[i].piv = solds[i + 1].piv = -1;
        }
    }

    solds.erase(partition(ALL(solds), [](Papers& a)
    {
        return a.piv != -1;
    }), end(solds));

    sort(ALL(solds), [](Papers& a, Papers& b)
    {
        return a.piv < b.piv;
    });

    solve(solds, grid, N);

    int rowcol = check(grid, other, N);

    if (rowcol & 1)
    {
        FORI(i, 0, N)
        {
            DPF(" %lld", grid[i][piv]);
        }
    }
    else
    {
        FORI(i, 0, N)
        {
            DPF(" %lld", grid[piv][i]);
        }
    }
}

int32 main(int32 argc, char *argv[])
{
    parse_cmd_line(argc, argv);

    READI(nCases);
    DISCARD_LINE;

    FORLE(i, 1, nCases)
    {
        DPF("Case #%lld:", i);

        process();

        DPF("\n");
    }

    return 0;
}