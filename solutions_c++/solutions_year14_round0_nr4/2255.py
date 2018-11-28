#include<iostream>
#include<cstdio>
#include<queue>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;

double a[1005],b[1005];

int main(){
	int t,l=0;
	scanf("%d",&t);
	while(l++<t){
		int n,i,j;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf",a+i);
		for(i=0;i<n;i++)
			scanf("%lf",b+i);
		sort(a,a+n);
		sort(b,b+n);
		/*for(i=0;i<n;i++)
			printf("%lf ",a[i]);
		cout << endl;
		for(i=0;i<n;i++)
			printf("%lf ",b[i]);
		cout << endl;
		*/
		i=0;j=0;
		for(i=0;i<n;i++){
			while(j<n && a[i]>b[j])
				j++;
			if(j==n)
				break;
			j++;
		}
		int ans1=0,ans2;
		ans2=n-i;
		j=0;
		//reverse(b,b+n);
		for(i=0;i<n;i++){
			if(j<n && a[i]>b[j]){
				j++;
				ans1++;
			}
			//else if(j<n && a[i]<b[j])
				//j++;
		}
		printf("Case #%d: %d %d\n",l,ans1,ans2);
	}
	return 0;
}