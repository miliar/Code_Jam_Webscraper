#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int t,n,count=0,ct=0,a[4][4],v;
	bool ch[20];
	cin>>t;
	for(int x=1;x<=t;x++)
	{
		memset(ch,0,sizeof(ch));
		while(count<2)
		{
		cin>>n;
		count++;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
			if(i==n-1&&count==1)
			{
				for(int k=0;k<4;k++)
					ch[a[i][k]]=true;
			}
			else if(i==n-1&&count==2)
			{
				for(int k=0;k<4;k++)
				{
					if(ch[a[i][k]]==true)
					{
						ct++;
						v=a[i][k];
					}
				}
			}
		}
		}
		if(ct==0)
			cout<<"Case #"<<x<<": Volunteer cheated!\n";
		else if(ct==1)
			cout<<"Case #"<<x<<": "<<v<<"\n";
		else
			cout<<"Case #"<<x<<": Bad magician!\n";
		v=0;ct=0;count=0;
	}
	return 0;
}
