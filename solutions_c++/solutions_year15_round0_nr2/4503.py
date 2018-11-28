#include <cstring>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <string>
#include <set>
using namespace std;

int Calc()
{
	vector<int> p;
	int n;
	cin >> n;
	for ( int i = 0; i < n; i ++)
	{
		int t;
		cin >> t;
		p.push_back(t);
	}
	int res = 10000000;
	for( int i = 1; i < 1000; i ++)
	{
		int cnt = 0;
		for( int j = 0; j < p.size(); j++)
			if (p[j] >=i)
			{
				int a =  (p[j] / i - 1);
				int b = (p[j] % i) != 0;
				cnt+= a + b ;
			}
		res = min(res, cnt + i);
	}
	return res;
}
int main()
{
    freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	
	int t;
	cin >> t;
	for(int k = 0 ; k < t; k ++)
	{
		cout << "Case #" << k + 1 << ": " << Calc() << endl;
	}
	return 0;
}