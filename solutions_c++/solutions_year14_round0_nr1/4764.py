#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

ifstream cin("A-small-attempt0.in");
ofstream cout("out.txt");

int a[10],b[10];

int main()
{
	int t,i,j,k,l,count=0;
	cin>>t;
	while (t--)
	{
		count++;
		cout<<"Case #"<<count<<": ";
		cin>>l;
		for (i=1;i<=4;i++)
			for (j=1;j<=4;j++)
			{
				cin>>k;
				if (i==l)
					a[j]=k;
			}
		cin>>l;
		for (i=1;i<=4;i++)
			for (j=1;j<=4;j++)
			{
				cin>>k;
				if (i==l)
					b[j]=k;
			}
		k=0;
		l=0;
		for (i=1;i<=4;i++)
			for (j=1;j<=4;j++)
				if (a[i]==b[j])
				{
					k++;
					l=a[i];
				}
		if (k==1)
		{
			cout<<l;
		}
		else if (k>1)
		{
			cout<<"Bad magician!";
		}
		else if (k==0)
		{
			cout<<"Volunteer cheated!";
		}
		cout<<endl;
	}
	return 0;
}