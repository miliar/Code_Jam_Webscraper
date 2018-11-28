#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> vi;
typedef vector<string> vs;
const int INF = 0x7fffffff;

int Solution()
{
	int a, b;
	set<int> row1, row2;
	cin >> a;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
		{
			int x;
			cin >> x;
			if(i + 1 == a)
				row1.insert(x);
		}
	cin >> b;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
		{
			int x;
			cin >> x;
			if(i + 1 == b)
				row2.insert(x);
		}

	int cnt = 0, ans = 0;
	for(set<int> :: iterator it = row1.begin(); it != row1.end(); ++it)
	{
		int x = *it;
		if(row2.find(x) != row2.end()) 
		{
			cnt++;
			ans = x;
		}
	}
	switch(cnt) 
	{
		case 0:
			cout << "Volunteer cheated!";
			break;
		case 1:
			cout << ans;
			break;
		default:
			cout << "Bad magician!";
	}
	return 0;
}

#define debug 1

int main()
{
#ifdef debug
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
#endif
	int n;
	cin >> n;
	getchar();
	for(int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		Solution();
		printf("\n");
	}
	return 0;
}
