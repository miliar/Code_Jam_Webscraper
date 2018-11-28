#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <cstring>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
using namespace std;
 
typedef pair<int, int> pii;
typedef long long llong;
typedef pair<llong, llong> pll;
typedef unsigned long long ullong;
#define mp make_pair
#define sqr(x) ((x)*(x))
const double PI = 3.14159265359;
#define y1 Y1
#define y0 alalal1231

vector<int> vec[5][5];
pii pos[17];

void clear()
{
	for (int i = 1; i < 5; ++i)
		for (int j = 1; j < 5; ++j)
			vec[i][j].clear();
}

void answer(int a, int b)
{
	if (vec[a][b].empty())
		puts("Volunteer cheated!");
	else if (vec[a][b].size() != 1)
		puts("Bad magician!");
	else
		printf("%d\n", vec[a][b][0]);
}

int main()
{
#ifdef MYLOCAL
    freopen("input.txt","rt",stdin);
    freopen("output.txt", "wt", stdout);
    clock_t beginTime = clock();
#endif

	int t;
	scanf("%d", &t);
	for (int _i = 1; _i <= t; ++_i)
	{
		clear();
		int a, b, x;
		scanf("%d", &a);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &x), pos[x].first = i;
		scanf("%d", &b);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &x), pos[x].second = i;
		for (int i = 1; i <= 16; ++i)
			vec[pos[i].first][pos[i].second].push_back(i);
		printf("Case #%d: ", _i);
		answer(a, b);
	}

#ifdef MYLOCAL
    cout << endl << "time: " << double(clock() - beginTime) / CLOCKS_PER_SEC;
#endif
    return 0;
}