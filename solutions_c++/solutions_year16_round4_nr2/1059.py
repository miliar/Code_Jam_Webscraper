#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <unordered_map>
using namespace std;

int n,k,mask;
double arr[209],dp[20][20][(1<<17)];

double bt(int i,int a,int b)
{
    if(i==n)
        return a+b==k&&a==b;
    if(dp[i][a][mask]!=-1)
        return dp[i][a][mask];
    if((mask&(1<<i))==0)
        return  dp[i][a][mask]=bt(i+1,a,b);
    return dp[i][a][mask]=arr[i]*bt(i+1,a+1,b)+(1-arr[i])*bt(i+1,a,b+1);
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>n>>k;
        for(int f=0;f<n;f++)
            cin>>arr[f];
        for(int f=0;f<20;f++)
            for(int f1=0;f1<20;f1++)
                for(int f2=0;f2<(1<<17);f2++)
                    dp[f][f1][f2]=-1;
        double ans=0;
        for(int f=1;f<(1<<n);f++)
        {
            mask=f;
            ans=max(ans,bt(0,0,0));
        }
        cout<<"Case #"<<tc<<": ";
        cout<<setprecision(9)<<fixed<<ans<<endl;
    }
}