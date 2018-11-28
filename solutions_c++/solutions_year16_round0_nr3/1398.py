#include<bits/stdc++.h>
using namespace std;
bool isPrime(__int128 n){
    srand(time(nullptr));
    for(int i=0;i<100;i++){
        __int128 a,b,c,x,y,m;
        m=rand()%1000;
        while(m--){
            a=rand();
        }
        a=rand()%100000000;
        b=rand()%100000000;
        c=rand()%100000000;
        x=rand()%100000000;
        y=rand()%100000000;
        m=a*x*x+b*y*y+c;
        m%=(n-4);
        m+=2;
        if(__gcd(n,m)>1)return 0;
    }
    return 1;
}
bool ok(__int128 y) {
    if(!(y&1))return 0;
    __int128 n,m;
    for(__int128 i=2; i<=10; i++) {
        n=0,m=1;
        for(__int128 j=0; j<32; j++) {
            n+=m*((y>>j)&1);
            m*=((long long)i);
        }
//        cout<<"-> "<<n<<endl;
        bool f=1;
        if(n<=(1e16)) {
            for(__int128 j=2; j*j<=n; j++) {
                if(n%j==0) {
                    f=0;
                    break;
                }
            }
        }else f=isPrime(n);
        if(f)return 0;
    }
    return 1;
}
string calc(__int128 y,__int128 b) {
    __int128 n=0,m=1;
    for(__int128 i=0; i<32; i++) {
        n+=m*((y>>i)&1);
        m*=b;
    }
    __int128 ii=-1;
    for(__int128 i=2; i*i<=n; i++) {
        if(n%i==0) {
            ii=i;
            break;
        }
    }
    string ret="";
    while(ii) {
        ret+=char(48+(ii%10));
        ii/=10;
    }
    reverse(ret.begin(),ret.end());
    assert(!ret.empty());
    return ret;
}
int main() {
    __int128 m=500;
    __int128 x=0x80000001;
    cout<<"Case #1:\n";
    while(m--) {
        while(x<=(0xffffffff) && !ok(x)) {
//            cout<<x<<"\n";
            x+=2;
        }
        if(x<=(0xffffffff)) {
            string s="";
            __int128 y=x;
            while(y) {
                s+=char(48+(y&1));
                y>>=1;
            }
            reverse(s.begin(),s.end());
            cout<<s;
            for(__int128 i=2; i<11; i++) {
                cout<<" "<<calc(x,i);
            }
            cout<<"\n";
        }
        x+=2;
    }
    return 0;
}
