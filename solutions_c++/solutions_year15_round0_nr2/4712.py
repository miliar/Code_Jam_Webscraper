#include <cstdio>  
#include <cstring>  
#include <algorithm>  
using namespace std ;  
int main()
{
int test,n,x,i,j;
	scanf("%d",&test);
	for(x=0;x<test;x++){
		scanf("%d",&n);
		int a[n];
		for(j=0;j<n;j++)
		 scanf("%d",&a[j]);
		int bc=a[0];
		j=1;
		while(j<n){
			if(a[j]>bc)bc=a[j];
			j++;
		}
		int m1=bc,s;
		for(i=1;i<bc+1;i++){
			s=i;
			for(j=0;j<n;j++){
				if(a[j]>i){
					if(a[j]%i==0)
						s+=((a[j]/i)-1);
					else 
						s+=a[j]/i;
				}
 
			}
			m1=min(m1,s);	
		}
		int r=m1;
		printf("Case #%d: %d\n",x+1,r);
	}
	//system("PAUSE");
	return 0;
}
