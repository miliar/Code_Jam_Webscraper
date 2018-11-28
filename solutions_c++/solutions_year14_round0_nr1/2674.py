#include<iostream>
#include <cmath>
#include <algorithm>
#include<vector>
#include <string>
#include <set>
#include <sstream>
#include<fstream>
using namespace std;


int main()
{
freopen("A-small-attempt2.in","r",stdin);
freopen("out234.out","w",stdout);
int  value,a,y,b,num,count;
	int t;
	cin>>t;
	for(int y=0;y<t;y++)
	{
		vector<int>arr;
		vector<int>brr;
		cin>>a;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>num;
				if(i==a-1)
				{
					arr.push_back(num);
				}
			}
		}
		cin>>b;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>num;
				if(i==b-1)
				{
					brr.push_back(num);
				}
			}
		}
		count=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr[i]==brr[j])
				{
					count++;
					value=arr[i];
				}
			}
		}
		if(count==0){cout<<"Case #"<<y+1<<": "<<"Volunteer cheated!"<<endl;}
		else if(count==1){cout<<"Case #"<<y+1<<": "<<value<<endl;}
		else {cout<<"Case #"<<y+1<<": "<<"Bad magician!"<<endl;}
	}
	return 0;
}
