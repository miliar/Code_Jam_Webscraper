#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int main()
{
	freopen("D-large.in ","r",stdin);
	freopen("ku2.txt","w",stdout);
	int t,c = 1;
	scanf("%d",&t);
	while( t-- ) {
	int i,j,n;
	scanf("%d",&n);
	double naomi[n];
	double ken[n];
	double ken1[n];
	for(i=0;i<n;i++)
	scanf("%lf",&naomi[i]);
	for(i=0;i<n;i++) {
	scanf("%lf",&ken[i]);
}
	sort(naomi,naomi+n);
	sort(ken,ken+n);
	for(i=0;i<n;i++)
	ken1[i]=ken[i];
	int f=0;
	int ans1=0,ans2=0;
	for(i=n-1;i>=0;i--) {
		for(j=n-1;j>=0;j--) {
			if(naomi[i]>ken[j] && ken[j]!=-1){
				ans1++;
				ken[j] = -1;
				break;
			}
		}
	}
	for(i=0;i<n;i++) {
		for(j=0;j<n;j++) {
			if(ken1[i]>naomi[j] && naomi[j]!=-1) {
				naomi[j]=-1;
				ans2++;
				break;
				
			}
		}
	}
	printf("Case #%d: %d %d\n",c++,ans1,n-ans2);
	
}
fclose(stdin);
fclose(stdout);
return 0;
}
