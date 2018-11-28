#include <iostream>
#include <string>
#include <sstream>
#include <cassert>
using namespace std;

typedef long long LL;

LL atoi(const string &s){
    stringstream ss(s);
    LL res;
    ss>>res;
    return res;
}

LL gcd(LL a, LL b){
    return b==0?a:gcd(b, a%b);
}

int main(int argc, const char * argv[])
{
    int ncase; cin>>ncase;
    for(int ca=1; ca<=ncase; ca++){
        string s;cin>>s;
        auto md=s.find('/');
        LL p=atoi(s.substr(0,md)), q=atoi(s.substr(md+1));
        LL g=gcd(q,p);
        p /= g; q /= g;
        LL res=-1,l=0;
        for(LL i=0; res<0&&i<44; i++)
            if(q==(1<<i))
                res= i;
        for(l=0; (1<<l)<=p; l++);
        cout<<"Case #"<<ca<<": ";
        if(res>=0)
            cout<<res-l+1<<endl;
        else cout<<"impossible"<<endl;
            
    }
    return 0;
}

