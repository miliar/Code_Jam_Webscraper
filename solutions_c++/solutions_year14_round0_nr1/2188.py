#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("A-small-attempt2.in","r", stdin);
	freopen("A-small-attempt0.out","w", stdout);
	int T;
	cin>>T;
	int temp;
	int d1[17], d2[17];
	int a, b;
	for(int i=0; i<T; i++)
	{
		for(int j=1; j<17; j++)
		{
			d1[j]=0;
			d2[j]=0;
		}
		cin>>a;
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				cin>>temp;
				if(j+1==a)
				 d1[temp]++;
			}
			
		}
		cin>>b;
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				cin>>temp;
				if(j+1==b)
				 d2[temp]++;
			}
			
		}
		int sum=0;
		int ind;
		for(int j=1; j<17; j++)
		{
			if(d1[j]>0&&d1[j]==d2[j])
			{
				sum++;
				ind=j;
			}
		}
		if(sum==1)
		{
			cout<<"Case #"<<i+1<<": "<<ind<<endl;
		}
		if(sum==0)
		{
			cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		}
		if(sum>1)
		{
			cout<<"Case #"<<i+1<<": Bad magician!\n";
		}
	}
	//system("pause");
	return 0;
}