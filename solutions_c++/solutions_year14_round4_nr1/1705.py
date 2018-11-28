#include<iostream>
#include<iomanip>
#include<fstream>
#include<vector>
#include<map>
#include<string>
#include<queue>
#include<algorithm>
#include<cmath>
using namespace std;

int a[100000];

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	cin>>t;
	for (int ii=0;ii<t;ii++)
	{
		int n;
		int m;
		cin>>n>>m;
		for (int i=0;i<n;i++)
			cin>>a[i];
		sort(a,a+n);
		int i=0;
		int j=n-1;
		int an=0;
		while (i<=j)
		{
			an++;
			if (a[i]+a[j]<=m)
			{
				i++;
				j--;
			}
			else
			{
				j--;
			}
		}
		cout<<"Case #"<<ii+1<<": ";
		cout<<an<<'\n';
	}
}