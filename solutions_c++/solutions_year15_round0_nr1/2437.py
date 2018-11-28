#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <set>
#include <list>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int s;
		cin >> s;
		int ans = 0, cur = 0;
		for(int i = 0; i <= s; i++)
		{
			char x;
			cin >> x;
			int k = x - '0';
			if(k != 0 && cur < i)
			{
				ans += i - cur;
				cur = i;
			}
			cur += k;
		}
		cout << "Case #" << t << ": " << ans << '\n';
	}
}