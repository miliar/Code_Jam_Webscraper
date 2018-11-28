#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;


typedef long long ll;
ll cnt = 0;
double eps = 1e-9;

ll gcd(ll a, ll b)
{ 
	return b?gcd(b,a%b):a;
}

bool check(double a, double b){
	return !(fabs(a - b) < eps);
}
set<int> s;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	vector<double> arr;
	for(int i=0; i<50; ++i)
	{
		ll tmp = (1LL<<i);
		s.insert(tmp);
		arr.push_back(tmp);
	}
	ll test;
	cin>>test;
	for(ll testcase = 0; testcase<test; ++testcase)
	{

		ll x,y;
		char c;
		cin>>x>>c>>y;
		int gc = gcd(x,y);
		x/=gc;
		y/=gc;
		double cur = (double)y/(double)x;
		if(s.find(y) == s.end())
		{
			cout<<"Case #"<<testcase+1<<": impossible\n";
			continue;
		}

		

		cout<<"Case #"<<(testcase+1)<<": ";
		for(int i=0; i<arr.size(); i++){
			if( arr[i] - cur > eps || fabs(arr[i] - cur) < eps ){
				cout<<i;
				break;
			}
		}
		cout<<"\n";
	}
	return 0;
}