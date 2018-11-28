#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> ii;
typedef vector<int> vi;

#define PI 3.1415926535897932385

//int dp[101][1000002];
int mote[10001],n;
long long mx;

int func(int i,long long mysize)
{
    if(i==n) return 0;
    int fl=0,added=0,j=i;
    while(mysize<=mote[i])
    {
        if((mysize-1)<=0) break;
        mysize+=(mysize-1);
        added++;
    }
    mysize=min(mysize,mx+1);
    while(i<n&&mysize>mote[i])
    {
        fl=1;
        mysize=min(mysize+mote[i],mx+1);
        i++;
    }
    if(mysize==(mx+1)) return min(added,n-j);
    int ans=n;
    if(fl==1) ans=added+func(i,mysize);
    return min(ans,n-j);
}

int main()
{
    ios::sync_with_stdio(false);
    //freopen("cr1.in","r",stdin);
    //freopen("cr1.out","w",stdout);
    int t,my,tt=0;
    cin>>t;
    //t=1;
    while(t--)
    {
        tt++;
        cin>>my>>n;
        for(int i=0;i<n;i++){
            cin>>mote[i];
         //   cout<<mote[i]<<" "<<i<<"\n";
        }
        sort(mote,mote+n);
        mx=mote[n-1]+2;
        cout<<"Case #"<<tt<<": "<<func(0,my)<<"\n";
    }
    return 0;
}
