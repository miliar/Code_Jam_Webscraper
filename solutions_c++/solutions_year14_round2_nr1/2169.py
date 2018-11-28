#include <cstdio>
#include <queue>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <utility>
#define pii pair<int, int>
#define VI vector < int >
#define PB push_back
#define FOR(i,a,b) for(i=a;i<b;i++)
#define FORD(i,a,b) for(i=a;i>b;i--)
typedef long long LL;
using namespace std;
int main()
{
	int i,j,k,n,t;
	cin>>t;
	int a[120][101];
	int max1;
	for(k=1;k<=t;k++)
	{
		cin>>n;
		char b[200];
		char arr[103];
		cin>>b;
		for(j=0;j<=100;j++)
			a[0][j]=0;
		i=0;
		for(j=0;b[j]!='\0';j++)
		{
			arr[i]=b[j];
			a[0][i]++;
		//	cout<<"b="<<b[j]<<" "<<a[0][i]<<endl;
			while(b[j]==b[j+1])
			{
				a[0][i]++;	
				j++;
			}
			i++;
		}
		int win=0;
		for(i=1;i<n;i++)
		{
			for(j=0;j<=100;j++)
				a[i][j]=0;
			cin>>b;
			int yy=0;
			for(j=0;b[j]!='\0';j++)
			{
				if(b[j]==arr[yy])
				{
					a[i][yy]++;
				}
				else
				{
					yy++;
					if(b[j]==arr[yy])
					{
						a[i][yy]++;
					}
					else
						win=1;
				}
			}
			max1=max(max1,yy);
	
		}
//		for(i=0;i<4;i++)
//		{	cout<<a[0][i]<<" "<<arr[i]<<endl;
//			cout<<a[1][i]<<" "<<arr[i]<<endl;
//		}
		long int ans=0;
		for(j=0;j<=max1;j++)
		{
			int zero=0;
			int sum=0;
			for(i=0;i<n;i++)
			{
				sum+=a[i][j];
				if(a[i][j]==0)
				{
					zero=1;
				}
			}
			if(zero==1 && sum!=0)
			{
				win=1;
				break;
			}
			int avg=sum/n;
			if(sum%n > n/2.0)
				avg++;
			for(i=0;i<n;i++)
				ans+=abs(a[i][j]-avg);
		}
		if(win==1)
		{
			cout<<"Case #"<<k<<": "<<"Fegla Won\n";
		}
		else
			cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}

