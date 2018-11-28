#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,n,m,q,i,j,k,last,x[22],y[22],z[22][2],u[22],p[22],o[22],e[22];
int main() {
  freopen("Cs.in","r",stdin);
  freopen("Cs.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d%d",&n,&m,&q);
	for (i=0; i<m; i++)
	  scanf("%d%d%d%d",&x[i],&y[i],&z[i][0],&z[i][1]);
	last=0;
	for (i=0; i<q; i++) {
	  scanf("%d",&e[i]);
	  e[i]--;
	}
	for (i=0; i<(1<<m); i++) {
	  for (j=1; j<=n; j++) o[j]=p[j]=1000000000;
	  p[1]=0; o[2]=0;
	  for (j=0; j<m; j++) u[j]=(i>>j)&1;
	  for (j=0; j<n; j++) {
	    for (k=0; k<m; k++) {
		  p[y[k]]=min(p[y[k]],p[x[k]]+z[k][u[k]]);
		  o[x[k]]=min(o[x[k]],o[y[k]]+z[k][u[k]]);
		}
	  }
	  for (; last<q; last++) {
	    j=e[last];
	    if (p[x[j]]+z[j][u[j]]+o[y[j]]>p[2]) break;
	  }
	}
    printf("Case #%d: ",t);
	if (last==q) puts("Looks Good To Me"); else printf("%d\n",e[last]+1);
  }
  return 0;
}
