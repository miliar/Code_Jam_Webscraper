#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef pair<int, int> pii;
typedef vector<int> vi;

#define pb push_back
#define mp make_pair

template <class T> inline T sqr(T x) { return x * x; }
template <class T> inline void updMin(T& a, const T& b) { if (b < a) a = b; }
template <class T> inline void updMax(T& a, const T& b) { if (b > a) a = b; }

const int INF = -10000;

vector <int> s;
vector < set<int> > w;

void solve()
{
    int n, x;

    scanf("%d%d", &n, &x);
    s.clear();
    s.resize(n);

    w.clear();
    w.resize(701);

    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &s[i]);
    }

    sort(s.begin(), s.end());
    for (int i = 0; i < n; ++i)
    {
        w[s[i]].insert(i);
    }

    int ans = 0;
    for (int i = n - 1; i >= 0; --i)
    {
        if (s[i] == INF)
            continue;
        set<int>::iterator beg = w[s[i]].find(i);
        if (beg == w[s[i]].end())
        {
            int stop = 1;
            ++stop;
        }
        w[s[i]].erase(beg);
        int d = x - s[i];
        s[i] = INF;
        ++ans;
        for (int j = d; j >= 1; --j)
        {
            if (!w[j].empty())
            {
                int t = *w[j].begin();
                w[j].erase(w[j].begin());
                s[t] = INF;
                break;
            }
        }
    }

    printf("%d\n", ans);
}


int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int test = 1; test <= t; ++test)
    {
        printf("Case #%d: ", test);
        solve();
    }



    return 0;
}