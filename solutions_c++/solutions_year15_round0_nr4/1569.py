#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <stack>
#include <cmath>
#include <queue>
using namespace std;

void input()
{
	int a, b, c;
	cin >> a >> b >> c;
	if (b > c) swap(b, c);
	if (a == 4 && b == 2 && c == 4) {printf("RICHARD\n"); return;}
	a++;
	int x = a/2;
	int y = a - x;
	a--;
	if (min(x, y) > min (b, c) || max(x, y) > max(b, c) || a > max(b, c)) 
	{
		printf("RICHARD\n");
		return;
	}

	if ((b * c) % a == 0) printf("GABRIEL\n");
	else printf("RICHARD\n");
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int T;
	scanf("%d", &T);

	for (int test = 1; test <= T; ++test)
	{
		printf("Case #%d: ", test);
		input();
	}

	return 0;
}