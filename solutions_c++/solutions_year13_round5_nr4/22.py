#include <cstdio>
#include <cstring>
using namespace std;
int t,tt,n,i,j,mask,k,z;
double se,p,f[1100100];
char s[22];
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%s",s);
	n=strlen(s);
	for (mask=i=0; i<n; i++) if (s[i]=='.') mask|=(1<<i);
	for (i=1; i<=mask; i++) {
	//printf("%d\n",i);
	  f[i]=0;
	  if (i&(1<<(n-1))) j=0; else for (j=1; (i&(1<<(j-1)))==0; j++);
	  for (z=j; j<n; ) {
	    //printf("%d j %d\n",i,j);
	    for (k=j, p=1, se=0; ; p++) {
		//printf("k %d\n",k);
		  se+=n-p+1;
		  if (i&(1<<k)) break;
		  k++;
		  if (k>=n) k=0;
		}
		//printf("%d %d %d %.5lf %.5lf %5.lf\n",i,j,k,se,p,f[i^(1<<k)]);
		f[i]+=(se+f[i^(1<<k)]*p)/n;
		j=k+1;
		if (j==z) break;
	  }
	  //printf("%.5lf\n",f[i]);
	}
    printf("Case #%d: %.14lf\n",t,f[mask]);
  }
  return 0;
}
