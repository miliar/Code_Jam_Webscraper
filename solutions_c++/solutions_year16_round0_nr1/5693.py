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

int main()
{
	std::ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	string root = "C:/Users/edu97250/Desktop/codejam/";

	ifstream cin(root + "in.txt");
	ofstream cout(root + "out.txt");

	int t;
	cin >> t;

	range(test, 0, t)
	{
		ull n;
		cin >> n;
		cout << "Case #" << test + 1 << ": ";
		if (n == 0)
		{
			cout << "INSOMNIA" << endl;
		}
		else
		{
			vb seen(10, false);
			int left = 10;
			ull cur = 1;
			while (left > 0)
			{
				string s = ToString(cur * n);
				for (char c : s)
					if (!seen[c - '0'])
						seen[c - '0'] = true, --left;
				++cur;
			}
			cout << n * (cur - 1) << endl;
		}
	}

	system("pause");
	return 0;
}