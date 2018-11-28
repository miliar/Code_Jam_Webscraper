#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstring>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <climits>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <sstream>
#include <map>
#include <ctime>
#include <cstdlib>
#include <list>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include<unordered_map>
#include <stdio.h>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#define IO               cin.tie(0);std::ios::sync_with_stdio(false)
using namespace std;


int  main()
{
	int t; cin >> t;
	for (int j = 1; j <= t;j++)
	{
		set<int> s;
		int x, n;
		int ans = 0;
		cin >> n;
		for (int i = 1; i <= 100000000; i++)
		{
			x = n*i;
			ans = x;
			while (x > 0)
			{
				s.insert(x % 10);
				x /= 10;
			}
			if (s.size() == 10)break;
		}
		if (s.size()!=10)
			cout << "Case #" << j << ": " << "INSOMNIA" << endl;
		else
		cout <<"Case #"<<j<<": " << ans<<endl;
	}
}