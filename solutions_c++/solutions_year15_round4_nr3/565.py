#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#pragma comment(linker, "/STACK:266777216")
using namespace std;

#define assert(f) { if(!(f)) { fprintf(stderr,"Assertion failed: "); fprintf(stderr,#f); fprintf(stderr,"\n"); exit(1); } }

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;

const int inf=1000000000;
const LL INF=LL(inf)*inf;
const double eps=1e-9;
const double PI=2*acos(0.0);
#define bit(n) (1<<(n))
#define bit64(n) ((LL(1))<<(n))
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) (a).begin(),(a).end()
#define fill(ar,val) memset((ar),(val),sizeof (ar))
#define MIN(a,b) {if((a)>(b)) (a)=(b);}
#define MAX(a,b) {if((a)<(b)) (a)=(b);}
#define sqr(x) ((x)*(x))
#define X first
#define Y second

clock_t start=clock();

struct Dinic {
    static const int MaxN = 10000;
    static const int MaxE = 10000000;
    static const int INF = 1000000000;

    int n, src, tar, ptr;
    int head[MaxN], vert[MaxE], next[MaxE], cap[MaxE];
    int t[MaxN], q[MaxN], work[MaxN];

    Dinic (int _node) {
        n = _node;
        memset(head, -1, sizeof(head[0])*n);
        ptr = 0; }

    void addedge(int u, int v, int c1, int c2) {
        vert[ptr] = v, cap[ptr] = c1,
        next[ptr] = head[u], head[u] = (ptr++);
        vert[ptr] = u, cap[ptr] = c2,
        next[ptr] = head[v], head[v] = (ptr++); }

    bool dinic_bfs() {
        memset(t, 255, sizeof(t[0]) * n);
        t[src] = 0;
        int p1 = 0, p2 = 0;
        q[p2++] = src;
        while(p1 < p2) {
            for (int v = q[p1++], i = head[v]; i >= 0; i = next[i])
                if (cap[i] > 0 && t[vert[i]] < 0) {
                    t[vert[i]] = t[v] + 1;
                    q[p2++] = vert[i]; }}
        return t[tar] >= 0; }

    int dinic_dfs(int v, int exp) {
        if (v == tar) return exp;
        for (int &i = work[v]; i >= 0; i = next[i]) {
            int u = vert[i], tmp;
            if (cap[i] > 0 && t[u] == t[v] + 1 &&
                    (tmp = dinic_dfs(u, min(exp, cap[i]) ) ) > 0) {
                cap[i] -= tmp;
                cap[i ^ 1] += tmp;
                return tmp;	}}
        return 0; }

    int dinic_flow() {
        int ans = 0;
        while (dinic_bfs()) {
            memcpy(work, head, sizeof(head[0])*n);
            while (1) {
                int delta = dinic_dfs(src, INF);
                if (delta == 0) break;
                ans += delta; }}
        return ans; }
};


char s[1010101];

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    map<string, int> ids;
    VI sent[222];
    int cnt=0;
    int w;
    scanf("%d ",&w);
    for(int j=0;j<w;j++) {
      gets(s);
      for(int i=0;s[i];)
        if(s[i]==' ') i++; else {
          string q;
          for(;s[i] && s[i]!=' ';i++) q+=s[i];
          if(!ids.count(q)) ids[q]=++cnt;
          sent[j].pb(ids[q]);
        }
    }
    Dinic din(2*cnt+2);
    din.src=0;
    din.tar=2*cnt+1;
    for(int u=1;u<=cnt;u++)
      din.addedge(u,u+cnt,1,0);
    for(int j=0;j<w;j++) {
      for(int i=0;i<sent[j].sz;i++) {
        int u = sent[j][i];
        if(j==0) {
          din.addedge(0,u,1,0);
        } else if(j==1) {
          din.addedge(u+cnt,2*cnt+1,1,0);
        }
        for(int k=0;k<i;k++) {
          int v = sent[j][k];
          if(u!=v) {
            din.addedge(u+cnt,v,1,0);
            din.addedge(v+cnt,u,1,0);
          }
        }
      }
    }
    int res = din.dinic_flow();
    printf("%d\n",res);
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
