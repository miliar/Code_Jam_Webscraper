#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<stdio.h>
#include<queue>
#include<set>
#include<vector>
#include<map>
#include<string>
#define pq priority_queue
using namespace std;
bool life[15];
int f;
void solve(long long x)
{
    while(x)
    {
        if(!life[x%10])
        {
            f++;
            life[x%10]=1;
        }
        x=x/10;
    }
}
int main()
{
    freopen("date1.txt","r",stdin);
    freopen("date2.txt","w",stdout);
    int t=0, T;
    long long n,ans;
    scanf("%d", &T);
    while(++t<=T)
    {
        f=0;
        ans=0;
        memset(life,0,sizeof(life));
        scanf("%lld", &n);
        if(n)
        {
            while(f<10)
            {
                ans+=n;
                solve(ans);
            }
            printf("Case #%d: %lld\n", t, ans);
        }
        else
        {
            printf("Case #%d: INSOMNIA\n", t);
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
