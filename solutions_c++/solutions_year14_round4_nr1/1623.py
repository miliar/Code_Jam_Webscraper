#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<set>
#include<fstream>
#include<algorithm>
using namespace std;

int dk[10100],n,x;
bool used[10100];
#define INF 1e7
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int t,casecnt=1;
    scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",casecnt++);
        scanf("%d%d",&n,&x);
        for(int i=0;i<n;i++)
            scanf("%d",&dk[i]);
        sort(dk,dk+n); dk[n] = INF;
        memset( used, false ,sizeof used );
        used[n]=true;
        int cnt = 0;
        for(int i=0;i<n;i++)
        {
            if( !used[i] )
            {
                used[i] = true;
                cnt++;
                int k = upper_bound(dk,dk+n,x-dk[i])- dk -1;
                if( k )
                {
                    while( k >=0 && used[k] ) k--;
                    if( k>=0 ) used[k] = true;
                }
            }
        }
        printf("%d\n",cnt);
    }
    return 0;
}
