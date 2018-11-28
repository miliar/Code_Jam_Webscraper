/* ***********************************************
Author        :kuangbin
Created Time  :2015/6/13 22:18:31
File Name     :A.cpp
************************************************ */

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;


const int MAXN = 1000010;
struct Node *null;
struct Node{
	Node *fa,*ch[2];
	int co;//0 is black, 1 is white
	int lco,rco;
	int ls,rs;
	int s[2];
	int sum[2];//the sum of black and white
	inline void clear(){
		fa = ch[0] = ch[1] = null;
		co = lco = rco = 0;
		ls = rs = 1;
		s[0] = s[1] = 0;
		sum[0] = 1;  sum[1] = 0;
	}
	inline void push_up(){
		if(this == null)return;
		if(ch[0] != null)lco = ch[0]->lco;
		else lco = co;
		if(ch[1] != null)rco = ch[1]->rco;
		else rco = co;
		sum[0] = ch[0]->sum[0] + ch[1]->sum[0] + (co == 0);
		sum[1] = ch[0]->sum[1] + ch[1]->sum[1] + (co == 1);
		int ml = 1 + s[co] + (co==ch[0]->rco?ch[0]->rs:0);
		int mr = 1 + s[co] + (co==ch[1]->lco?ch[1]->ls:0);
		ls = ch[0]->ls;
		if(lco == co && ch[0]->sum[!co] == 0)ls += mr;
		rs = ch[1]->rs;
		if(rco == co && ch[1]->sum[!co] == 0)rs += ml;
	}
	inline void setc(Node *p,int d){
		ch[d] = p;
		p->fa = this;
	}
	inline bool d(){
		return fa->ch[1] == this;
	}
	inline bool isroot(){
		return fa == null || fa->ch[0] != this && fa->ch[1] != this;
	}
	inline void rot(){
		Node *f = fa, *ff = fa->fa;
		int c = d(), cc = fa->d();
		f->setc(ch[!c],c);
		this->setc(f,!c);
		if(ff->ch[cc] == f)ff->setc(this,cc);
		else this->fa = ff;
		f->push_up();
	}
	inline Node* splay(){
		while(!isroot()){
			if(!fa->isroot())
				d()==fa->d() ? fa->rot() : rot();
			rot();
		}
		push_up();
		return this;
	}
	inline Node* access(){
		for(Node *p = this,*q = null; p != null; q = p, p = p->fa){
			p->splay();
			if(p->ch[1] != null)
				p->s[p->ch[1]->lco] += p->ch[1]->ls;
			if(q != null)
				p->s[q->lco] -= q->ls;
			p->setc(q,1);
			p->push_up();
		}
		return splay();
	}
};
Node pool[MAXN],*tail;
Node *node[MAXN];
void init(int n){
	tail = pool;
	null = tail++;
	null->fa = null->ch[0] = null->ch[1] = null;
	null->s[0] = null->s[1] = 0;
	null->ls = null->rs = 0;
	null->sum[0] = null->sum[1] = 0;
	null->co = null->lco = null->rco = 0;
	for(int i = 0;i < n;i++){
		node[i] = tail++;
		node[i]->clear();
	}
}
struct Edge{
	int to,next;
}edge[MAXN*2];
int head[MAXN],tot;
inline void addedge(int u,int v){
	edge[tot].to = v; edge[tot].next = head[u]; head[u] = tot++;
}
void dfs(int u,int pre){
	for(int i = head[u];i != -1;i = edge[i].next){
		int v = edge[i].to;
		if(v == pre)continue;
		node[v]->fa = node[u];
		dfs(v,u);
		node[u]->s[node[v]->lco] += node[v]->ls;
	}
	node[u]->push_up();
}

int S[MAXN];
int M[MAXN];

int id[MAXN];
bool cmp(int i,int j){
	return S[i] < S[j];
}

int main()
{
int __size__ = 256<<20;
	char *__p__ = (char *)malloc(__size__)+__size__;
	__asm__("movl %0,%%esp\n"::"r"(__p__));
	
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
	scanf("%d",&T);
	int iCase = 0;
	while(T--){
		iCase++;
		int n,d;
		scanf("%d%d",&n,&d);
		init(n);
		int as,cs,rs;
		scanf("%d%d%d%d",&S[0],&as,&cs,&rs);
		for(int i = 1;i < n;i++){
			S[i] = ((long long)S[i-1]*as+cs)%rs;
		}
		int am,cm,rm;
		scanf("%d%d%d%d",&M[0],&am,&cm,&rm);
		for(int i = 1;i < n;i++)
			M[i] = ((long long)M[i-1]*am+cm)%rm;
		for(int i = 0;i < n;i++)head[i] = -1;
		tot = 0;
		for(int i = 1;i < n;i++){
			addedge(i,M[i]%i);
			addedge(M[i]%i,i);
		}
		for(int i = 1;i < n;i++){
			node[i]->access();
			node[i]->splay();
			node[i]->co ^= 1;
			node[i]->push_up();
		}
		dfs(0,0);
		for(int i = 0;i < n;i++)id[i] = i;
		sort(id,id+n,cmp);
		int mid;
		for(int i = 0;i < n;i++)
			if(id[i] == 0){
				mid = i;
				break;
			}
		
		int st = mid;
		while(st > 0 &&  S[id[mid]]-S[id[st-1]] <= d)
		{
			int u = id[st-1];
			node[u]->access();
			node[u]->splay();
			node[u]->co ^= 1;
			node[u]->push_up();
			st--;
		}
		//printf("st %d mid %d\n",st,mid);
		node[0]->access();
		node[0]->splay();
		int ans = 0;
		for(int i = mid;i < n;i++){
			if(S[id[i]]-S[id[mid]] > d)break;
			while(S[id[i]]-S[id[st]] > d){
			int u = id[st];
			node[u]->access();
			node[u]->splay();
			node[u]->co ^= 1;
			node[u]->push_up();
				st++;
			}
			node[0]->access();
			node[0]->splay();
			ans = max(ans,node[0]->rs);

			if(i < n-1)
			{
			int u = id[i+1];
			node[u]->access();
			node[u]->splay();
			node[u]->co ^= 1;
			node[u]->push_up();
			}

		}
		printf("Case #%d: %d\n",iCase,ans);
	}
    return 0;
}
