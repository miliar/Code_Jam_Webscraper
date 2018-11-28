#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int main(void){
	freopen("2014Q_pD_L.in","r",stdin);
	freopen("2014Q_pD_L.txt","w",stdout);
	int t,hh;
	scanf("%d",&t);
	for(hh=1;hh<=t;hh++){
		int n,i;
		double s1[1005],s2[1005];
		scanf("%d",&n);
		for(i=0;i<n;i++)
		  scanf("%lf",&s1[i]);
		for(i=0;i<n;i++)
		  scanf("%lf",&s2[i]);
		sort(s1,s1+n);
		sort(s2,s2+n);
		int j=0;
		int ans1=0,ans2=0;
		for(i=0;i<n&&j<n;i++){
			while(s2[j]<=s1[i]&&j<n) j++;
			if(j<n) j++,ans2++;
		}
		i=0;
		for(j=0;j<n&&i<n;j++){
			while(s1[i]<=s2[j]&&i<n) i++;
			if(i<n) i++,ans1++;
		}  
	/*	for(i=0;i<n;i++)
		  printf("%.3lf ",s1[i]);
		printf("\n");
		for(i=0;i<n;i++)
		  printf("%.3lf ",s2[i]);
		printf("\n");  */
		printf("Case #%d: %d %d\n",hh,ans1,n-ans2);
	}
	return 0;
}
