#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <cctype>
#include <ctime>
#include <strstream>
#define min(a,b) ((a) < (b) ? (a) : (b)) 
#define max(a,b) ((a) > (b) ? (a) : (b)) 
using namespace std;
#define N 1005
int n;
double a[N],b[N],c[N],d[N];

bool cmp(double *p1,double *p2,int l)
{
	int i;
	for(i=0;i<l;i++)
		if(p1[i]<p2[i])return 0;
	return 1;
}
int main()
{
	ios_base::sync_with_stdio(false);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	int ki,i,j;
	scanf("%d",&cas);
	for(ki=1;ki<=cas;ki++)
	{
		printf("Case #%d: ",ki);
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
			c[i]=a[i];
		}
		for(i=0;i<n;i++)
		{
			cin>>b[i];
			d[i]=b[i];
		}
		sort(a,a+n);
		sort(b,b+n);
		//reverse(b,b+n);
		for(i=0;i<n;i++)
		{
			if(cmp(a+i,b,n-i))break;
		}
		printf("%d ",n-i);

		sort(b,b+n);
		j=0;
		for(i=0;i<n;i++)
		{
			while(j<n&&b[j]<a[i])j++;
			if(j==n)break;
			j++;
		}

		printf("%d\n",n-i);
	}
	return 0;
}