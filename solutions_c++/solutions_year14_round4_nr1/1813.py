#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <list>
#include <vector>
#include <cctype>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<string> vs;

#define SIZE(x) (int)(x).size()
#define REP(i, n) for(int i = 0; i < n; ++i)
#define FOR(i, a, b) for(auto i = (a); i <= (b); ++i)
#define FORR(i, a, b) for (auto i = (a); i >= (b); --i)
#define FOREACH (i, c) for(auto i = (c).begin(); i != (c).end(); ++i)
#define FORREACH (i, c) for(auto i = (c).rbegin(); i != (c).rend(); ++i)
#define ALL(c) (c).begin(), (c).end()

const int inf = 100000001;
const ll INF = 1000000000000000001;
const double EPS = 10e-9;

ostringstream out;
//------------------------------

int files[10006];

struct Poss
{
	int number1;
	int number2;
	ll sum;
};

Poss pfiles[1000007];
bool used[10005];

bool cmp(Poss a, Poss b)
{
	return (a.sum > b.sum);
}

int all_used(int n)
{
	int counter = 0;
	REP(i, n)
		if (used[i] == false)
			counter++;
	return counter;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	REP(h, t)
	{
		ll n, cap;
		cin >> n >> cap;

		
		REP(i, n)
		{
			cin >> files[i];
			used[i] = false;
		}
		sort(files, files + n);
		int k = 0;
		REP(i, n)
		{
			FOR(j, i + 1, n - 1)
			{
				if (files[i] + files[j] <= cap)
				{
					pfiles[k].number1 = i;
					pfiles[k].number2 = j;
					pfiles[k].sum = files[i] + files[j];
					k++;
				}
			}
		}

		sort(pfiles, pfiles + k, cmp);
		int j = 0;
		int c = 0;


		while (all_used(n) > 0)
		{
			if (j == k)
			{
				c += all_used(n);
				break;
			}
			if (used[pfiles[j].number1] == false && used[pfiles[j].number2] == false)
			{
				used[pfiles[j].number1] = true;
				used[pfiles[j].number2] = true;
				c++;
			}
			j++;
			
		}
		out << "Case #" << h + 1 << ": " << c << endl;
	}
	cout << out.str();
	return 0;
}