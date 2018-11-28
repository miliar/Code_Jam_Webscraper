#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	int t,i,j,n,k,flag;
	int ans1=0,ans2=0;
	double x;
	scanf("%d",&t);
	vector<double> a,b,u,v;
	for(i=1;i<=t;i++)
	{
		a.clear();
		b.clear();
		u.clear();
		v.clear();
		ans1=0,ans2=0;
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%lf",&x);
			a.push_back(x);
			u.push_back(0);
		}
		for(j=0;j<n;j++)
		{
			scanf("%lf",&x);
			b.push_back(x);
			v.push_back(0);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());

		// plays dwar optimally
		for(j=0;j<n;j++)
		{
			flag=0;
			for(k=0;k<n;k++)
			{
				if(!v[k])
				{
					flag=1;
					if(a[j]>b[k])
					{
						ans1++;
						v[k]++;
						flag=2;
					}
					break;
				}
			}
			if(flag==1)
			{
				for(k=n-1;k>=0;k--)
				{
					if(a[j]<b[k] && !v[k])
					{
						v[k]++;
						break;
					}
				}
			}
		}
		//plays war optimally
		for(j=0;j<n;j++)
		{
			flag=0;
			for(k=0;k<n;k++)
			{
				if(b[k]>a[j] && !u[k])
				{
					u[k]++;
					flag=1;
					break;
				}
			}
			if(!flag)
			{
				ans2++;
				for(k=0;k<n;k++)
				{
					if(b[k]<a[j] && !u[k])
					{
						u[k]++;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d %d\n",i,ans1,ans2);
		/*
		   for(j=0;j<n;j++)
		   {
		   printf("%lf ",a[j]);
		   }
		   printf("\n");
		   for(j=0;j<n;j++)
		   {
		   printf("%lf ",b[j]);
		   }
		   printf("\n");
		   */
	}
	return 0;
}
