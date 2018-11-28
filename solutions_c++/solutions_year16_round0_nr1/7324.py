#include<bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define FRI freopen("A-small-attempt0.in","r",stdin)
#define FRO freopen("A-small-attempt0.out","w",stdout)
#define debug(args...) {dbg,args; cerr<<endl;}
#define EPS 1e-12
#define RAD(x) ((x*PI)/180)
#define MAXN 100005
using namespace std;

const double PI=acos(-1.0);

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

bool seen[10];

bool isAllSeen() {
    int i;
    for(i=0;i<10;i++)
        if(!seen[i])
            return false;
    return true;
}

void makeSeen(unsigned long long n) {
    while(n) {
        seen[n%10]=true;
        n/=10;
    }
}

int main() {
    unsigned long long n,m,i,T,t=0;
    cin>>T;
    while(t++<T) {
        for(i=0;i<10;i++)
            seen[i]=false;
        cin>>n;
        m=n;
        while(n!=0) {
            makeSeen(m);
            if(isAllSeen())
                break;
            m+=n;
        }
        if(n==0)
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
        else
            cout<<"Case #"<<t<<": "<<m<<endl;
    }
    return 0;
}
