#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <list>
#include <stack>
#include <functional>

using namespace std;


int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
  
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		int n, x;
		cin >> n >> x;
		multiset< int, std::greater<int> > S;

		for(int i = 0; i < n; ++i)
		{
			int a;
			cin >> a;
			S.insert(a);
		}

		int ans = 0;

		while(!S.empty())
		{
			int cur = *S.begin();
			S.erase(S.begin());
			int need = x - cur;
			auto it = S.lower_bound(need);
			if(it != S.end())
				S.erase(it);
			++ans;
		}

		cout << "Case #" << t << ": " << ans << endl;
	}

    return 0;
}