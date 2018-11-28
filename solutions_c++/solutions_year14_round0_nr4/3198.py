#include<iostream>
#include<algorithm>
#include<stdio.h>

using namespace std;

double a[1010],b[1010];

int find1(int n){
	int i=0,j=0,k=0,flag,count=0;
	while(i<n && j<n ){
		flag=0;
		if(a[i]>b[j]){
			j++;	
		}
		else{
			flag=1;
			count+=(j-k);
			j++;
			k=j;
			i++;	
		}
	}
	if(flag==0)
		count+=(j-k);

	return count;

}


int find2(int n){
	int i=0,j=0,flag=0,lim,count=0;

	while(i<n && j<n){
		if(a[i]>b[j]){
			i++;
			j++;
			count++;

		}
		else{
			i++;
			
		}

			
	}
	return count;
}


int main(){
	int t,k,n,i,j,count1,count2;


	scanf("%d",&t);
	for(k=1;k<=t;k++){
		count1=0;
		count2=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		    scanf("%lf",&a[i]);

		for(i=0;i<n;i++)
			scanf("%lf",&b[i]);

		sort(a, a+n);
		sort(b, b+n);

		/*for(i=0;i<n;i++){
			printf("%.3lf\t",a[i] );
		}
		printf("\n");
		for(i=0;i<n;i++){
			printf("%.3lf\t",b[i] );
		}
		*/
	

	

		
		printf("Case #%d: %d ",k,find2(n));
		printf("%d\n",find1(n));







	}






	return 0;
}