#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
		freopen("D-large.in","r",stdin);
		freopen("output.txt","w",stdout);
	int t,t1=0,i,n,p,q,ans1,ans2;
	float a[1002],b[1002];
	scanf("%d",&t);
	while(t--)
	{
		t1++; ans1=0; ans2=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%f",&a[i]);
		}
		sort(a,a+n);
		for(i=0;i<n;i++)
		{
			scanf("%f",&b[i]);
		}
		sort(b,b+n);
		
	//	for(i=0;i<n;i++)
	//	{
	//		cout<<a[i]<<" ";
	//	}
	//	cout<<endl;
		p=0; q=n-1;	
		for(i=n-1;i>=0;i--)
		{
			if(p==q && a[i] < b[p])
			{
				break;
			}
			else if(p==q && a[i] > b[p])
			{
				ans2++; break;
			}
			else if(a[i] < b[p])
			{
				p++; 
			}
			else if(a[i] > b[p] && a[i] > b[q] && p!=q)
			{
				ans2++; p++;
			}
			else if(a[i] > b[p] && a[i] < b[q] && p!=q)
			{
				 q--;
			}
		}
		p=0; q=n-1;
		for(i=0;i<n;i++)
		{
			if(a[i] > b[p] && p==q)
			{
				ans1++; break;
			}
			if(a[i] > b[p] && p!=q)
			{
				ans1++; p++;
			}
			else if(a[i] < b[p] && p!=q)
			{
				q--;
			}
			else if(a[i] > b[p] && a[i] < b[q] && p!=q)
			{
				ans1++; p++;
			}
		}
		
		printf("Case #%d: %d %d\n",t1,ans1,ans2);
	}
	return 0;
}
