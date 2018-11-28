#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define fi first
#define prev asfansjfansjabfasjlbfa
#define se second
#define I "%d"
#define II "%d%d"
#define III "%d%d%d"
#define time afsaGAEgagknlenkawgn
#define out_files freopen("D-small-attempt0.in", "r", stdin);freopen("output.txt", "w", stdout)

using namespace std;

typedef vector <int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef vector <pii> vii;
typedef vector <vi> vvi;
typedef long double ld;

#ifdef WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif // WIN32

const int inf = (int)1e9;
const ll INF = 1LL*inf*inf;
const double eps = 1e-9;
const int SZ = 1000;
const int md = (int)1e9+7;

int t;
string s;

int main()
{
    out_files;
    scanf(I, &t);
    for (int q=1; q<=t; q++)
    {
        int k,c,s;
        scanf(III, &k, &c, &s);
        if (s<k-1 || (c==1 && s<k)) {printf("Case #%d: IMPOSSIBLE\n", q); continue;}
        if (c==1 || k==1)
        {
            printf("Case #%d:", q);
            for (int i=1; i<=k; i++)
                printf(" %d", i);
            printf("\n");
        } else
        {
            printf("Case #%d:", q);
            for (int i=2; i<=k; i++)
                printf(" %d", i);
            printf("\n");
        }
    }
    return 0;
}
