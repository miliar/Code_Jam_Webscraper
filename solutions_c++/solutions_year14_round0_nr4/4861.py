#include <iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main() {
int test,n,i,j,ans1=0,ans2=0;
cin>>test;
int t1=test;
while(test--)
{
	ans1=0;ans2=0;
scanf("%d",&n);
float a[n],b[n],c[n];
for(i=0;i<n;i++)
scanf("%f",&a[i]);
for(i=0;i<n;i++)
scanf("%f",&b[i]);
sort(a,a+n);
sort(b,b+n);
for(i=0;i<n;i++)
c[i]=b[i];
for(i=0;i<n;i++)
	for(j=0;j<n;j++)
			if(a[i]>b[j])
			{	ans1++;b[j]=1;break;}
for(i=0;i<n;i++)
for(j=0;j<n;j++)
			if(c[i]>a[j])
			{
				ans2++;
				a[j]=1;break;}
			printf("Case #%d: %d %d\n",t1-test,ans1,n-ans2);
			ans1=ans2=0;
}

	return 0;
}