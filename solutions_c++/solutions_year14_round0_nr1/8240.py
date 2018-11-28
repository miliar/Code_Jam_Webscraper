#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int a[4],b[4];
int check()
{
	int ans=0,flag=0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(a[i]==b[j])
			{
				if(flag==0)
				{
					flag=1;
					ans=a[i];
				}
				else
					return -1;
			}
	if(flag==0)
		return -2;
	else
		return ans;
}
int main()
{
	int t;
	ifstream inp("input.in");
	ofstream out("answer.txt");
	inp>>t;
	for(int k=1;k<=t;k++)
	{
		int r1,r2,x;
		inp>>r1;
		for(int i=1;i<=4;i++)
			for(int j=0;j<4;j++)
			{
				inp>>x;
				if(r1==i)
					a[j]=x;
			}
		inp>>r2;
		for(int i=1;i<=4;i++)
			for(int j=0;j<4;j++)
			{
				inp>>x;
				if(r2==i)
					b[j]=x;
			}
		x=check();
		out<<"Case #"<<k<<": ";
		if(x==-2)
			out<<"Volunteer cheated!\n";
		else if(x==-1)
			out<<"Bad magician!\n";
		else
			out<<x<<endl;
	}
	return 0;
}