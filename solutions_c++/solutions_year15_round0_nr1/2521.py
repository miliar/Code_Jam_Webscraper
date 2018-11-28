#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <list>
#include <map>
#include <functional>
#include <algorithm>
#include <set>
#include <queue>
#include <memory>
#include <forward_list>
#include <ctime>

using namespace std;

#define ALL(x) begin(x), end(x)

#define FORI(i,a,b)  for (remove_const<decltype(b)>::type i=a, _b=b; i < _b;  ++i)
#define FORLE(i,a,b) for (remove_const<decltype(b)>::type i=a, _b=b; i <= _b; ++i)
#define FORD(i,a,b)  for (remove_const<decltype(a)>::type i=a, _b=b; i > _b;  --i)
#define FORGE(i,a,b) for (remove_const<decltype(a)>::type i=a, _b=b; i >= _b; --i)

#define FREACH(i, x) for (auto &i : x)

#define DPF(...) fprintf(fout, __VA_ARGS__); printf(__VA_ARGS__)

#define READI(var) int var; fin >> var
#define READLL(var) long long var; fin >> var
#define READSTR(var) string var; fin >> var

#define DISCARDLINE {char buf[32]; fin.getline(buf, 32);}

#define SIMPLE_MEMOIZE(funcName) funcName ## FuncReturnTypeVariable_; template <typename ...Args, typename ReturnType = decltype(funcName ## FuncReturnTypeVariable_)> ReturnType funcName(Args... args) { static std::map<std::tuple<Args...>, ReturnType> cache; std::tuple<Args...> t(args...); auto cacheLocItr = cache.find(t); auto &ret = cache[t]; if (cacheLocItr == cache.end()) ret = funcName ## _func(args...); return ret; }  decltype(fibFuncReturnTypeVariable_) funcName ## _func

#define int long long
using int32 = decltype(0);

using vi = vector < int >;
using vll = vector < long long >;
using li = list < int >;

struct PerformanceCounter{ clock_t start, total, startCase, caseClock, worst; int worstI; PerformanceCounter() : start{ clock() }, worstI{ 1 }{ worst = clock() - start; }void StartCase(){ startCase = clock(); }void EndCase(int i){ caseClock = clock() - startCase; if (worst < caseClock){ worst = caseClock; worstI = i; } }void Terminate(){ total = clock() - start; cout << "\ntotal = " << static_cast<float>(total) / CLOCKS_PER_SEC << " seconds\n"; cout << "worst = Case #" << worstI << ": " << static_cast<float>(worst) / CLOCKS_PER_SEC << " seconds\n"; } };

ifstream fin;
FILE* fout;

void parse_cmd_line(int argc, char *argv[]){ if (argc < 3){ fout = fopen("out.txt", "w"); }if (argc < 2){ fin.open("in.txt"); }if (argc > 1){ fin.open(argv[1]); }if (argc > 2){ fout = fopen(argv[2], "w"); } }

//////////////////////////////////////////////////////////////////////////////////////////////////////////


void process()
{
    READI(smax);
    READSTR(shyCntStr);

    auto get_shy = [&](int i){ return shyCntStr[i] - '0'; };

    int totalStanding = 0;
    int ans = 0;
    FORLE(i, 0, smax)
    {
        if (totalStanding < i)
        {
            ans += i - totalStanding;
            totalStanding = i;
        }

        totalStanding += get_shy(i);
    }

    DPF("%d", ans);
}

int32 main(int32 argc, char *argv[])
{
    //if (1) return 0;

    parse_cmd_line(argc, argv);

    //PerformanceCounter pc;

    READI(nCases);
    DISCARDLINE;

    FORLE(i, 1, nCases)
    {
        //pc.StartCase();

        DPF("Case #%d: ", i);
        process();
        DPF("\n");

        //pc.EndCase(i);
    }

    //pc.Terminate();

    return 0;
}