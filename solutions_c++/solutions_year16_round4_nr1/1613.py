// by ¦Î
// program sky  :)

#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>

#define Rin register int
#define oo (c=getchar())
#define For(i,l,r) for(int _r=r,i=l;i<=_r;++i)
#define rep(i,l,r) for(int _r=r,i=l;i<_r;++i)
#define dto(i,r,l) for(int _l=l,i=r;i>=_l;--i)

using namespace std;

inline int IN(){
	char c;Rin x=0;
	for(;oo<48 && c^'-' || c>57;);bool f=c=='-';if(f)oo;
	for(;c>47 && c<58;oo)x=(x<<3)+(x<<1)+c-48;if(f)x=-x;return x;
}

int n,R,P,S,N;
char f[333][333];

inline void hello(){
	freopen("ha.in","r",stdin);
	freopen("ha.out","w",stdout);
}

inline bool ck(string s){
	string xx="";
	int n=s.length();
	if(n==1)return 1;
	for(int i=0;i<n;i+=2){
		if(s[i]==s[i+1])return 0;
		xx+=s[i]<s[i+1]?f[s[i]][s[i+1]]:f[s[i+1]][s[i]];
	}
	return ck(xx);
}

pair<bool,string> dfs(int s,int a,int b,int c,string xx){
	if(s==N+1){
		if(ck(xx))return make_pair(1,xx);
		return make_pair(0,"");
	}
	pair<bool,string> ret=make_pair(0,"");
	if(a<P){
		ret=dfs(s+1,a+1,b,c,xx+'P');
		if(ret.first)return ret;
	}
	if(b<R){
		ret=dfs(s+1,a,b+1,c,xx+'R');
		if(ret.first)return ret;
	}
	if(c<S){
		ret=dfs(s+1,a,b,c+1,xx+'S');
		if(ret.first)return ret;
	}
	return ret;
}

int main(){
// say hello
	hello();
	f['P']['R']='P';
	f['R']['S']='R';
	f['P']['S']='S';
	For(tc,1,IN()){
		n=IN();R=IN();P=IN();S=IN();
		N=1<<n;
		pair<bool,string> _=dfs(1,0,0,0,"");
		printf("Case #%d: ",tc);
		cout<<(_.first?_.second:"IMPOSSIBLE")<<endl;
	}
// never say goodbye
}