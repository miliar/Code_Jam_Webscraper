#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int T,p,n,m,s,a[4][4],b[4][4];
	freopen("c2.in","r",stdin);
	freopen ("output3.txt","w",stdout);
	cin>>T;
	for(int k=1;k<=T;k++)
	{
		s=0;
		cin>>n;
		
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		cin>>a[i][j];
	}
	cin>>m;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		cin>>b[i][j];
	}
	for(int i=0;i<4;i++)
	{
	
	for(int j=0;j<4;j++)
	{
		if(a[n-1][i]==b[m-1][j])
		{   p=a[n-1][i];
			++s;
		}
	}
}
			if(s==1)
	cout<<"Case #"<<k<<": "<<p<<endl;
	else if(s>1)
	cout<<"Case #"<<k<<": Bad magician!"<<endl;
	else if(s==0)
	cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
	
	
	}
	 fclose (stdout);
	return 0;
}
