#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define N 1000010
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,te,T,As,Cs,Rs,Am,Cm,Rm,D,an,flag;
int S[N],M[N],fa[N],f[N],ge[N],id[N],cun[N];
VI a[N];
inline bool cc1(const int &A,const int &B) {
	return S[A]<S[B];
}
int get(int x) {
	return f[x]==x?x:f[x]=get(f[x]);
}
inline void jia(int x) {
	if (cun[x]) return;
	if (!x) {
		flag=1;
		return;
	}
	int A=get(fa[x]);
	ge[A]+=ge[x];
	f[x]=fa[x];
}
void dfs(int x) {
	if (cun[x]) return;
	cun[x]=1;
	ge[get(x)]--;
	for (auto i:a[x]) dfs(i);
}
int main() {
	freopen("fair.in","r",stdin);
	freopen("fair.out","w",stdout);
	scanf("%d",&T);
	For(te,1,T) {
		scanf("%d%d",&n,&D);
		scanf("%d%d%d%d",&S[0],&As,&Cs,&Rs);
		scanf("%d%d%d%d",&M[0],&Am,&Cm,&Rm);
		For(i,0,n-2) S[i+1]=(S[i]*As+Cs)%Rs;
		For(i,0,n-2) M[i+1]=(M[i]*Am+Cm)%Rm;
		For(i,1,n-1) fa[i]=M[i]%i;
		For(i,0,n-1) f[i]=i,cun[i]=0,ge[i]=1,id[i]=i;
		For(i,0,n-1) a[i].clear();
		For(i,1,n-1) a[fa[i]].push_back(i);
		sort(id,id+n,cc1);
		i=an=0; flag=0;
		For(j,0,n-1) {
			jia(id[j]);
			for (;S[id[i]]+D<S[id[j]];i++) dfs(id[i]);
			if (flag) an=max(an,ge[0]);
		}
		printf("Case #%d: %d\n",te,an);
		cerr<<te<<endl;
	}
	return 0;
}
