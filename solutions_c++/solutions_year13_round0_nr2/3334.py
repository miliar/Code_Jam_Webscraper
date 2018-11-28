#include<iostream>
#include<math.h>

#define FOR(i,n) for(i=0;i<n;i++)
#define max 100
using namespace std;

int maximum(int a, int b)
{
	if(a>b)
		return a;
	return b;
}

int main()
{
	int i,j,t,n,m,a[100][100],diff[100][100],minr,minc,temp=1,k;
	cin>>t;
	while(t--)
	{
		cin>>n>>m;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				cin>>a[i][j];
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				diff[i][j]=max-a[i][j];
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				minr=minc=101;
				for(k=0;k<m;k++)
					if(diff[i][k]<minr)
						minr=diff[i][k];
				for(k=0;k<n;k++)
					if(diff[k][j]<minc)
						minc=diff[k][j];
				a[i][j]+=maximum(minr,minc);
			}
		}

		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
				if(a[i][j]!=max)
					break;
			if(j!=m)
				break;
		}
		if(i==n)
			cout<<"Case #"<<temp++<<": YES";
		else
			cout<<"Case #"<<temp++<<": NO";
		if(t!=0)
			cout<<endl;
	}
	return 0;
}
