#include<bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define pi(x) printf("%d\n",x)
#define F first
#define S second
#define PB push_back
#define MP make_pair

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;

const int mod = 1000000007;
inline void add(int &x, int y){x+=y; if(x>=mod)x-=mod; if(x<0)x+=mod;}
inline int mul(int x, int y){ return ((LL)x * y)%mod;}
int gcd(int a, int b){ if(b)return gcd(b,a%b); return a;}
int power(int a ,int p){int ret = 1; while(p){if(p&1)ret=mul(ret,a); a=mul(a,a); p/=2;}return ret;}
int phi(int n){ int ret=n; int i = 2; 
    if(n%i==0){ ret-=ret/i; while(n%i==0)n/=i;}
    for(i=3; i*i<=n; i++)if(n%i==0){ ret-=ret/i; while(n%i==0)n/=i;}
    if(n>1)ret-=ret/n;return ret;
}

int main()
{
    int test; cin>>test; 
    for(int tc = 1; tc <= test; tc++)
    {
        vector<bool> f(10);
        int x; cin>>x; 
        int iter = 100000; 
        LL y = 0;
        int done = 0;
        while(done < 10 and iter--)
        {
            y+=x;
            LL tm = y; 
            while(tm>0){
                int z = tm % 10; tm/=10;
                if(f[z])continue; f[z] = true; done++; 
            }
        }
        cout<<"Case #"<<tc<<": ";
        if(done<10) cout<<"INSOMNIA\n"; else cout<<y<<endl;
    }
    return 0;	
}
