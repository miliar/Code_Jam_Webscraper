#include <cstring>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <string>
using namespace std;
int Calc()
{
	int res = 0;
	int len;
	cin >> len;
	string s;
	cin >> s;
	int cnt = 0;
	for ( int i = 0; i < s.size(); i ++)
	{
		if ( s[i] != '0')
		{
			if ( cnt < i)
				res+= i - cnt, cnt = i;
			cnt += s[i] - '0';
		}
	}

	return res;
}
int main()
{
    freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin >> t;
	for(int k = 0 ; k < t; k ++)
	{
		cout << "Case #" << k + 1 << ": " << Calc() << endl;
	}
	return 0;
}