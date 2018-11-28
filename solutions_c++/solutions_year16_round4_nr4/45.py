#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
#include <fstream>
using namespace std;

#define lowbit(x) ((x)&(-(x)))
#define sqr(x) ((x)*(x))
#define PB push_back
#define MP make_pair

int n;
char s[100][100];
int f[100],g[100];
int cnt[100];
bool sa[100];

void touch(int i,int v){
	if (f[i]==v) return;
	f[i]=v;
	for (int q=0;q<n;q++)
		if (s[i][q]=='1'&&g[q]==-1){
			g[q]=v;
			for (int z=0;z<n;z++)
			if (s[z][q]=='1')
				touch(z,v);
		}
}

int M;
vector<pair<int,int> > z;

int searchA(int N,int le,int la,int st,int remain);
int searchB(int N,int le,int la,int st,int remain,int curf,int curg,int cur){
	int res=N*N;
	if (curf>la) return res;
	if (curf>=curg&&le>=curf-curg)
		res=min(res,curf*curf+searchA(N-curf,le-(curf-curg),curf,st,remain));
	if (cur>=M) return res;
	for (int i=cur;i<M;i++)
		if (remain&(1<<i)){
			if (sa[i])
				if (remain&(1<<(i-1))) continue;
			int tf=curf+z[i].first;
			if (tf>la) break;
			int tg=curg+z[i].second;
			res=min(res,searchB(N,le,la,st,remain-(1<<i),tf,tg,i+1));
		}

	return res;
}

int searchA(int N,int le,int la,int st,int remain){
	if (N==0) return 0;
	for (;(remain&(1<<st))==0&&st<M;st++);
	int res=N*N;
	for (int i=st;i<M;i++)
		if (remain&(1<<i)){
			res=min(res,searchB(N,le,la,st,remain-(1<<i),z[i].first,z[i].second,i+1));
		}
	// printf("A:%d %d %d %d - %d\n",N,la,st,remain,res); 
	return res;
}

int getans(){
	scanf("%d",&n);
	for (int i=0;i<n;i++) scanf("%s",s[i]);
	memset(f,-1,sizeof(f));
	memset(g,-1,sizeof(g));
	int res=0;
	z.clear();
	int N=n;
	for (int i=0;i<n;i++)
		if (f[i]==-1){
			touch(i,i);
			int cf=0,cg=0;
			for (int a=0;a<n;a++){
				if (f[a]==i) cf++;
				if (g[a]==i) cg++;
			}
			if (cf==cg){
				res+=cf*cg;
				N-=cf;
			}
			else z.PB(MP(cf,cg));
		}
	int le=0;
	memset(sa,false,sizeof(sa));
	sort(z.begin(),z.end());
	// for (int i=0;i<z.size();i++)
	// 	printf("%d-%d\n",z[i].first,z[i].second);
	for (int i=1;i<z.size();i++)
		if (z[i].first==z[i-1].first&&z[i].second==z[i-1].second) {
			sa[i]=true;
		}
	for (int i=0;i<n;i++) if (g[i]==-1) le++;
	M=z.size();
	res+=searchA(N,le,N,0,(1<<M)-1);
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++) 
			if (s[i][j]=='1') res--;
	return res;
}

int main(int argc,char ** argv){
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;t++){
		printf("Case #%d: %d\n",t,getans());
	}
	return 0;
}