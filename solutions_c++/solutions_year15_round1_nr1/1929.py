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

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long n,x,cnt1=0;
        long double d=0,cnt2=0;
        cin>>n;
        vector <int> v;
        for(int j=0;j<n;j++)
        {
            cin>>x;
            v.push_back(x);
        }
        for(int j=0;j<n-1;j++)
        {
            if(v[j+1]<v[j]){cnt1+=v[j]-v[j+1];}
            if(v[j+1]<v[j] && (v[j]-v[j+1])/10.0>d){d=(v[j]-v[j+1])/10.0;}
        }
        for(int j=0;j<n-1;j++)
        {
            cnt2+=min(d*10,(long double)v[j]);
        }
        cout<<"Case #"<<i<<": "<<cnt1<<" "<<fixed<<setprecision(0)<<cnt2<<endl;
    }
    return 0;
}
