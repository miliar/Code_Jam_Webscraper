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

bool dig[10] = { false };

bool check(ll k)
{
	while (k > 0)
	{
		dig[k % 10] = true;
		k /= 10;
	}
	fore(i, 0, 10)
	{
		if (!dig[i])
			return true;
	}
	return false;
}

int main()
{
	int t;
	cin >> t;
	for (int h = 0; h < t; h++)
	{
		memset(dig, false, sizeof dig);
		ll a, k;
		cin >> a;
		cout << "Case #" << h + 1 << ": ";
		bool flag = false;
		fore(i, 1, 100)
		{
			k = a * i;
			if (!check(k)) 
			{
				cout << k << endl;
				flag = true;
				break;
			}
		}
		if (!flag)
			cout << "INSOMNIA" << endl;
	}
}