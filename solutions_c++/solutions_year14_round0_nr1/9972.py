#include <iostream>
#include <cassert>
using namespace std;
int common(int a[4][4],int b[4][4],int c1,int c2,int &val)
{
	int count=0;
	for(int j=0;j<4;j++)
	{
		for(int k=0;k<4;k++)
		{
			if(a[j][c1-1]==b[k][c2-1])
			{
				val=a[j][c1-1];
				count++;
			}
		}
	}
	return count;
}
int main()
{
	int testcase=0;
	cin >> testcase;
	int column1,column2;
	int pseud=0;
	int val;
	int mag1[4][4],mag2[4][4];
	for(int i=0;i<testcase;i++)
	{
		cin>>column1;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>mag1[k][j];
			}
		}
		cin>>column2;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>mag2[k][j];
			}
		}
		pseud=common(mag1,mag2,column1,column2,val);
		if(pseud==1)
		{
			cout<<"Case #"<<i+1<<": "<<val<<endl;
		}
		else if(pseud==0)
		{
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}
	}
}
