#define filer() freopen("f.in","r",stdin)
#define filew() freopen("out.txt","w",stdout)
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<stack>
#include<string>
#include<vector>
#include <map>
#define INF 1<<29
#define PI pair<int,int>

#define SET(a, x) memset((a), (x), sizeof(a))
#define pb push_back
#define i64 long long
#define EPS (1e-9)
using namespace std;
typedef vector<int> VI;
typedef vector<PI> vii;
//i64 INF=(i64)((i64)1<<(i64)59);

int N;

bool pal(i64 x)
{
    i64 a[20],b=0;

    while(x)
    {
        a[b]=x%10;
        x/=10;
        b++;
    }
    i64 lo=0,hi=b-1;

    while(lo<=hi)
    {
        if(a[lo]!=a[hi])return 0;
        lo++;
        hi--;
    }
    return 1;
}
vector<i64>V;

int searchl(i64 x)
{
    if(x>V[V.size()-1])return-1;
    int ans=-1,lo=0,hi=V.size()-1,mid;
    while(lo<=hi)
    {
        mid=(lo+hi)/2;
        if(V[mid]>=x)
        {
            ans=mid;
            hi=mid-1;
        }
        else lo=mid+1;
    }
    return ans;
}

int searchr(i64 x)
{
    int ans=-1,lo=0,hi=V.size()-1,mid;
    i64 y;
    while(lo<=hi)
    {
        mid=(lo+hi)/2;
        y=V[mid];
        if(y<=x)
        {
            ans=mid;
            lo=mid+1;
        }
        else hi=mid-1;
    }

    return ans;
}

int main()
{
    //filer();
    //filew();
    int T,cas=0;
    i64 i,j;
    //cout<<pal(68772654813184)<<endl;
    for(i=1;i<=10000000;i++)
    {
        if(pal(i) && pal(i*i))
        {
            V.pb(i*i);
            //if(i<=20)cout<<i<<endl;
        }

    }
    //cout<<V[V.size()-1]<<endl;;
    //cout<<V.size();
    i64 A,B,x,y,ans;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lld%lld",&A,&B);
        x=searchl(A);
        if(x==-1)ans=0;
        else
        {
            y=searchr(B);
            //if(V[y]>B)y--;
            ans=y-x+1;
        }
        printf("Case #%d: %lld\n",++cas,ans);
    }

    return 0;
}
/*
Test Case:

*/

