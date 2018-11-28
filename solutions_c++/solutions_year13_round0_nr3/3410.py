#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <utility>
#include <sstream>
#include <algorithm>
using namespace std;
#define ll long long
bool solve(ll num)
{
    if(num==0) return true;
    vector<int> a;
    while(num)
    {
        a.push_back(num%10);
        num/=10;
    }
    int l=0,r=a.size()-1;
    while(l<r)
    {
        if(a[l]!=a[r]) return false;
        l++;
        r--;
    }
    return true;
}
int main()
{
    int T;
    freopen("C-small-attempt2.in.txt","r",stdin);
    freopen("C-small-attempt2.out.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        ll a,b;
        printf("Case #%d: ",cas);
        cin>>a>>b;
        ll l=sqrt(a*1.0),r=sqrt(b*1.0);
        ll low=l,right=r;
        //cout<<l<<endl;
        if((l+1)*(l+1)>=a) low=l+1;
        if(l*l>=a) low=l;
        if((l-1)*(l-1)>=a) low=l-1;
        if((r-1)*(r-1)<=b) right=r+1;
        if(r*r<=b) right=r;
        if((r+1)*(r+1)<=b) right=r-1;
        int ans=0;
       // cout<<low<<" "<<right<<endl;
        for(ll num=low;num<=right;num++)
            if(solve(num)&&solve(num*num)){
                ans++;
            }
        printf("%d\n",ans);
    }
    return 0;
}