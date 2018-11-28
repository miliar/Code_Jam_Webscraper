#include<iostream>
#include<cstring>
#include<stack>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int a[20][20],b[20][20];
int row1,row2;
int num,ans;
void work()
{
	int i,j,k;
	cin>>row1;
	num=0;
	for (i=1;i<=4;i++)
		for (j=1;j<=4;j++)
			cin>>a[i][j];
	cin>>row2;
	for (i=1;i<=4;i++)
		for (j=1;j<=4;j++)
			cin>>b[i][j];
	for (k=1;k<=16;k++)
	{
		int t1,t2;
		for (i=1;i<=4;i++)
		{
			for (j=1;j<=4;j++)
			{
				if (a[i][j]==k) t1=i;
			}
		}
		for (i=1;i<=4;i++)
		{
			
			for (j=1;j<=4;j++)
			{
				if (b[i][j]==k) t2=i;
			}
		}
		if (t1==row1&&row2==t2){
			num++;
			ans=k;
		}
	}	
	if (num==0)
	{
		cout<<"Volunteer cheated!"<<endl;
		return;
	}
	if (num>1)
	{
		cout<<"Bad magician!"<<endl;
		return;
	}
	if (num==1)
	{
		cout<<ans<<endl;
	}
	return;
}
int main()
{
	int cas,T;
	freopen("a1.in","r",stdin);
	freopen("a1.out","w",stdout);
	cin>>T;
	cas=0;
	while (T--)
	{
		cas++;
		cout<<"Case #"<<cas<<": ";
		work();
	}
}
