#include<iostream>
#include<cmath>
#include<map>
#include<string>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<set>
#include<iomanip>
#include<algorithm>
using namespace std;
typedef long double LD;
int main()
{
	//freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int test;
	cin >> test;
	for(int t = 1; t <= test; ++t)
	{
		LD c, f, x;
		LD cookie = 2.0;
		cin >> c >> f >> x;
		LD prev = x / cookie;
		LD next = 0.0;
		LD time = 0.0;
		LD intermediateTime = 0.0;
		int count = 0;
		while(prev > next)
		{
			++count;
			if(count > 1)		prev = next;
			time += c / cookie;
			cookie += f;
			intermediateTime = x / cookie;
			next = time + intermediateTime;
		}
		cout << fixed;
		cout << setprecision(7);
		cout << "Case #" << t << ": " << prev << endl;
	}
	return 0;
}