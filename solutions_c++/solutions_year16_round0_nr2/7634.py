#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <climits>
#include <cmath>
#include <sstream>
#include <map>
#include <list>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <string>
#include <cstdlib>
#include <stack>
#include <ctime>
#include <fstream>
#include <cstdio>
#include <cstring>

#define L(a) (int)((a).size())
#define sqr(x) ((x) * 1ll * (x))
#define vi vector<int>
#define mp make_pair
#define pub push_back
#define pob pop_back
#define ii pair<int, int>
#define vii vector <ii>
#define all(s) (s).begin(),(s).end()
#define fore(i, l ,r) for(int i = (int)l; i < (int)r; i++)

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const ld EPS = 1e-9;
const ld PI = acos(-1);
const int MOD = (int)1e9 + 7;
const int INF32 = (int)1e9;
const int INF64 = (ll)1e19;

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int h = 0; h < t; h++)
	{
		string s;
		cin >> s;
		int cnt = 0;
		for (int i = L(s) - 1; i >= 0; i--)
		{
			if ((s[i] == '-' && (cnt % 2) == 0) || (s[i] == '+' && (cnt % 2) == 1))
			{
				cnt++;
			}
		}
		cout << "Case #" << h + 1 << ": " << cnt << endl;
	}
}