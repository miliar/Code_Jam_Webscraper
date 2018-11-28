#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#define MAX(a,b) a>b?a:b;
#define MIN(a,b) a<b?a:b;
typedef long long int lld;
using namespace std;

int main()
{
	int t,n,i,j,a[6][6],b[6][6],x,m;
	int count, ans;
	cin>>t;
	x=0;
	while(t--)
	{
		x++;
		cin>>n;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		cin>>a[i][j];
		
		cin>>m;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		cin>>b[i][j];
		count=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[n-1][i]==b[m-1][j])
				{
					ans=a[n-1][i];
					count++;
					break;
				}
			}
		}
		if(count==1)
		cout<<"Case #"<<x<<": "<<ans<<endl;
		
		else if(count==0)
		cout<<"Case #"<<x<<": Volunteer cheated!\n";
		
		else
		cout<<"Case #"<<x<<": Bad magician!\n";
		
	}
	return 0;
}

