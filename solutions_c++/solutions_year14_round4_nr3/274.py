#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>
#include<stdlib.h>

using namespace std;

typedef long long int lnt;
typedef double dou;
#define N 300514
#define M 2000514
using namespace std;
typedef struct{int f,t,c,ne;}edge;
edge e[M];
int es[N],ee[N],et;
int d[N];
int pre[N];
//int blk[N];
int gap[N];
int advance(int*x){
	for(int i=es[*x];i!=-1;i=e[i].ne){
        int t=e[i].t;
        if(e[i].c&&d[*x]==d[t]+1){
            pre[t]=i;
            //blk[t]=std::min(blk[*x],e[i].c);
            *x=t;
            return 1;
        }
    }
    return 0;
}
int maxflow(int n,int st,int ed){
	int flow=0;
	for(int i=0;i<=n+1;i++)
		d[i]=gap[i]=0;
	gap[0]=n+1;
	pre[st]=-1;
	//blk[st]=1<<30;
	for(int x=st;d[st]<=n;){
		if(x==ed){
			//int nf=blk[ed];
			for(int i=pre[ed];i!=-1;i=pre[e[i].f]){
				e[i  ].c--;
				e[i^1].c++;
			}
			flow++;
			x=st;
		}
		if(!advance(&x)){
            int mn=n;
            for(int i=es[x];i!=-1;i=e[i].ne){
                if(e[i].c&&mn>d[e[i].t]){
                    mn=d[e[i].t];
                }
            }
            if(--gap[d[x]]==0)
                break;
            gap[d[x]=mn+1]++;
            if(x!=st)
                x=e[pre[x]].f;
        }
	}
	return flow;
}
int q[N],qs,qe;
int bfs(int st,int ed){
	qs=qe=0;
	q[qe++]=st;
	d[st]=1;
	pre[st]=-1;
	for(;qs<qe;){
		int w=q[qs++];
		for(int i=es[w];i!=-1;i=e[i].ne){
			if(d[e[i].t]==0&&e[i].c){
				d[e[i].t]=1;
				pre[e[i].t]=i;
				q[qe++]=e[i].t;
			}
		}
		if(d[ed])break;
	}
	int ans=d[ed];
	for(int i=0;i<qe;i++){
		d[q[i]]=0;
	}
	return ans;
}
int maxflow2(int n,int st,int ed){
	int flow=0;
	for(;bfs(st,ed);flow++){
		for(int i=pre[ed];i!=-1;i=pre[e[i].f]){
			e[i  ].c--;
			e[i^1].c++;
		}
	}
	return flow;
}
void adde(int f,int t,int c){
	e[et]=(edge){f,t,c,-1};
	es[f]==-1?es[f]=et:e[ee[f]].ne=et;
	ee[f]=et++;
}
void addbe(int f,int t,int c){
	adde(f,t,c);
	adde(t,f,0);
}

void addbe_ex(int f,int t,int c){
	adde(f,t,c);
	adde(t,f,c);
}

int mp[514][514];
int nid(int x,int y,int z,int h,int w){
	return 2+z+2*(y+w*x);
}
void sol(int uuu){
	fprintf(stderr,"%d\n",uuu);
	int h,w;
	scanf("%d %d",&w,&h);
	for(int i=0;i<h;i++){
		for(int j=0;j<w;j++){
			mp[i][j]=0;
		}
	}
	int b;
	scanf("%d",&b);
	for(int i=0;i<b;i++){
		int sx,sy;
		int bx,by;
		scanf("%d %d %d %d",&sy,&sx,&by,&bx);
		for(int tx=sx;tx<=bx;tx++){
			for(int ty=sy;ty<=by;ty++){
				mp[tx][ty]=1;
			}
		}
	}
	/*
	for(int i=0;i<h;i++){
		for(int j=0;j<w;j++){
			printf("%d",mp[i][j]);
		}printf("\n");
	}printf("\n");
	*/
	int n=nid(h-1,w-1,1,h,w);
	for(int i=0;i<=n;i++){
		es[i]=ee[i]=-1;
	}
	et=0;
	int st=0;
	int ed=1;
	for(int j=0;j<w;j++){
		if(mp[0][j])continue;
		addbe(st,nid(0,j,0,h,w),1);
	}
	for(int i=0;i+1<h;i++){
		for(int j=0;j<w;j++){
			if(mp[i][j]||mp[i+1][j])continue;
			   addbe(nid(i+0,j,1,h,w),nid(i+1,j,0,h,w),1);
			   addbe(nid(i+1,j,1,h,w),nid(i+0,j,0,h,w),1);
			//addbe_ex(nid(i+0,j,1,h,w),nid(i+1,j,0,h,w),1);
		}
	}
	for(int i=0;i<h;i++){
		for(int j=0;j+1<w;j++){
			if(mp[i][j]||mp[i][j+1])continue;
			   addbe(nid(i,j+0,1,h,w),nid(i,j+1,0,h,w),1);
			   addbe(nid(i,j+1,1,h,w),nid(i,j+0,0,h,w),1);
			//addbe_ex(nid(i,j+0,1,h,w),nid(i,j+1,0,h,w),1);
		}
	}
	for(int j=0;j<w;j++){
		if(mp[h-1][j])continue;
		addbe(nid(h-1,j,1,h,w),ed,1);
	}
	for(int i=0;i<h;i++){
		for(int j=0;j<w;j++){
			if(mp[i][j])continue;
			addbe(nid(i,j,0,h,w),nid(i,j,1,h,w),1);
		}
	}
	int flow=maxflow2(n,st,ed);
	printf("Case #%d: %d\n",uuu,flow);
}
#include<time.h>
int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("pc_s.txt","w",stdout);
	int t;
	scanf("%d",&t);
	//t=10;
	int ttt=clock();
	for(int ti=1;ti<=t;ti++)sol(ti);
	fprintf(stderr,"time=%d\n",clock()-ttt);
	return 0;
}

