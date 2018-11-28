#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
const int maxn=1010;
int naomi[maxn],ken[maxn];
int n;
bool judge(int x)
{
	int tmp=0;
	for(int i=0;i<x;i++)
		if(naomi[i]<ken[n+i-x])
			tmp++;
	if(tmp==x)
		return true;
	return false;
}
bool judge1(int x)
{
	int tmp=0;
	for(int i=0;i<x;i++)
		if(ken[i]<naomi[n+i-x])
			tmp++;
	if(tmp==x)
		return true;
	return false;
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
	int t;
	double tmp;
	scanf("%d",&t);
	//cout<<"t="<<t<<endl;
	for(int ca=1;ca<=t;ca++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&tmp);
			naomi[i]=tmp*100000;
		}
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&tmp);
			ken[i]=tmp*100000;
		}
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		/*for(int i=0;i<n;i++)
			printf("%d ",naomi[i]);
		cout<<endl;
		for(int i=0;i<n;i++)
			printf("%d ",ken[i]);
		cout<<endl;
		*/
		int ans0=0,ans1=0;
		int aa=1,bb=0;
		bool flag=true;
		int l=0,r=n;
		while(l<=r)
		{
			int mid=(l+r)/2;
			if(judge(mid))
			{
				ans1=mid;
				l=mid+1;
			}
			else
				r=mid-1;
		}
		l=0,r=n;
		while(l<=r)
		{
			int mid=(l+r)/2;
			if(judge1(mid))
			{
				ans0=mid;
				l=mid+1;
			}
			else
				r=mid-1;
		}
		/*while(flag)
		{
			if(judge(aa))
			{
				aa++;
				ans0++;
			}
			else
				flag=false;
		}
		for(int i=1;i<=n;i++)
		{
			if(judge1(i))
				ans1=i;
			else  break;
		}
		*/
		printf("Case #%d: %d %d\n",ca,ans0,n-ans1);
	}
	return 0;
}
