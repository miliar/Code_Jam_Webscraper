// Catalin Craciun
//  B
//   Codejam
#include <iostream>
#include <cmath>
#include <bitset>
#include <iomanip>
#include <fstream>
#include <string>
#include <cstring>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

int t;
int a, b, k;

void solve()
{
	int rez=0;
	
	for (int i=0;i<a;i++)
	{
		for (int j=0;j<b;j++)
			if ((i & j) < k)
				rez++;
	}
	
	cout<<rez;
}

int main()
{
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>a>>b>>k;
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<'\n';
	}
	
	return 0;
}
