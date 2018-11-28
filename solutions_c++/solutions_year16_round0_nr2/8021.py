#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define eps 1e-9
#define MAX 100000
#define MAXL 20
#define MAXE 100000
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};
char pan[105];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ncase, tcase = 1, n, i;
    scanf("%d", &ncase);
    while(ncase--)
    {
        scanf("%s", pan);
        int len = strlen(pan);
        int ans = 0;
        for(i = len-1; i >= 0; i--)
        {
            if((ans&1) && pan[i] == '+') ans++;
            else if(!(ans&1) && pan[i] == '-') ans++;
        }
        printf("Case #%d: %d\n", tcase++, ans);
    }
    return 0;
}
