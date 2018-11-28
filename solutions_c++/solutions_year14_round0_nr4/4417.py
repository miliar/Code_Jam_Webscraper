#include <iostream>
#include <assert.h>
using namespace std;
int main() {
	int t,i,j,m,n;
	int ans1,ans2;
	FILE *fp;
	fp=fopen("ans","w");
	assert(fp!=NULL);
	cin>>t;
	for(m=0;m<t;m++){
		ans1=0;
		ans2=0;
		cin>>n;
		double a[n],b[n];
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		i=0;
		j=0;
		while(i<n){
			if(a[i]>b[j]){
				ans1++;
				i++;
				j++;
			}
			else if(a[i]<b[j]){
				i++;
			}
			else{
				i++;
			}
		}
		i=0;
		j=0;
		while(j<n){
			if(a[i]<b[j]){
				ans2++;
				i++;
				j++;
			}
			else if(a[i]>b[j]){
				j++;
			}
			else{
				j++;
			}
		}
		ans2=n-ans2;
		printf("Case #%d: %d %d\n",m+1,ans1,ans2);
		fprintf(fp,"Case #%d: %d %d\n",m+1,ans1,ans2);

	}
	fclose(fp);
}

