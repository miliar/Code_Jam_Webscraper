#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>

#define MAXN 1000005


struct node {
	node *s[2],*fa;
	int size,size_sub;
	bool rev;
	
	inline void add_rev_tag()
	{
		std::swap(s[0],s[1]);rev^=1;
	};
	
	inline void down()
	{
		if (rev) {
			if (s[0]) s[0]->add_rev_tag();
			if (s[1]) s[1]->add_rev_tag();
			rev=0;
		};
	};
	
	inline void update()
	{
		size=1;
		if (s[0]) size+=s[0]->size+s[0]->size_sub;
		if (s[1]) size+=s[1]->size+s[1]->size_sub;
	};
};

node lct[MAXN];

inline int get_parent(node *x,node *&fa)
{
	return (fa=x->fa) ? fa->s[0]==x?0:fa->s[1]==x?1:-1 : -1;
};

inline void rotate(node *x)
{
	int t1,t2;
	node *fa,*gfa;
	t1=get_parent(x,fa);
	t2=get_parent(fa,gfa);
	if ((fa->s[t1]=x->s[t1^1])) fa->s[t1]->fa=fa;
	fa->fa=x;x->fa=gfa;x->s[t1^1]=fa;
	if (t2!=-1) gfa->s[t2]=x;
	fa->update();
};

inline void pushdown(node *x)
{
	static node *tmp[MAXN];
	int cnt=0;
	while (1) {
		tmp[cnt++]=x;
		node *fa=x->fa;
		if (!fa || (fa->s[0]!=x && fa->s[1]!=x)) break;
		x=fa;
	};
	while (cnt--) tmp[cnt]->down();
};

inline node * splay(node *x)
{
	pushdown(x);
	while (1) {
		int t1,t2;
		node *fa,*gfa;
		t1=get_parent(x,fa);
		if (t1==-1) break;
		t2=get_parent(fa,gfa);
		if (t2==-1) {
			rotate(x);break;
		} else if (t1==t2) {
			rotate(fa);rotate(x);
		} else {
			rotate(x);rotate(x);
		};
	};
	x->update();
	return x;
};

inline node * access(node *x)
{
	node *ret=NULL;
	while (x) {
		if (splay(x)->s[1]) {
			x->size_sub+=x->s[1]->size+x->s[1]->size_sub;
			x->s[1]=NULL;
		};
		if (ret) {
			x->size_sub-=ret->size+ret->size_sub;
			x->s[1]=ret;
		};
		(ret=x)->update();
		x=x->fa;
	};
	return ret;
};

inline void setroot(int x)
{
	access(lct+x)->add_rev_tag();
};

inline long long link(int u,int v)
{
	// printf("L %d %d\n",u,v);
	setroot(u),access(lct+u);
	setroot(v),access(lct+v)->fa=lct+u;
	long long ret=1LL*(lct[u].size+lct[u].size_sub)*(lct[v].size+lct[v].size_sub);
	lct[u].size_sub+=lct[v].size+lct[v].size_sub;
	return ret;
};

inline long long cut(int u,int v)
{
	// printf("C %d %d\n",u,v);
	setroot(u);
	node *t=(access(lct+v),splay(lct+v));
	long long ret=1LL*(t->size-1)*(t->size_sub+1);
	t->s[0]->fa=NULL;t->s[0]=NULL;
	t->size=1;
	return ret;
};


int n,D;

int S[MAXN];
int M[MAXN];
int ids[MAXN];

inline bool cmp_S(int i,int j)
{
	return S[i]<S[j];
}

inline int abs(int x)
{
	return x<0?-x:x;
}

inline void solve()
{
	scanf("%d%d",&n,&D);
	int s0,as,cs,rs;
	int m0,am,cm,rm;
	scanf("%d%d%d%d",&s0,&as,&cs,&rs);
	scanf("%d%d%d%d",&m0,&am,&cm,&rm);
	int i;
	S[1]=s0;
	for (i=1;i<n;i++) {
		s0=(1LL*s0*as+cs)%rs;
		m0=(1LL*m0*am+cm)%rm;
		S[i+1]=s0;
		M[i+1]=m0%i+1;
		// printf("i = %d S %d M %d\n",i,s0,m0);
		// printf("M %d = %d\n",i+1,M[i+1]);
	}
	memset(lct,0,sizeof(lct));
	for (i=1;i<=n;i++) {
		lct[i].size=1;
	}
	for (i=1;i<=n;i++) {
		ids[i]=i;
	}
	std::sort(ids+1,ids+n+1,cmp_S);
	for (i=1;i<=n;i++) {
		if (ids[i]==1) break;
	}
	int pos=i;
	for (i=1;i<=n;i++) {
		if (S[1]-S[ids[i]]<=D) break;
	}
	int next=i;
	for (i=next;i<=pos;i++) if (ids[i]!=1) link(ids[i],M[ids[i]]);
	
	setroot(1);access(lct+1);
	splay(lct+1);
	int ans=lct[1].size+lct[1].size_sub;
	
	for (i=pos+1;i<=n;i++) {
		if (S[ids[i]]-S[1]>D) break;
		link(ids[i],M[ids[i]]);
		while (next<=n && S[ids[i]]-S[ids[next]]>D) {
			if (ids[next]!=1) cut(ids[next],M[ids[next]]);
			++next;
		}
		setroot(1);access(lct+1);
		splay(lct+1);
		// printf("Q -> %d\n",lct[1].size+lct[1].size_sub);
		ans=std::max(ans,lct[1].size+lct[1].size_sub);
	}
	printf("%d\n",ans);
}

int main()
{
	int T;
	scanf("%d",&T);
	int i;
	for (i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		solve();
	}
}