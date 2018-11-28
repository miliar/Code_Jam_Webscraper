#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<utility>
using namespace std;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ll long long
#define MAX_SIZE 200005
#define MOD 1000000007
#define S(x) scanf("%d",&x)
#define SL(x) scanf("%lld",&x)
#define SC(x) scanf("%c",&x)
#define SS(x) scanf("%s",x)
#define SZ(x) x.size()
#define IT iterator
#define PI pair<int,int>
#define PL pair<ll,ll>
#define VI vector<int>
#define VL vector<ll>
#define VVI vector< VI >
#define VVL vector< VL >
#define VVP vector< PI >
#define READ() freopen("C:\\Users\\Tarun Sapra\\Desktop\\input.txt","r",stdin)
#define WRITE() freopen("C:\\Users\\Tarun Sapra\\Desktop\\output.txt","w",stdout)
#define dump() SC(dump_char)
int dump_char;

int check(ll n)
{
    char str[20];
    sprintf(str,"%lld",n);
    //printf("string is %s\n",str);
    int l=strlen(str),i;
    for(i=0;i<l/2;i++)
    {
        if(str[i]!=str[(l-1)-i])
            return 0;
    }
    return 1;
}

int main()
{
    READ();
    WRITE();
    VL palin;
    for(ll i=1;i<=10000000;i++)
    {
        if(check(i) && check(i*i))
        {
            palin.pb(i*i);
        }
    }
    int T,t,i,cnt;
    ll a,b;
    S(T);
    //printf("test cases = %d\n",T);
    for(t=1;t<=T;t++)
    {
        //printf("hello");
        scanf("%lld %lld",&a,&b);
        //printf("a = %lld and b = %lld (%d)\n",a,b,t);
        for(cnt=0,i=0;i<SZ(palin);i++)
        {
            if(palin[i]>=a && palin[i]<=b)
                cnt++;
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
