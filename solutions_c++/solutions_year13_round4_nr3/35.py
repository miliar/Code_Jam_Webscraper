#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int t,tt,n,it,i,l[2020],a[2020],u[2020],k[2020],r[2020];
vector<int> g[2020],v[2020];
bool cmp(int i, int j) { return v[i]<v[j]; }
void dfs(int i) {
  u[i]=it;
  for (int j=0; j<g[i].size(); j++) if (u[g[i][j]]!=it) dfs(g[i][j]);
}
int main() {
  freopen("Cl.in","r",stdin);
  freopen("Cl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n);
	for (i=0; i<=n; i++) {
	  g[i].clear();
	  l[i]=-1;
	}
	for (i=0; i<n; i++) {
	  scanf("%d",&a[i]);
	  if (l[a[i]]!=-1) g[i].push_back(l[a[i]]);
	  if (l[a[i]-1]!=-1) g[l[a[i]-1]].push_back(i);
	  l[a[i]]=i;
	}
	for (i=0; i<n; i++) scanf("%d",&a[i]);
	for (i=0; i<=n; i++) l[i]=-1;
	for (i=n-1; i>=0; i--) {
	  if (l[a[i]]!=-1) g[i].push_back(l[a[i]]);
	  if (l[a[i]-1]!=-1) g[l[a[i]-1]].push_back(i);
	  l[a[i]]=i;
	}
	for (i=0; i<n; i++) {
	  ++it;
	  dfs(i);
	  v[i].clear();
	  for (int j=0; j<n; j++) if (u[j]==it) v[i].push_back(j);
	  v[i].push_back(n);
	  k[i]=i;
	}
	sort(k,k+n,cmp);
	for (i=0; i<n; i++) r[k[i]]=i+1;
    printf("Case #%d:",t);
	for (i=0; i<n; i++) printf(" %d",r[i]);
	puts("");
  }
  return 0;
}
