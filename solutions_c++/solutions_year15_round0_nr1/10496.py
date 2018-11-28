#include <bits/stdc++.h>
#define MAX 1000000007
#define pb push_back
#define mp make_pair
#define FOR(n) for(i=0;i<n;i++)
#define rep(i,n) for(i=0;i<n;i++)
#define reps(i,a,b) for(i=a;i<=b;i++)
#define swap(a,b) T=a,a=b,b=T
#define ll long long int
#define ff first.first
#define ss first.second
#define pii pair< ll,ll >
#define piii pair< pii,ll >
#define que queue<int>
#define s(t) scanf("%lld",&t)
#define p(t) printf("%lld\n",t)
using namespace std;
int main()
{
ll i,j,k,l,n,m,t,T,f,p,ans,cnt,par,ele,a[100005],sum;
char str[100005];
s(t);
k=0;
while(t--)
{
    k++;
    s(n);
    scanf("%s",str);
    FOR(n+1)
    {
        a[i]=str[i]-'0';
    }
    sum=0;
    cnt=0;
    FOR(n+1)
    {
        sum+=a[i];
        if(sum<=i)
        {
            sum++;
            cnt++;
        }
    }
    printf("Case #%lld: %lld\n",k,cnt);
}

return 0;
}
