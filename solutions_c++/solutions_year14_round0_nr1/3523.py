#include<stdio.h>
#include<conio.h>
#include<iostream>

using namespace std;

int main()
{
	int i,j,t,n,save,ctr,a,k,b;
	cin>>t;
	int arr[4][4],brr[4][4];
	for(i=0;i<t;i++)
	{
		int crr[17]={0};
		cin>>a;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>arr[j][k];
				if(j==a-1)
				{
					crr[arr[j][k]]=1;
				}
			}
		}
		cin>>b;
		ctr=0;
		save=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>brr[j][k];
				if(j==b-1)
				{
					if(crr[brr[j][k]]==1)
					{
						ctr++;
						save=brr[j][k];
					}
				}
			}
		}
		if(ctr==0)
		cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		if(ctr==1)
		cout<<"Case #"<<i+1<<": "<<save<<"\n";
		if(ctr>1)
		cout<<"Case #"<<i+1<<": Bad magician!\n";
	}
	getch();
	return 0;
}
