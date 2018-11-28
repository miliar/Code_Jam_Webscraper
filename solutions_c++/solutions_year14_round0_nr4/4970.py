#include <iostream>
# include <algorithm>
# include <iomanip>
# include <stdio.h>
using namespace std;
long double a[10000];
long double b[10000];
int main()
{
	freopen("CODEJAM_Q2.txt","w",stdout);
	int t;
	cin>>t;
	for (int x=1;x<=t;x++)
	{
		int n;
		cin>>n;
		for (int i=0;i<n;i++)
			cin>>a[i];
		for (int i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		int y=0;
		int z=0;
		int j=0;
		for (int i=0;i<n;i++)
		{
			for (;j<n;j++)
			{
				if (b[j]>a[i])
				{
					j++;
					y++;
					break;
				}
			}
		}
		y=n-y;
		j=0;
		for (int i=0;i<n;i++)
		{
			if (a[i]>b[j])
			{
				z++;
				j++;
			}
		}
		cout<<"Case #"<<x<<": "<<z<<" "<<y<<endl;
	}
}