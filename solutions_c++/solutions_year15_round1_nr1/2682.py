#include<iostream>
#include<string>
#include<cstdio>

using namespace std;

int main()
{
	int t,n,m[10000];
	cin>>t;
	int smax,j=1;
	while(j<=t)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>m[i];
		int p=0;
		int max=m[0]-m[1];
		for(int i=1;i<n;i++)
		{
			if(m[i]<m[i-1])
				{
					p=p+m[i-1]-m[i];
					if(max<(m[i-1]-m[i]))
						max=m[i-1]-m[i];
				}
		}
		int k=0;
		for(int i=0;i<n-1;i++)
		{
			if(max!=0)
			{
			if(max>=m[i])
				k=k+m[i];
			else
				{
					k=k+max;
				}
			}
		}

		printf("Case #%d: %d %d\n",j++,p,k);
	}
	return 0;
}