#include<bits/stdc++.h>
using namespace std;
int main()
{
	int i,j,t,n,k=1,ans1,ans2;
	float a[10000],b[10000];
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%f",&a[i]);
		}
		for(i=0;i<n;i++){
			scanf("%f",&b[i]);
		}
		ans1=0;ans2=0;
		sort(a,a+n);
		sort(b,b+n);
		for(i=0,j=n-1;i<n;i++,j--){
			if(a[j]>b[i]){
				ans1++;
			}
			if(a[i]>b[j]){
				ans2++;
			}
		}
		printf("Case #%d: %d %d\n",k++,ans1,ans2);
	}
	return 0;
}
