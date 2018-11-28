//joyneel
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	LL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))

#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

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

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);

LL pw(LL a,int n,int v){
    if(v==0) return 0;
    if(!n) return 1;
    LL tp = pw(a,n/2,v);
    if(n&1) return a*tp*tp;
    return tp*tp;
}

int main(){
    int t;
    si(t);
    int n,J;
    si(n);si(J);
    int cnt = 0;
    cout<<"Case #1:"<<endl;
    for(int i=0;i<1<<(n-2);i++){
        int tp = i;
        VI v,fct;
        v.PB(1);
        for(int j=0;j<n-2;j++){
            v.PB((tp&(1<<j))>>j);
        }
        v.PB(1);
        LL num;
        for(LL j=2;j<=10;j++){
            num = 0;
            for(int k=0;k<SZ(v);k++){
                num += pw(j,k,v[k]);
            }
            for(int k=2;k<=sqrt(num);k++){
                if(num%k==0){
                    fct.PB(k);
                    break;
                }
            }
        }
        if(SZ(fct)==9){
            for(int k=SZ(v)-1;k>=0;k--) cout<<v[k];
            cout<<' ';
            for(int k=0;k<SZ(fct);k++) cout<<fct[k]<<' '; cout<<endl;
            cnt++;
            if(cnt==J) break;
        }
    }
    return 0;
}
