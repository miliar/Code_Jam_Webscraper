#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<math.h>
using namespace std;
int t,x,y;
int a[1000];
int main()
{
	scanf("%d",&t);
	for (int l=1;l<=t;l++)
	{
		scanf("%d%d",&x,&y);
		int k=0,kk=0,sum=0;
		for (int i=x;i<=y;i++)
		{
			k=int(sqrt(i));
			if (k*k==i)
			{
				int p=0,p1=0,l=0,r=0;
				memset(a,0,sizeof(a));
				while (k>0)
				{
					a[0]++;
					a[a[0]]=k%10;
					k/=10;
				}
				if (a[0]%2==0)
				{
					l=1; r=a[0];
					while (l<r)
					{
						if (a[l]!=a[r]) {p1=1; break;}
						l++;
						r--;
					}
				}
				else
				{
					l=1; r=a[0];
					while (l<=r)
					{
						if (a[l]!=a[r]) {p1=1; break;}
						l++;
						r--;
					}
				}

				kk=i;
				memset(a,0,sizeof(a));
				while (kk>0)
				{
					a[0]++;
					a[a[0]]=kk%10;
					kk/=10;
				}
				if (a[0]%2==0)
				{
					l=1; r=a[0];
					while (l<r)
					{
						if (a[l]!=a[r]) {p=1; break;}
						l++;
						r--;
					}
				}
				else
				{
					l=1; r=a[0];
					while (l<=r)
					{
						if (a[l]!=a[r]) {p=1; break;}
						l++;
						r--;
					}
				}
				if (p==0 && p1==0) sum++;
			}
		}
		printf("Case #%d: %d\n",l,sum);
	}
	return 0;
}
