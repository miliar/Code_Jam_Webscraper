#include<bits/stdc++.h>
using namespace std;
int war(double a[], double b[],int n)
{
	int i,j,ctr=0;;
	for(  i = 0,j =0;i<n && j < n;){
		if(a[i] > b[j]){
			j++;
		}
		else {
			ctr++;
			j++;
			i++;
		}
	}
	return ctr;
}
int main()
{
	freopen("ques.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int t,n,i,x=0;
	scanf("%d",&t);
	while(t--){
		x++;
		scanf("%d",&n);
		double a[n];
		double b[n];
		for(i = 0 ;i<n;i++){
			scanf("%lf",&a[i]);
		}
		for(i=0;i<n;i++){
			scanf("%lf",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		printf("Case #%d: %d",x,war(b,a,n));
		printf(" %d\n",n-war(a,b,n));
	}
	fclose(stdout);
}
