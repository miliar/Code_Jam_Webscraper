#include <stdio.h>

int main() {
	int t,i,j,d;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d",&d);
		int a[d],min=0,max=0;
		for(j=0;j<d;j++){
			scanf("%d",&a[j]);
			if(max<a[j])
			max=a[j];
		}
		for(j=1;j<=max;j++){
			int k,nrml=0,spcl=0,add=0;
			for(k=0;k<d;k++){
				if(j>=a[k] && nrml<a[k]){
					nrml = a[k];
				}
				else{
					if(a[k]%j==0){
						add=a[k]/j-1;
						spcl+=add;
					}
					else{
						add=a[k]/j;
						spcl+=add;
					}
					if(j>nrml){
						nrml=j;
					}
				}
			}
			if(j==1){
				min=nrml+spcl;
			}
			else if((nrml+spcl)<min){
				min=nrml+spcl;
			}
		}
		printf("Case #%d: %d\n",i,min);
	}
	return 0;
}
