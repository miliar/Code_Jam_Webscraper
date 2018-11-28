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

#define N 2020
VI a[N];

int main()
{
	freopen("c2.in","r",stdin);
	freopen("c2.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    int n;
    scanf("%d",&n);
    int inc[N],dec[N];
    for(int i=0;i<n;i++) a[i].cl;
    for(int i=0;i<n;i++) scanf("%d",inc+i);
    for(int i=0;i<n;i++) scanf("%d",dec+i);
    int deg[N]={0};
    int prev[N];
    fill(prev,-1);
    for(int i=0;i<n;i++)
    {
      int k = inc[i];
      int j = prev[k];
      if(j>=0) {
        a[i].pb(j);
        deg[j]++;
      }
      j = prev[k-1];
      if(j>=0) {
        a[j].pb(i);
        deg[i]++;
      }
      prev[k] = i;
    }
    fill(prev,-1);
    for(int i=n;i--;)
    {
      int k = dec[i];
      int j = prev[k];
      if(j>=0) {
        a[i].pb(j);
        deg[j]++;
      }
      j = prev[k-1];
      if(j>=0) {
        a[j].pb(i);
        deg[i]++;
      }
      prev[k] = i;
    }
    int mark[N]={0};
    set<int> st;
    for(int i=0;i<n;i++)
      if(deg[i]==0) {
        st.insert(i);
        mark[i]=1;
      }
    int res[N];
    for(int k=1;st.sz;k++)
    {
      int u = *st.begin();
      st.erase(st.begin());
      res[u]=k;
      for(int i=a[u].sz;i--;)
      {
        int v=a[u][i];
        deg[v]--;
        if(deg[v]==0) {
          st.insert(v);
          mark[v]=1;
        }
      }
    }
    for(int i=0;i<n;i++)
      printf("%d%c",res[i],i<n-1?' ':'\n');
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
