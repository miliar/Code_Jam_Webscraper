#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
#define ll long long int
using namespace std;
int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		ll c2 = 1;
		for(int j = 0; j < c - 1; j++) c2 *= k;
		printf("Case #%d:", i);
		ll v = 1;
		for(int j = 0; j < s; j++)
		{
			printf(" %I64d", v);
			v += c2;
		}
		printf("\n");
	}
	return 0;
}
