#include<stdio.h>
#include<algorithm>
using namespace std;
double arr[1000],arr2[1000];
bool fun(double x,double y){
	if(x>y)return true;
	return false;
}
int main(){
int i,j,t,n,k,c1,c2;
scanf("%d",&t);
for(k=1;k<=t;k++){
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%lf",&arr[i]);
	}
	for(i=0;i<n;i++){
		scanf("%lf",&arr2[i]);
	}
	sort(arr,arr+n);
	sort(arr2,arr2+n);
	//for(i=0;i<n;i++)printf("%.3f ",arr[i]);printf("\n");
	//for(i=0;i<n;i++)printf("%.3f ",arr2[i]);printf("\n");
	c1=c2=0;
	j=0;	
	for(i=0;i<n;i++){
		while(j<n&&arr[j]<arr2[i])j++;
		if(j<n)c1++;
		else break;
		j++;
	}
	j=0;
	for(i=0;i<n;i++){
		while(j<n&&arr[i]>arr2[j])j++;
		if(j<n)c2++;
		else break;	
		j++;
	}
	printf("Case #%d: %d %d\n",k,c1,n-c2);
}
return 0;
}


		
	





