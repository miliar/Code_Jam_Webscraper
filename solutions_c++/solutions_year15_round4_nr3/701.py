#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

const int maxn = 1e6;

//map <int, int> eng, french;
int n, best;
vector <string> list[maxn];
vector <int> numbers[maxn];
vector <string> all;
//bool mark[25][20005];
int eng[20005];
int french[20005];

/*inline void upd(int typ, string & s, int delta)
{
    if (typ == 0)
        eng[num[s]] += delta;
    else french[num[s]] += delta;
}*/

void go(int step)
{
//    printf("go %d\n", step);
    if (step == n)
    {
        int cnt = 0;
        forn(i, all.size())
        {
            if (eng[i] > 0 && french[i] > 0)
                cnt++;
        }
        best = min(best, cnt);
        return;
    }
    forn(j, list[step].size())
        eng[numbers[step][j]]++;
    go(step + 1);
    forn(j, list[step].size())
    {
        eng[numbers[step][j]]--;
        french[numbers[step][j]]++;
    }
    go(step + 1);

    forn(j, list[step].size())
        french[numbers[step][j]]--;
}

int main() {
#ifdef LOCAL
    //freopen("inp", "r", stdin);
    //freopen("outp", "w", stdout);
#else
    // freopen(TASKNAME ".in", "r", stdin);
    // freopen(TASKNAME ".out", "w", stdout);
#endif
    int tests;
    scanf("%d", &tests);
    forn(test, tests)
    {
        scanf("%d\n", &n);
        all.clear();
        forn(i, n)
        {
            list[i].clear();
            char c;
            string cur = "";
            while(true)
            {
                c = getchar();
                if (c == '\n' || c == -1)
                {
                    if (cur != "")
                        list[i].pb(cur);
                    break;
                }
                else if (c == ' ')
                {
                    if (cur != "")
                    {
                        list[i].pb(cur);
                        cur = "";
                    }
                }
                else cur += c;
            }
            forn(j, list[i].size())
                all.pb(list[i][j]);
//            forn(j, list[i].size())
  //              cout << list[i][j] << " ";
    //        cout << endl;
        }
        sort(all.begin(), all.end());
        all.resize(unique(all.begin(), all.end()) - all.begin());
//        fprintf(stderr, "sz %d\n", all.size());
        forn(i, n)
        {
            numbers[i].resize(list[i].size());
            forn(j, list[i].size())
                numbers[i][j] = lower_bound(all.begin(), all.end(), list[i][j]) - all.begin();
        }
        //eng.clear();
        //french.clear();
        memset(eng, 0, sizeof(eng));
        memset(french, 0, sizeof(french));
        forn(j, list[0].size())
            eng[numbers[0][j]]++;
        forn(j, list[1].size())
            french[numbers[1][j]]++;
/*        forn(i, n)
            forn(j, all.size())
                mark[i][j] = false;*/
/*        forn(i, n)
            forn(j, list[i].size())
                mark[i][numbers[i][j]] = true;*/
        best = 1e9;
        go(2);
        fprintf(stderr, "Case #%d: %d\n", test + 1, best);

        printf("Case #%d: %d\n", test + 1, best);
    }
}
