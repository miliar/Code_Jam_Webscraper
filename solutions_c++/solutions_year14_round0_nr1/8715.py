#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int t,i,j,m,n,h[20],a[20][20],flag,num,l=1;
	
	cin>>t;
	
	for(l=1;l<=t;l++)
	{	
		for(i=1;i<=16;i++)
		{
			h[i]=0;
		}		

		cin>>m;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
	

		
		i=m-1;
		flag=0;
		for(j=0;j<4;j++)
		{
			h[a[i][j]]++;
		}

		cin>>n;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}

		i=n-1;
	
		for(j=0;j<4;j++)
		{
			h[a[i][j]]++;
		}
	
		for(i=1;i<=16;i++)
		{
			if(h[i]==2)
			{flag++;num=i;}
		}
	
	if(flag==0)
	cout<<"Case #"<<l<<": Volunteer cheated!"<<endl;
	
	else if(flag>1) 
	cout<<"Case #"<<l<<": Bad magician!"<<endl;
	
	else
	cout<<"Case #"<<l<<": "<<num<<endl;

	}
	return 0;
	
}