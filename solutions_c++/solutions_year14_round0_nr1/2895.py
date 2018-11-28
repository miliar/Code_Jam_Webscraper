#include<iostream>
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream cin;
  ofstream cout;
  cin.open ("A-small-attempt1.in");
  cout.open("output.txt");
	int t,i,j,k,x,y,count,p;
	int a[4][4],b[4][4];
	cin>>t;
	for(i=1;i<=t;i++)
	{
		count=0;
		cin>>x;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>a[j][k];
			}
		}
		cin>>y;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>b[j][k];
			}
		}
		x=x-1;
		y=y-1;
		for(j=0;j<4;j++)
		{
            for(k=0;k<4;k++)
            {
            	if(a[x][j]==b[y][k])
            	{
            		count++;
            		p=j;
            	}
            }
		}
		if(count<1)
		{
			cout<<"Case #"<<i<<":"<<" "<<"Volunteer cheated!"<<endl;
		}
		else if(count==1)
		{
			cout<<"Case #"<<i<<":"<<" "<<a[x][p]<<endl;
		}
		else if(count>1)
		{
			cout<<"Case #"<<i<<":"<<" "<<"Bad magician!"<<endl;
		}
	}
}
