#include<iostream>
#include <cmath>
#include <algorithm>
#include<vector>
#include <string>
#include <set>
#include <sstream>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int main()
{
	READ("A-small-attempt2.in");
    WRITE("A-small-attempt2.out");
	int n;
	cin>>n;
	for(int l=0;l<n;l++)
	{
		int n1,n2,y;
		cin>>n1;
		vector<int>v1;
		vector<int>v2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>y;
				if(i==n1-1)
				{
					v1.push_back(y);
				}
			}
		}
		cin>>n2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>y;
				if(i==n2-1)
				{
					v2.push_back(y);
				}
			}
		}
		int x=0;
		int an;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(v1[i]==v2[j])
				{
					x++;
					an=v1[i];
				}
			}
		}
		if(x==0){cout<<"Case #"<<l+1<<": "<<"Volunteer cheated!"<<endl;}
		else if(x==1){cout<<"Case #"<<l+1<<": "<<an<<endl;}
		else {cout<<"Case #"<<l+1<<": "<<"Bad magician!"<<endl;}
	}
	return 0;
}