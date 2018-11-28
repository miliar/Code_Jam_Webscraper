#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
using namespace std;

struct coin
{
	int p;
	int w;
};

bool comp(coin c1, coin c2)
{
	return c1.w < c2.w;
}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    cin>>t;
	for (int j = 0; j < t; ++j)
	{
		int n;
		string s;
		cin>>n>>s;
		int res = 0;
		int sum = s[0] - '0';
		for (int i = 1; i <= n; ++i)
		{
			int c = s[i] - '0';
			if (c == 0) continue;
			if (sum < i)
			{
				int d = i - sum;
				res += d;
				sum += d;
			}
			sum += c;
		}
		cout<<"Case #"<<j + 1<<": "<<res<<endl;		
	}
    return 0;
}