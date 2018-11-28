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
int x,y;
vector<long long int>v;
long long int ulta(long long int n){
    long long int ans = 0;
    while(n) {
        ans = ans*10 + n%10;
        n/=10;
    }
    return ans;
}
bool isPalin(long long int n) {
    if(n == ulta(n))
        return 1;
    return 0;
}
int main()
{
    freopen("/Users/anujkumar/Desktop/cdcdc/test/test/ip.in","r",stdin);
    freopen("/Users/anujkumar/Desktop/cdcdc/test/test/anuj.out","w",stdout);
    int t;
    cin>>t;
    int cseno = 0;
    for(x=0;x<10000000;x++)
        if(isPalin(x) && isPalin(x*x))
            v.pb(x*x);
//    cout<<v.size();
    while(t--){
        cseno++;
        long long int a,b;
        cin>>a>>b;
        int ans = 0;
        for(x=0;x<24;x++)
            if(v[x]>=a && v[x]<=b)
                ans++;
        cout<<"Case #"<<cseno<<": "<<ans<<"\n";
    }
    return 0;
}