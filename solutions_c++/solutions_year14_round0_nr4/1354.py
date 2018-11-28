#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
double a[1010],b[1010];
int ans1,ans2,T,i,N,j;
bool v[1010];

void work1(){
  memset(v,1,sizeof(v));
  ans1=0;
  for (i=1;i<=N;i++){
  	for (j=1;j<=N;j++)
  	 if (v[j] && b[j]>a[i])
	  {v[j]=0;break;}
	if (j>N)
	 for (j=1;j<=N;j++)
	  if (v[j]) {ans1++;v[j]=0;break;}
  }
}

void work2(){
  ans2=0;
  for (i=1,j=1;i<=N;i++)
  	if (a[i]>b[j]) ans2++,j++;
}

int main(){
  //freopen("a.in","r",stdin);
  //freopen("a.out","w",stdout);
  int T;
  scanf("%d",&T);
  for (int I=1;I<=T;I++){
  	scanf("%d",&N);
  	for (i=1;i<=N;i++) scanf("%lf",&a[i]);
  	for (i=1;i<=N;i++) scanf("%lf",&b[i]);
  	sort(a+1,a+N+1);
  	sort(b+1,b+N+1);
  	work1();
  	work2();
  	printf("Case #%d: %d %d\n",I,ans2,ans1);
  }
  return 0;
}
