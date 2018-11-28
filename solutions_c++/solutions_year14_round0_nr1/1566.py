#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
bool v[20],g[20],flag;
int T,i,j,r1,r2,ans,a[5][5];

int main(){
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d",&T);
  for (int I=1;I<=T;I++){
  	memset(v,0,sizeof(v));
  	memset(g,0,sizeof(g));
  	scanf("%d",&r1);
  	for (i=1;i<=4;i++)
  	  for (j=1;j<=4;j++) scanf("%d",&a[i][j]);
  	for (i=1;i<=4;i++) v[a[r1][i]]=1;
  	scanf("%d",&r2);
  	for (i=1;i<=4;i++)
  	  for (j=1;j<=4;j++) scanf("%d",&a[i][j]);
  	for (i=1;i<=4;i++) g[a[r2][i]]=1;
  	ans=0; flag=1;
  	for (i=1;i<=16;i++)
  	  if (v[i] && g[i]){
  	  	if (ans==0) ans=i,flag=1;
  	  	else {flag=0;break;}
  	  }
  	printf("Case #%d: ",I);
  	if (!flag) printf("Bad magician!\n");
  	 else{
  	  if (ans) printf("%d\n",ans);
  	   else printf("Volunteer cheated!\n");
  	 }
  }
  return 0;
}
