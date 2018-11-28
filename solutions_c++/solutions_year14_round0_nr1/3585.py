#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<stdlib.h>
#include<vector>
#include<cmath>
#include<queue>
#include<set>
using namespace std;
#define N 100000
#define LL long long
#define INF 0xfffffff
const double eps = 1e-8;
const double pi = acos(-1.0);
const double inf = ~0u>>2;
int a[5][5];
int b[5][5];
bool f[20];
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int t,i,j,n,m;
    cin>>t;
    int kk = 0,k;
    while(t--)
    {
        memset(f,0,sizeof(f));
        cin>>n;
        for(i = 1; i <= 4 ; i++)
            for(j = 1; j <= 4 ; j++)
            {
                cin>>a[i][j];
                if(i==n)
                f[a[i][j]] = 1;
            }
        cin>>m;
        int ans = 0 ;
        for(i = 1; i <= 4 ; i++)
            for(j = 1;j <= 4 ; j++)
            {
                cin>>b[i][j];
                if(i==m)
                {

                    if(f[b[i][j]])
                    {
                        ans++;
                        k = b[i][j];
                    }
                }
            }
        printf("Case #%d: ",++kk);
        if(ans==0)
        puts("Volunteer cheated!");
        else if(ans>1)
        puts("Bad magician!");
        else
        printf("%d\n",k);
    }
    return 0;
}
