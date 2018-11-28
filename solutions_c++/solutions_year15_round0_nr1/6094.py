#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:133217728")
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef pair<int, int> PII;
typedef vector<int> VI;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(int i = (a) - 1; i >= (b); --i)
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define pi acos(-1.0)

const int MOD = 1000000007;
const int INF = 2000000007;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//freopen("teams.in", "r", stdin);
	//freopen("teams.out", "w", stdout);

	int t;
	cin >> t;
	FOR(test,0,t)
	{
		int n;
		string s;
		cin >> n >> s;
		
		int add = 0;
		int sum = 0;
		FOR(i, 0, n + 1)
		{
			if (sum < i)
			{
				add += i - sum;
				sum = i;
			}
			sum += s[i] - '0';
		}
		cout << "Case #" << test+1 << ": " << add << endl;
	}

	return 0;
}