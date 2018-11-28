#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <fstream>
#include <string>
#include <cmath>
#include <queue>
 
using namespace std;

int solve(vector<double>& a, vector<double>& b)
{
	int indx = 0;
	for(int i = 0 ; i < a.size(); i++)
	{
		if(a[i] > b[indx])
			indx++;
	}
	return indx;
}
 
int main()
{
	//freopen("INPUT.TXT","r",stdin); freopen("OUTPUT.TXT","w",stdout);
	int t, n;
	cin>>t;
	for(int i = 1; i <= t; i++)
	{
		cin>>n;
		vector<double> a(n), b(n);
		for(int j = 0; j <n; j++)
			cin>>a[j];
		for(int j = 0; j <n; j++)
			cin>>b[j];
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		cout<<"Case #"<<i<<": "<<solve(a,b)<<" "<<n - solve(b, a)<<endl;
	}
	
}