#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
bool q1,q2,q3,q4;
char a[105][105];
int t,n,m;

bool check()
{
	q1=false;
	q2=false;
	for (int i1=0;i1<n;i1++)
		for (int j1=0;j1<m;j1++)
		{
			for (int l=0;l<n;l++)
				if (a[l][j1]>a[i1][j1])
					q1=true;

			for (int l=0;l<m;l++)
				if (a[i1][l]>a[i1][j1])
					q2=true;
		if (q1 && q2) 
			return false;
		q1=false;
		q2=false;
		}
	 return true;
}

int main()
{
	freopen("B-small-attempt3.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;

	for (int k=0;k<t;k++)
	{
		cin>>n>>m;
		
		for (int i=0;i<100;i++)
			for (int j=0;j<100;j++)
				a[i][j]=0;

		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				cin>>a[i][j];

		if (n==1 || m==1) 
		{
			cout<<"Case #"<<k+1<<": YES"<<endl;
			continue;
		}

		if (check())
			cout<<"Case #"<<k+1<<": YES";
		else cout<<"Case #"<<k+1<<": NO";
		cout<<endl;
	}

	return 0;
}