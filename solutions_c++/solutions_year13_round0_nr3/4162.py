#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
typedef long long ll;
using namespace std;
int f[10000010], cnt;
ll p[10000010];
bool isPalin(ll x)
{
    ostringstream os; os<<x;
    string s=os.str();
    int n=s.size();
    for(int i=0;i<n/2;++i) if(s[i]!=s[n-1-i]) return false;
    return true;
}
int main()
{
    cnt=1;
    for(int i=1;i<10000010;++i) {
        if(isPalin((ll)i*i)) f[cnt]=isPalin(i);
        p[cnt++]=(ll)i*i;
    }
    for(int i=1;i<cnt;++i) f[i]+=f[i-1];
        
    int T; cin>>T;
    for(int t=1;t<=T;++t) {
        ll a,b; cin>>a>>b;
        int x=lower_bound(p,p+cnt,a-1)-p;
        int y=lower_bound(p,p+cnt,b)-p;
        if(p[x]>=a) x--;
        if(p[y]>b) y--;
        cout<<"Case #"<<t<<": "<<f[y]-f[x]<<endl;
    }
    return 0;
}
