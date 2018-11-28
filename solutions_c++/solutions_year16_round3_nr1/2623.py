/*
        SUPTO
        UNIVERSITY OF DHAKA
*/
#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
#define popcount(n) __builtin_popcount(n)
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair < ll, ll > pll;
#define eps 1e-9
#define MAX 100000
#define pi acos(-1.0)
#define MAXL 20
#define MAXE 100000
#define inf 1000000000
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};
pii pr[30];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ncase, tcase = 1, n, i;
    scanf("%d", &ncase);
    while(ncase--)
    {
        scanf("%d", &n);
        for(i = 0; i < n; i++)
        {
            scanf("%d", &pr[i].ff);
            pr[i].ss = i;
        }
        sort(pr, pr+n);
        printf("Case #%d:", tcase++);
        while(pr[n-1].ff != pr[n-2].ff)
        {
            printf(" %c", pr[n-1].ss+65);
            pr[n-1].ff--;
        }
        for(i = 0; i < n-2; i++)
        {
            if(pr[i].ff&1)
            {
                printf(" %c", pr[i].ss+65);
                pr[i].ff--;
            }
            for(int j = 0; j < pr[i].ff; j += 2) printf(" %c%c", pr[i].ss+65, pr[i].ss+65);
        }
        for(i = 0; i < pr[n-1].ff; i++) printf(" %c%c", pr[n-2].ss+65, pr[n-1].ss+65);
        printf("\n");
    }
    return 0;
}
