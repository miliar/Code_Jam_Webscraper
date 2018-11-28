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
inline void read(int &x){
	x=0;int f=1;char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
	x*=f;
}
inline void judge(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
}
/*******************************head*******************************/
int res=500;
inline int powmod(int a,int b,int mod){
	int res=1;
	for(;b;b>>=1){
		if(b&1)res=1ll*res*a%mod;
		a=1ll*a*a%mod;
	}return res;
}
int v[12][1005],n=32;
char s[55];
inline void check(){
	rep(i,2,10){
		bool flag=0;
		rep(j,2,1000){
			if(v[i][j]==0){
				flag=1;break;
			}
		}
		if(!flag)return;
	}
	printf("%s",s+1);
	rep(i,2,10){
		rep(j,2,1000){
			if(v[i][j]==0){
				printf(" %d",j);break;
			}
		}
	}
	res--;puts("");
}
inline void dfs(int x){
	if(x==0){
		check();if(res==0)exit(0);return;
	}
	s[x]='1';
	rep(i,2,10){
		rep(j,2,1000){
			int w=powmod(i,(n-x),j);
			v[i][j]=(v[i][j]+w)%j;
		}
	}
	dfs(x-1);
	rep(i,2,10){
		rep(j,2,1000){
			int w=powmod(i,(n-x),j);
			v[i][j]=(v[i][j]-w+j)%j;
		}
	}
	if(x==1||x==n)return;
	s[x]='0';
	dfs(x-1);
}
int main(){
	judge();
	puts("Case #1:");
	dfs(n);
	return 0;
}
