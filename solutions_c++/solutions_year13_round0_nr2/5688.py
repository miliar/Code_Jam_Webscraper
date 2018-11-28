#include<iostream>
#include<fstream>

using namespace std;
int check(int x,int y,int c,int d);
int a[11][11];

int main()
{
		freopen("B-small-attempt1.in","r",stdin);
		freopen("output18.in","w",stdout);

	int T;
	cin>>T;
	int z=T;
	while(T--)
	{
		int m,n,i,j,f=0;
		
		cin>>n>>m;
		
		for(i=0;i<11;i++)
		{
			for(j=0;j<11;j++)
			{
				a[i][j]=0;
			}
		}
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				cin>>a[i][j];
			}
		}
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(a[i][j]==1)
				f=check(i,j,m,n);
				if(f==1)
				break;
			}
			if(f==1)
			break;
		}
		if(f==0)
		cout<<"Case #"<<z-T<<": YES"<<endl;
		else
		cout<<"Case #"<<z-T<<": NO"<<endl;		
	}
}

int check(int x,int y,int c,int d)
{
	
	int r,countx=0,county=0;
	
	for(r=0;r<d;r++)
	{
	//	cout<<r<<" "<<y<<" "<<a[r][y]<<endl;
		if(a[r][y]==1)
		{
			countx++;	
		}
		
	}
	
	for(r=0;r<c;r++)
	{
		if(a[x][r]==1)
		county++;
	}
	
	if(countx==d||county==c)
	{
		return 0;	
	}
	else
	{
	//	cout<<"countx is "<<countx<<" county is "<<county<<endl;
	//	cout<<"i is "<<x<<" j is "<<y<<endl;
		return 1;
	}

}
