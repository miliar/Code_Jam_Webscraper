#include<bits/stdc++.h>
using namespace std;
#define REP(i,a,b)for(int i=(a),i##_end_=(b);i<i##_end_;++i)
#define PER(i,a,b)for(int i=(b)-1,i##_end_=(a);i>=i##_end_;--i)
#define pb push_back
#define fi first
#define se second
template<class T>inline bool umx(T& A,const T& B){return A<B?A=B,1:0;}
template<class T>inline bool umn(T& A,const T& B){return A>B?A=B,1:0;}
typedef long long LL;
typedef double db;
typedef pair<int,int> PII;
typedef pair<db,int> PDI;

const int maxn=1010;

char _s[maxn];
int s[maxn],d[maxn];int n,k;
void solve(){
	scanf("%s%d",_s,&k);n=strlen(_s);
	REP(i,0,n)s[i]=(_s[i]=='+');
	memset(d,0,sizeof d);
	int now=0,t=0;
	REP(i,0,n-k+1){
		now^=d[i];
		if((s[i]^now)==0){
			d[i+k]^=1;
			now^=1;
			++t;
		}
	}
	REP(i,n-k+1,n){
		now^=d[i];
		if((s[i]^now)==0){puts("IMPOSSIBLE");return;}
	}
	printf("%d\n",t);
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int _,__=0;scanf("%d",&_);
	while(_--){
		printf("Case #%d: ",++__);
		solve();
	}
	return 0;
}

