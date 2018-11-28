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
#include <stack>

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
int solve(stack<int>& diners, int numMoves, int& numPansEaten)
{
    if (diners.empty() || diners.top() <= numMoves)
        return 0;

    return 0;
}

struct dpentry
{
    short pancakesEaten;
    short numMoves;
};

dpentry dp[1001][1001];

int solve(vi &startdiners, int maxi, int idx = 0, int depth = 0)
{
    if (depth >= maxi) return depth;

    while (idx < startdiners.size() &&
        startdiners[idx] <= 0) ++idx;

    if (idx >= startdiners.size())
    {
        return depth;
    }

    int a = 1001;

    //auto itr = max_element(ALL(startdiners));
    auto cnt = 0;
    FORI(i, 0, startdiners.size())
    {
        //int i = rand() % startdiners.size();
        int s = startdiners[i];
        ++cnt;
        if (s <= 1) continue;
        FORLE(tmp, 2, s/2)
        {
            startdiners.push_back(s - tmp);
            startdiners[i] = tmp;

            a = min(a, solve(startdiners, maxi, 0, depth + 1));
            startdiners.pop_back();
            startdiners[i] = s;
        }
    }// while (cnt < 3);

    for (auto& s : startdiners) --s;
    int b = solve(startdiners, maxi, 0, depth + 1);
    for (auto& s : startdiners) ++s;

    return min(a,b);
}

void process()
{
    READI(D);

    vi startdiners(D);

    FORI(i, 0, D)
    {
        READI(p);
        startdiners[i] = p;
    }

    sort(ALL(startdiners));

    //DPF("%d", solve(startdiners, *max_element(ALL(startdiners))));
    //return;
    

/*
    if (dp[startdiners.back()][0].numMoves == startdiners.back())
    {
        DPF("%d", startdiners.back());
        return;
    }
*/
    dpentry specialDP[1001];
    int maxi = startdiners.back();
    specialDP[maxi] = { maxi, maxi };
    int best = 1001;
    FORGE(pe, maxi - 1, 0)
    {
        int numMoves = pe, numPansEaten = pe;
        int limit = 0;
        int start = -1;
        FORI(i, 0, startdiners.size())
        {
            int p = startdiners[i];
            /*
                        if (p <= limit)
                        {
                        start = i;
                        continue;
                        }
                        */
            numMoves -= numPansEaten;
            numMoves += dp[p][numPansEaten].numMoves;
            numPansEaten = dp[p][numPansEaten].pancakesEaten;

            if (numPansEaten > pe)
            {
                specialDP[pe] = specialDP[pe + 1];
                numMoves = specialDP[pe].numMoves;
                numPansEaten = specialDP[pe].pancakesEaten;
                break;
            }

            /*
                        if (limit < numPansEaten)
                        {
                        limit = numMoves = numPansEaten;
                        i = start;
                        }
                        */
            /*
            stack<int> diners;
            diners.push(startdiners[i]);*/
            /*int p = startdiners[i];
            _ASSERT(numMoves <= p);
            _ASSERT(numPansEaten <= numMoves);
            if (numMoves == p)
            {
            numPansEaten = p;
            continue;
            }

            int a = p >> 1;
            int b = p - a;*/
            //        numMoves += solve(a, b, numPansEaten);
        }

        specialDP[pe].numMoves = numMoves;
        specialDP[pe].pancakesEaten = numPansEaten;


        //numMoves = numPansEaten;

        //for (auto p : startdiners)
        //{
        //    //if (p <= limit) continue;

        //    numMoves -= numPansEaten;
        //    numMoves += dp[p][numPansEaten].numMoves;
        //    numPansEaten = dp[p][numPansEaten].pancakesEaten;

        //}
    }

    FORGE(i, maxi, 0)
    {
        int nm = specialDP[i].numMoves;
        best = min(best, nm);
    }

    DPF("%d", best);
}

int32 main(int32 argc, char *argv[])
{
    //if (1) return 0;
    srand(time(NULL));
    dp[1][0] = { 1, 1 };
    FORI(pe, 1, 1001)
    {
        dp[1][pe] = { pe, pe };
    }

    FORI(p, 2, 1001)
    {
        FORGE(pe, 1000, 1)
        {
            auto& dpent = dp[p][pe];

            if (pe >= p)
            {
                dpent = { pe, pe };
                continue;
            }

            int a = p - pe;
            int b = p - a;

            if (a > b) swap(a, b);

            const auto& dpa = dp[a][pe];
            const auto& dpb = dp[b][dpa.pancakesEaten];

            if (dpb.pancakesEaten > pe)
            {
                dpent = dp[p][pe + 1];
            }
            else if (dpb.pancakesEaten == pe)
            {
                dpent.pancakesEaten = dpb.pancakesEaten;
                dpent.numMoves = dpa.numMoves - dpa.pancakesEaten + dpb.numMoves + 1;

                if (dpent.numMoves >= p)
                {
                    dpent = { p, p };
                }
            }
            else
            {
                cout << "what?\n" << endl;
            }


            auto& dpprev = dp[p][pe + 1];
            if (dpprev.numMoves == dpent.numMoves && dpprev.pancakesEaten > dpent.pancakesEaten)
                dpent.pancakesEaten = dpprev.pancakesEaten;
        }

        dpentry &best = dp[p][0];
        best = { p, p };
        FORGE(pe, p, 1)
        {
            const dpentry &d = dp[p][pe];
            if ((d.numMoves < best.numMoves) ||
                (d.numMoves == best.numMoves && d.pancakesEaten > best.pancakesEaten))
            {
                best = d;
            }
        }
    }

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