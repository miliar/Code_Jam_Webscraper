// Code by SQL Ninja
#include<bits/stdc++.h>
using namespace std;
#define ll unsigned long long
#include <boost/multiprecision/cpp_int.hpp>
namespace mp = boost::multiprecision;
#define pb push_back
#define bi  mp::cpp_int
vector<bi> divs;
void print(ll   tmp){
    ll   a = ((ll  )1) << 63;
    int i=0;
    for( i=0;((a>>i & tmp)==0)&&i<63;i++);
    for(;i<=63;i++)
    {
        cout<<((a>>i & tmp)!=0);
    }
}
bi decode (ll   x,ll   y){
    bi a(x),b(y),ans(0),pw(1);
    while(a){
        ans += pw*(a & 1);
        pw*=b;
        a >>=1;
    }
    return ans ;
}
bool check(ll   x,ll   base)
{
    bi p = decode(x,base);
    for(bi i (2) ;i<=bi(1e5) && bi(i)*bi(i)<p;i++)
        if(p%i==0){
               // cout<<x<<" "<<p<<" "<<i<<endl;
         divs.pb(i);
                return 1;
        }
    return 0;
}
ll   last = 1;
ll   gen(int N){
    ll   ans = ((ll  )1) << (N-1);
    ll   tmp = last + ans;
    do{
        divs.clear();
        bool ok = true;
        for(int i=2;i<=10;i++)
        ok &= check(tmp,i);
        last +=2;
        tmp  = last + ans ;
        if(ok)return tmp-2;
    }while(true);

}
int main()
{
   // freopen("out.txt","w",stdout);
    int T=1,N,J;
    N=16;J=50;
    printf("Case #%d:\n",T);
    while(J--){
            ll   a = gen(N);
            print(a);
            for(int i=0;i<9;i++)
                cout<<" "<<divs[i];
            cout<<endl;

    }
}
