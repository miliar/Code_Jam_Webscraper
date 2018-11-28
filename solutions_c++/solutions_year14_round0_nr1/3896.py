#include<iostream>
#include <stdio.h>
using namespace std;
int arr1[4][4];
int arr2[4][4];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int p,i,j,t,ans1,ans2,count,num;
	cin>>t;
	for(p=1;p<=t;p++)
	{
		count=0;
		cin>>ans1;
		for(i=0;i<=3;i++)
		{
			for(j=0;j<=3;j++)
				cin>>arr1[i][j];
		}
		cin>>ans2;
		for(i=0;i<=3;i++)
		{
			for(j=0;j<=3;j++)
				cin>>arr2[i][j];
		}
		--ans1;
		--ans2;
		for(i=0;i<=3;i++)
		{
			for(j=0;j<=3;j++)
			{
				if(arr1[ans1][i]==arr2[ans2][j])
				{
					count++;
					num=arr1[ans1][i];
					break;
				}
			}
		}
		if(count==1)
			cout<<"Case #"<<p<<": "<<num<<endl;
		else if(count>1)
			cout<<"Case #"<<p<<": "<<"Bad magician!"<<endl;
		else
		 	cout<<"Case #"<<p<<": "<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
