#include<iostream>
#include<cstdlib>
#include<string.h>
#include<string>
#include<vector>
#include<math.h>
#include<ctype.h>

using namespace std;
int arr1[5][5],arr2[5][5];
int r1,r2,val1[4],val2[4],key;
void save()
{
	for(int i=0;i<4;i++)
	{
		val1[i]=arr1[r1][i+1];
//		cout<<val1[i]<<endl;
	}	
	for(int i=0;i<4;i++)
	{
		val2[i]=arr2[r2][i+1];
	}	
}
int check()
{
	int flag=0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(val1[i]==val2[j])
			{
				flag++;
				key=val1[i];
			}
		}
	}
	return flag;
}
int main()
{
	int T;
	cin>>T;
	for(int p=0;p<T;p++)
	{
		cin>>r1;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			cin>>arr1[i][j];
		}
		cin>>r2;
		for(int i=1;i<5;i++)
		
		{
			for(int j=1;j<5;j++)
			cin>>arr2[i][j];
		}
/*			for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			cout<<arr1[i][j]<<" ";
			cout<<endl;
		}
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			cout<<arr2[i][j]<<" ";
			cout<<endl;
		}*/
		save();
		int k=check();
		cout<<"Case #"<<p+1<<": ";
		if(k==0)
		cout<<"Volunteer cheated!"<<endl;
		else if(k==1)
		cout<<key<<endl;
		else
		cout<<"Bad magician!"<<endl;
	}
	return 0;
}
