#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int t,n,i,j;
int main(){
	freopen("4.in","r",stdin);
	scanf("%d",&t);
	for(int k = 1; k <=t; k++){
		scanf("%d",&n);
		double a[n],b[n];
		for(i = 0; i<n;i++)
			scanf("%lf",&a[i]);
		for(i = 0; i<n;i++)
			scanf("%lf",&b[i]);
		for(i=0;i<n-1;i++)
			for(j=i+1;j<n;j++){
				if(a[i]>a[j])swap(a[i],a[j]);
				if(b[i]>b[j])swap(b[i],b[j]);
			}
		int flag[n],ans1=0,ans2=0;
		memset(flag,0,sizeof(flag));
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(flag[j]==0&&a[j]>b[i]){
					flag[j]=1;
					ans1++;
					break;
				}
		int l = 0, r=n-1;
		for(i=n-1;i>=0;i--)
			if(a[i]>b[r]){
				l++;ans2++;
			}
			else {
				r--;
			}
		printf("Case #%d: %d %d\n",k,ans1,ans2);
	}
	fclose(stdin);
	return 0;
}
