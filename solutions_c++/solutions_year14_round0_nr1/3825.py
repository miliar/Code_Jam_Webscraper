#include<iostream>
#include <stdio.h>

using namespace std;
int a[4][4];
int b[4][4];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,t,l1,l2,count,k,m;
	cin>>t;
	for(m=1;m<=t;m++)
	{
		count=0;
		cin>>l1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>l2;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[l1-1][i]==b[l2-1][j])
				{
					k=a[l1-1][i];
					count++;
				}
			}
		}
		if(count==1)
		cout<<"Case #"<<m<<": "<<k<<endl;
		if(count>1)
		cout<<"Case #"<<m<<":"<<" Bad magician!"<<endl;
		else if(count==0)
		cout<<"Case #"<<m<<":"<<" Volunteer cheated!"<<endl;
		
		
		
		
		
		
	}
	return 0;
}


