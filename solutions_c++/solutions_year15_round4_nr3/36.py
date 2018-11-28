#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;
typedef long long int64;

const int oo=1000000000;
struct Edge {
	int v,r;
	Edge *next,*opp;
};

const int maxV=51000,maxE=210000;
Edge po[maxE*2],*ve[maxV];
int pon;
void init() {
	pon=0,memset(ve,0,sizeof(ve));
}
void addEdge(int a,int b,int c) {
	Edge *e1=po+pon++,*e2=po+pon++;
	(e1->opp=e2)->opp=e1;
	e1->v=b,e1->next=ve[a],ve[a]=e1;
	e2->v=a,e2->next=ve[b],ve[b]=e2;
	e1->r=c,e2->r=0;
}

int vn,vs,vt;
int step[maxV];
Edge *ve2[maxV];
bool relabel() {
	fill(step+1,step+vn+1,oo);
	step[vt]=0;
	
	static int l[maxV];
	l[1]=vt;
	for(int lh=1,lt=1;lh<=lt;lh++) {
		int x=l[lh];
		for(Edge *e=ve[x];e;e=e->next)
			if(e->opp->r&&step[e->v]>=oo) {
				step[e->v]=step[x]+1;
				l[++lt]=e->v;
			}
	}
	
	for(int x=1;x<=vn;x++)
		ve2[x]=ve[x];
	return step[vs]<oo;
}
int aug(int x,int limit) {
	if(x==vt)
		return limit;
	int ans=0;
	for(Edge *&e=ve2[x];e;e=e->next)
		if(e->r&&step[x]==step[e->v]+1) {
			int ret=aug(e->v,min(limit,e->r));
			e->r-=ret,e->opp->r+=ret;
			limit-=ret,ans+=ret;
			if(limit==0)
				break;
		}
	return ans;
}

const int maxn=310;
char s[100000],ss[10000];
vector<int> sent[maxn];
map<string, int> str2id;
void testcase() {
	str2id.clear();
	int n;
	scanf("%d ",&n);
	for(int i=1;i<=n;i++) {
		gets(s);
		char *cur=s;
		int delta;
		sent[i].clear();
		while(sscanf(cur,"%s%n",&ss,&delta)>0) {
			//printf("[%s]",ss);
			if(str2id.count(ss)==0) {
				int nid=str2id.size()+1;
				str2id[ss]=nid;
			}
			sent[i].push_back(str2id[ss]);

			cur+=delta;
		}
		//puts("");
	}
	
	/*for(int i=1;i<=n;i++) {
		for(int j=0;j<sent[i].size();j++)
			printf("%d ",sent[i][j]);
		puts("");
	}*/
	int m=str2id.size();

	vn=m*2+n+2;
	vs=vn-1, vt=vn;
	init();
	for(int i=1;i<=n;i++) {
		for(int j=0;j<sent[i].size();j++) {
			addEdge(m+m+i, sent[i][j], oo);
			addEdge(m+sent[i][j], m+m+i, oo);
		}
		if(i==1)
			addEdge(vs,m+m+i,oo);
		if(i==2)
			addEdge(m+m+i,vt,oo);
	}
	for(int i=1;i<=m;i++)
		addEdge(i,m+i,1);
	//printf("vn=%d %d\n",vn,pon);
	
	int flow=0;
	memset(step,0,sizeof(step));
	while(relabel())
		flow+=aug(vs,oo);
	printf("%d\n",flow);
}
int main() {
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		testcase();
	}
	scanf("%*s");
	return 0;
}
