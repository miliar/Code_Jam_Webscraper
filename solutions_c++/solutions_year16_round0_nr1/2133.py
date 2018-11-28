#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define per(i,a,b) for(int i=(a);i>=(b);i--)
#define forE(i,x) for(int i=head[x];i!=-1;i=ne[i])
using namespace std;
typedef long long i64;
typedef unsigned long long u64;
typedef unsigned u32;
typedef pair<int,int> pin;
#define mk(a,b) make_pair(a,b)
#define lowbit(x) ((x)&(-(x)))
#define sqr(a) ((a)*(a))
#define clr(a) (memset((a),0,sizeof(a)))
#define ls ((x)<<1)
#define rs (((x)<<1)|1)
#define mid (((l)+(r))>>1)
#define pb push_back
#define w1 first
#define w2 second
inline void read(i64 &x){
	x=0;i64 f=1;char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
	x*=f;
}
inline void judge(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
}
/*******************************head*******************************/
i64 x;
bool flag[11];
inline bool check(i64 w){
	while(w){
		flag[w%10]=1;
		w/=10;
	}
	rep(i,0,9)if(!flag[i])return 0;return 1;
}
inline void solve(){
	read(x);
	if(x==0){
		puts("INSOMNIA");return;
	}
	memset(flag,0,sizeof(flag));i64 tmp=x;
	while(233){
		if(check(x)){printf("%lld\n",x);return;}
		x+=tmp;
	}
}
int main(){
	judge();
	int T;cin>>T;
	rep(_,1,T){
		printf("Case #%d: ",_);
		solve();
	}
	return 0;
}
