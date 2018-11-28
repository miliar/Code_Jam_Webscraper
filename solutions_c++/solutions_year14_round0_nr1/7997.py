#include <stdio.h>
#include <istream>
#include <sstream>
#include <iomanip>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <deque>
#include <queue>

typedef long long ll;

using namespace std;

void run()
{
	int c[4];
	int d[4];
	int a,b;
	string line;
	cin>>a; cin.ignore();
	for(int i=1;i<=4;i++)
	{
		getline(cin, line);
		if(i==a)
		{
			stringstream ss(line);
			for(int j=0;j<4;j++) ss>>c[j];
		}
	}

	cin>>b; cin.ignore();
	for(int i=1;i<=4;i++)
	{
		getline(cin, line);
		if(i==b)
		{
			stringstream ss(line);
			for(int j=0;j<4;j++) ss>>d[j];
		}
	}

	int result=-1;
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	{
		if(c[i]==d[j])
		{
			if(result!=-1)
			{
				cout<<"Bad magician!";
				return;
			}
			result=c[i];
		}
	}
	
	if(result==-1) 
	{
		cout<<"Volunteer cheated!";
		return;
	}
	cout<<result;

	return;
}





int main(int argc, char** argv)
{
	int T;
	cin>>T;

	for(int i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<": ";
		run();
		cout<<endl;
	}
}