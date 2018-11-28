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
#define getnum(x) scanf("%d",&x);
#define dprintf(x...) fprintf(stderr,x);
#define lld I64d;
#define result(x,y)  printf("Case #%d: %I64d\n", x+1, (long long)y);
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

int T;
int cnt[10];
bool count(int N){
    string s = to_string(N);
    for(auto k:s){
        cnt[k-'0']++;
    }
    fora(i,10) if(cnt[i]==0) return false;
    return true;
}
int main() {
	//ios::sync_with_stdio(false);//use with care
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    getnum(T);
    // dprintf("%d %d\n",T,T);
    fora(t,T){
        int N;
        sd(N);
        if(N==0){
            printf("Case #%d: INSOMNIA\n", t+1);
            continue;
        }
        fora(i,10) cnt[i] = 0;
        int i;
        for(i=1;i<100000000;i++){
            if(count(N*i)) break;
        }
        if(i==100000000){
            printf("Case #%d: INSOMNIA\n", t+1);
            continue;
        }
    	result(t,N*i);
    }
    return 0;
}