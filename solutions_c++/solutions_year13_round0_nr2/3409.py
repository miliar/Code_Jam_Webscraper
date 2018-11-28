#include<iostream>
using namespace std;
int maxr[105],maxc[105];
int a[105][105];
int main()
{
	freopen("OUTPUT.txt", "w", stdout);
	int t;
	cin>>t;
	int _max;
	int i,j,ca;
	int n,m;
	ca=1;
	while(t--)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		for(i=0;i<n;i++)
		{
			_max=-1;
			for(j=0;j<m;j++)
			{
				if(_max<a[i][j])
				{
					_max=a[i][j];
				}
			}
			maxr[i]=_max;
		}
		for(i=0;i<m;i++)
		{
			_max=-1;
			for(j=0;j<n;j++)
			{
				if(_max<a[j][i])
				{
					_max=a[j][i];
				}
			}
			maxc[i]=_max;
		}
		bool flag=1;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(maxr[i]>a[i][j]&&maxc[j]>a[i][j])
				{
					flag=false;
					break;
				}
			}
			if(flag==false)
			{
				break;
			}
		}
		if(flag)
		{
			printf("Case #%d: YES\n",ca++);
		}
		else
		{
			printf("Case #%d: NO\n",ca++);
		}
		
	}
	return 0;
}