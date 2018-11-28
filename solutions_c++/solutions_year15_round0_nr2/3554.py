#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int D;
vector <int> P;
int result;

void read()
{
	cin>>D;
	P.resize(D);
	for(int i=0; i<D; i++)
	{
		cin>>P[i];
	}
}

int check(int maks)
{
	int res=0;
	for(int i=0; i<D; i++)
	{
		res+=(P[i]+maks-1)/maks-1;
	}
	return res+maks;
}

void solve()
{
	int d=0;
	for(int i=0; i<D; i++) d=max(d,P[i]);
	result=d;
	for(int i=1; i<d; i++) result=min(result,check(i));
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
