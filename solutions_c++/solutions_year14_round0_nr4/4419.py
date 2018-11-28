#include <iostream>
#include <algorithm>
#include <cstdlib>
double a[1010],b[1010];
int ai[1010],bi[1010];
using namespace std;
int main(int argc, char *argv[]) {
	
	FILE *f1;
	f1 = fopen("A-small-attempt0.out.txt","w");
	int t,T,n,i,j,pf,pr;
	
	scanf("%d",&T);
	
	for(t=0;t<T;t++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lf",&a[i]);
			ai[i]=1;
		}
		for(i=0;i<n;i++)
				{
					scanf("%lf",&b[i]);
					bi[i]=1;
				}
		sort(a,a+n);
		reverse(a,a+n);  
		sort(b,b+n);
		reverse(b,b+n);
		fprintf(f1,"Case #%d: ",t+1); 
		pf=0;pr=n-1;
		int cnt=0;
		for(i=0;i<n;i++){
			if(b[i]>a[pf])
			{
				pr--;
			}
			if(b[i]<a[pf])
			{
				pf++;
				cnt++;
			}
		}
		fprintf(f1,"%d ",cnt);
		pr=n-1;pf=0;
		cnt=0;
		for(i=0;i<n;i++){
				if(a[i]>b[pf])
				{
					pr--;
				}
				if(a[i]<b[pf])
				{
					pf++;
					cnt++;
				}
			}
fprintf(f1,
"%d\n",n-cnt);
	}
	
}
//	for(i=0;i<n;i++)
//					{
//						printf("%lf",b[i]);
//						
//					}	
//					printf("\n");	
//		for(i=0;i<n;i++)
//							{
//								printf("%lf",a[i]);
//							}	
//	}