#include <cstdlib>   
#include <cctype>   
#include <cstring>   
#include <cstdio>   
#include <cmath>   
#include <algorithm>   
#include <vector>   
#include <string>   
#include <iostream>   
#include <sstream>   
#include <map>   
#include <set>   
#include <queue>   
#include <stack>   
#include <fstream>   
#include <numeric>   
#include <iomanip>   
#include <bitset>   
#include <list>   
#include <stdexcept>   
#include <functional>   
#include <utility>   
#include <ctime>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MEM(a,b) memset((a),(b),sizeof(a))
const LL INF = 1e17;
const int N = 2e3;
priority_queue<int> pq;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		string ans;
		int x, r, c;
		cin >> x >> r >> c;
		if (x <= 2)
		{
			if (r*c %x == 0) ans = "GABRIEL";
			else ans = "RICHARD";
		}
		if (x == 3)
		{
			if (r*c == 9 || r*c %6 == 0) ans = "GABRIEL";
			else ans = "RICHARD";
		}
		if (x == 4)
		{
			ans = "RICHARD";
			if (r*c == 12) ans = "GABRIEL";
			if (r*c == 16) ans = "GABRIEL";

		}

		printf("Case #%d: %s\n", ks++, ans.c_str());
	}
	return 0;
}


