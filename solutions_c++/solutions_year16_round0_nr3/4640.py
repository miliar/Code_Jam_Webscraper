#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>
#include <functional>
#include <unordered_map>
#include <stack>
#include <set>
#include <bitset>
#include <sstream>
#include <list>
#include <forward_list>
#include <numeric>
#include <deque>
#include <fstream>
#include <bitset>
using namespace std;

#define range(x,s,e) for(int x=s;x<e;++x)
#define rerange(x,s,e) for(int x=e-1;x>=0;--x)
#define all(v) v.begin(), v.end()
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector<bool> vb;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<long, long> pll;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef unsigned long long ull;
typedef long long ll;

const double pi = 3.14159265358979323846;
const int INF32 = (int)1e9;
const ll INF64 = (ll)1e17;

#define vectorMax(v) (max_element(all(v)) - v.begin());

template<typename T>
std::string ToString(T t)
{
	std::stringstream s;
	s << t;
	return s.str();
}

int n, j;

ll val(int c, ll b)
{
	ll ret = 0;
	ll v = 1;
	range(i, 0, n)
	{
		if (c & (1 << i))
			ret += v;
		v *= b;
	}
	return ret;
}

ll findDiv(ull a)
{
	int top = (int)sqrt(a) + 1;
	range(i, 2, top)
	{
		if (a % i == 0)
			return i;
	}
	return -1;
}

int main()
{
	std::ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	string root = "C:/Users/edu97250/Desktop/codejam/";
	ofstream cout(root + "out.txt");

	cin >> n >> j;

	cout << "Case #1:" << endl;

	unsigned int cur = (1 << (n - 1)) + 1;
	//for (int i = 0; i < (n - 2); ++i, cur += 2)
	while (j > 0)
	{
		vector<ll> divs;
		range(b, 2, 10 + 1)
		{
			ll div = findDiv(val(cur, b));
			if (div != -1)
				divs.push_back(div);
			else
				break;
		}
		if (divs.size() == 9)
		{
			--j;
			rerange(i, 0, n)
				cout << ((cur & (1 << i)) ? '1' : '0');
			range(i, 0, 9)
				cout << " " << divs[i];
			cout << endl;
		}

		cur += 2;
	}



	system("pause");
	return 0;
}