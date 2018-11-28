#include <cstdio>
#include <fstream>
#include <iostream>

#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <vector>
#include <bitset>
#include <string>
#include <cstring>
#include <algorithm>

#include <ctime>
#include <cstdlib>
#include <cassert>

#define pb push_back
#define mp make_pair
#define sz(A) (int) (A).size()

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define eputs(A) fputs((A), stderr)

#define sqr(A) ((A) * (A))
#define start first
#define end second
  
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;

const int N = (int) 1e6;
const int M = 1000002013;

int t, n, m, cnt[N];
pii p[N];

bool IsIn (int a, int b)
{
    return p[b].start <= p[a].start && p[a].end <= p[b].end;
}

bool test (int a, int b)
{
    return max(p[a].start, p[b].start) <= min(p[a].end, p[b].end) && !IsIn(a, b) && !IsIn(b, a) && cnt[a] && cnt[b];
}

void Add (int s, int e, int c)
{
    p[m] = pii(s, e);
    cnt[m++] = c;    
}

bool makeChanges ()
{
    bool flag = false; 
    for (int i = 0; i < m; i++)
        for (int j = 0; j < m; j++)
            if (test(i, j)) {
                int c = min(cnt[i], cnt[j]);
                cnt[i] -= c, cnt[j] -= c;
                Add(p[i].start, p[j].end, c);
                Add(p[j].start, p[i].end, c);                
                flag = true;
            }

    return flag;
}

LL calc ()
{
    LL ans = 0;
    for (int i = 0; i < m; i++) {
        int len = p[i].end - p[i].start; 
        LL d = (LL) (2 * n - len + 1) * len / 2 % M;
        d = cnt[i] * d % M;
        
        ans = (ans + d) % M;
    }

    return ans;
}

int main () 
{
    #ifdef DEBUG
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    #endif

    scanf("%d", &t);
    for (int T = 0; T < t; T++) {
        cerr << T << endl;

        LL ans = 0;

        scanf("%d%d", &n, &m);
        for (int i = 0; i < m; i++)
            scanf("%d%d%d", &p[i].start, &p[i].end, cnt + i);
    
        LL get = 0;
        get = calc();

        while (makeChanges());
        
        ans = calc();

        /*
        cerr << get << ' ' << ans << endl;
        for (int i = 0; i < m; i++)
            if (cnt[i])
                cerr << p[i].start << ' ' << p[i].end << endl;
        cerr << endl;
        */

        printf("Case #%d: %I64d\n", T + 1, ((get - ans) % M + M) % M);
    }
    
    return 0; 
}

