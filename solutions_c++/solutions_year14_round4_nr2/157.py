#include<cstdio>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;
int z,c,n;
vector<pair<int,int> > b;
int a[1000],t[1000];
int dp[2000][2000];
bool v[2000][2000];
void f(int lo,int hi)
{
    if(v[lo][hi])
        return;
    v[lo][hi]=true;
    if(lo==hi)
        dp[lo][hi]=0;
    else
    {
        int p=-1,b=2000000000;
        for(int i=lo;i<=hi;i++)
            if(a[i]<b)
            {
                p=i;
                b=a[i];
            }
        for(int i=p;i>lo;i--)
            swap(a[i],a[i-1]);
        f(lo+1,hi);
        dp[lo][hi]=min(hi-p,p-lo)+dp[lo+1][hi];
    }
}
int main()
{
    freopen("b-large.out","w",stdout);
    freopen("b-large.in","r",stdin);
    cin>>z;
    for(int zz=1;zz<=z;zz++)
    {
        cin>>n;
        //b.clear();
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            //b.push_back(make_pair(a[i],i));
        }
        //sort(b.begin(),b.end());
        //for(int i=0;i<n;i++)
        //    a[b[i].second]=i;
        memset(v,0,sizeof(v));
        f(0,n-1);
        printf("Case #%d: %d\n",zz,dp[0][n-1]);
    }
    return 0;
}
