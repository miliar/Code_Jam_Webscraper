#include <cstdio>
const int MAXN=100;
int T,a[MAXN][MAXN],m1[MAXN],m2[MAXN];
int main(){
   scanf("%d",&T);
   for(int Testcase=0;Testcase<T;++Testcase){
      int n,m;
      scanf("%d%d",&n,&m);
      for(int i=0;i<n;++i){
	 m1[i]=0;
	 for(int j=0;j<m;++j){
	    scanf("%d",&(a[i][j]));
	    if(a[i][j]>m1[i]) m1[i]=a[i][j];
	 }
      }
      for(int i=0;i<m;++i){
	 m2[i]=0;
	 for(int j=0;j<n;++j)
	    if(a[j][i]>m2[i]) m2[i]=a[j][i];
      }
      int flag=1;
      for(int i=0;i<n;++i)
	 for(int j=0;j<m;++j)
	    if((a[i][j]<m1[i])&&(a[i][j]<m2[j])) flag=0;
      printf("Case #%d: ",Testcase+1);
      if(flag) printf("YES\n");
      else printf("NO\n");
   }
}
