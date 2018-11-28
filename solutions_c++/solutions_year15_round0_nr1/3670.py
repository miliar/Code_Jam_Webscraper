#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n;
string input;
int result;

void read()
{
	cin>>n;
	cin>>input;
}

void solve()
{
	int cur;
	result=cur=0;
	for(int i=0; i<=n; i++)
	{
		if(cur<i)
		{
			result+=i-cur;
			cur=i;
		}
		cur+=input[i]-'0';
	}
}

void answer(int id)
{
	cout<<"Case #"<<id<<": "<<result<<"\n";
}

int main()
{
	int t; cin>>t;
	for(int i=1; i<=t; i++)
	{
		read();
		solve();
		answer(i);
	}
	return 0;
}
