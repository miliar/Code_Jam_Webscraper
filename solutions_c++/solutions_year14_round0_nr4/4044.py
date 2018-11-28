#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

bool cmp(double x,double y){
	return x>y;
}
double a[1500],b[1500];
int main(){
	int cases,n;
	freopen("D-large.in","r",stdin);
	freopen("DLout.out","w",stdout);
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%lf",&a[i]);
		for (int i=1;i<=n;i++) scanf("%lf",&b[i]);
		sort(a+1,a+1+n,cmp);
		sort(b+1,b+1+n,cmp);
		int ans1=0,ans2=0;
		for (int i=1,j=1;i<=n&&j<=n;){
			if (a[i]>b[j]){
				i++;j++;
				ans1++;
			}
			else j++;
		}
		for (int i=1,j=1;i<=n&&j<=n;){
			if (a[i]<b[j]){
				i++;j++;
				ans2++;
			}
			else i++;
		}
		printf("Case #%d: %d %d\n",cas,ans1,n-ans2);	
	}
	return 0;
}
