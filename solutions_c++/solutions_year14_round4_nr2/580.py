#include <stdio.h>
#include <algorithm>
int n,su[1001],order[1001],print;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,testt,i,j,min,t;
	scanf("%d",&testt);
	for(test=1;test<=testt;test++){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d",&su[i]);
		}
		print=0;
		int s=0,e=n-1;
		for(i=0;i<n;i++){
			min=0x7fffffff;
			for(j=s;j<=e;j++){
				if(min>su[j]){
					min=su[j];
					t=j;
				}
			}
			if(t-s>e-t){
				print+=e-t;
				for(j=t;j<e;j++){
					su[j]=su[j+1];
				}
				e--;
			}
			else{
				print+=t-s;
				for(j=t;j>s;j--)
					su[j]=su[j-1];
				s++;
			}
		}
		printf("Case #%d: %d\n",test,print);
	}
	return 0;
}
