#include<cstring>
#include<set>
#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("pp3.txt","w",stdout);
	int t,count = 1;
	scanf("%d",&t);
	while(t--) {
	int i,j,kl;
	int n;
	scanf("%d",&n);
	double m[n];
	double k[n];
	double k1[n];
	for(i=0;i<n;i++)
	scanf("%lf",&m[i]);
	for(i=0;i<n;i++) {
	scanf("%lf",&k[i]);
}
	sort(m,m+n);
	sort(k,k+n);
	for(i=0;i<n;i++)
	k1[i]=k[i];
	//for(i=0;i<n;i++)
	//printf("%lf ",k1[i]);
	int f=0;
	int a1=0,a2=0;
	for(i=n-1;i>=0;i--) {
		for(j=n-1;j>=0;j--) {
			if(m[i]>k[j] && k[j]!=-1){
				a1++;
				k[j] = -1;
				break;
			}
		}
	}
//	printf("a1 : %d\n",a1);\
a2 = 0;
int p=0;
	for(i=0;i<n;i++) {
		for(j=0;j<n;j++) {
			if(k1[i]>m[j] && m[j]!=-1) {
				//printf("%lf %lf\n",m[i],k1[j]);
				m[j]=-1;
				a2++;
				//p = j+1;
				break;
				
			}
		}
	}
	printf("Case #%d: %d %d\n",count++,a1,n-a2);
	
}
fclose(stdin);
fclose(stdout);
return 0;
}
