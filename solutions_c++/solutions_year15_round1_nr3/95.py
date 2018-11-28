#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;
int x[3333],y[3333];
double a[6666];int la;
const double pi = acos(-1.);
double eps = 1e-12;
int n;
int main(){
	int _,T;
	scanf("%d",&_);
	for(T=1; T<=_; T++){
		scanf("%d",&n);
		for(int i=0; i<n; i++)
			scanf("%d%d",&x[i],&y[i]);
		printf("Case #%d:\n",T);
		for(int i=0; i<n; i++){
			la=0;
			for(int j=0; j<n; j++)if(j!=i)
				a[la++]=atan2(y[j]-y[i]+.0,x[j]-x[i]+.0);
			sort(a,a+la);

			int pnt=0;
			while(pnt<la && a[pnt]<-eps)pnt++;
			int pnt2=pnt;
			while(pnt2<la && a[pnt2]<eps)pnt2++;
			int res=min(pnt,n-pnt2);

			for(int j=la; j<la+la; j++)
				a[j]=a[j-la]+2*pi;

			for(int k2=0,k; k2<la; k2=k){
				for(k=k2; k<la && a[k]-a[k2]<eps; k++);
				while(pnt<la+k2 && a[pnt]-a[k2]<-eps+pi)pnt++;
				for(pnt2=pnt; pnt2<la+k2 && a[pnt2]-a[k2]<eps+pi; pnt2++);
				res=min(res,min(pnt-k,la+k2-pnt2));
			}
			printf("%d\n",res);
		}
	}
	return 0;
}
