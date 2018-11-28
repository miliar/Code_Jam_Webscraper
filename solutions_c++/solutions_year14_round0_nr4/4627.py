#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <cmath>
using namespace std;

ifstream cin("D-large.in");
ofstream cout("out.txt");

int n;
double a[1005],b[1005];

void work1()
{
	int i,j,k,l;
	j=n;
	l=0;
	k=0;
	for (i=n;i>0;i--)
	{
		while (j>l&&a[i]<b[j]) j--;
		if (j==l) break;
		k++;
		j--;
		if (j==l) break;
	}
	cout<<k;
}

void work2()
{
	int i,j;
	j=1;
	for (i=1;i<=n;i++)
	{
		while (j<=n&&a[i]>b[j]) j++;
		if (j==n+1) break;
		j++;
		if (j==n+1)
		{
			i++;
			break;
		}
	}
	cout<<n-i+1;
}

int main()
{
	int i,j,k,l,t,count=0;
	cin>>t;
	while (t--)
	{
		count++;
		cout<<"Case #"<<count<<": ";
		cin>>n;
		for (i=1;i<=n;i++)
			cin>>a[i];
		for (i=1;i<=n;i++)
			cin>>b[i];
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);
		work1();
		cout<<" ";
		work2();
		cout<<endl;
	}
	return 0;
}