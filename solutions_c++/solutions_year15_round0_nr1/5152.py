#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string.h>
#include<climits>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define sint(i) scanf("%d",&i)
#define ss(s) scanf("%s",s)
#define pii pair<int,int>
#define ll long long
#define MAX 1000000000
#define MOD 1000000007
int main()
{
    freopen("test.in", "r", stdin);
freopen("file.out", "w", stdout);
    int test,ans;
    int n,a,sum,i;
    char s[1010];
    sint(test);
    for(int t=1;t<=test;t++)
    {
        sum=0;
        ans=0;
        sint(n);
        ss(s);
        FOR(i,n+1)
        s[i]=s[i]-'0';
        FOR(i,n+1)
        {
            if(sum<i && s[i]>0)
            {
                ans=ans+i-sum;
                sum=i;
            }
            sum=sum+s[i];
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
