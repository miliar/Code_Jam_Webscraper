/*
	jsrkrmciB
 */
using namespace std;
#include <bits/stdc++.h> // precompiled headers
#define fora(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define clr clear()
#define inf (1<<30)
#define eps 1e-9
#define getnum(x) scanf("%d",&x)
#define dprintf(x...) fprintf(stderr,x)
#define lld I64d
#define result(x,y)  printf("Case #%d: %I64d\n", x+1, (long long)y)
#if __cplusplus <= 199711L
  #error This library needs at least a C++11 compliant compiler
#endif
#define sd(x)  scanf("%d",&x)
#define sc(x) scanf("%c",&x)
#define sll(x) scanf("%I64d",&x)
#define sf(x) scanf("%Lf",&x)
#define ss(x) scanf("%s",x)
typedef long double ld;
typedef long long ll;
typedef string str;

int T,N,J;
ll isprime(ll n){
    for(ll i=2; i*i<=n; i++){
        if(n%i==0) return i;
    }
    return 0;
}
ll basen(string s, int b){
    int p = N-1;
    ll t = 0;
    for(auto k:s){
        if(k=='1'){
            ll tmp = 1;
            fora(i,p) tmp*=b;
            t += tmp;
        }
        p--;
    }
    return t;
}
string next(string s){
    int i = 0;
    while(1){
        if(s[i]=='0') {
            s[i]='1';
            break;
        }
        else{
            s[i]='0';
            i++;
        }
    }
    return s;
}
int main() {
	//ios::sync_with_stdio(false);//use with care
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.out","w",stdout);
    sd(T);
    printf("Case #1:\n");
    sd(N);
    sd(J);
    string s (N-2, '0');
    for(int i=0;J>0;i++){
        ll t;
        vector<ll> v;
        if(i!=0) s = next(s);
        for(int i=2;i<=10;i++){
            t = isprime(basen("1"+s+"1",i));
            if(t==0) break;
            v.pb(t);
        }
        if(t==0) continue;
        cout << "1"+s+"1" << " ";
        for(auto n:v){
            cout << n << " ";
        }
        // for(int i=2;i<=10;i++){
        //     cout << basen("1"+s+"1",i) << " ";
        // }
        J--;
        cout << endl;
    }
    return 0;
}