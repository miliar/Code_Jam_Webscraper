#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <numeric>
#include <ctime>

using namespace std;

#define pb push_back
#define sz(x) ((int) (x).size())
#define forn(i, n) for (int i = 0; i < (n); i++)
#define rforn(i, n) for (int i = (n) - 1; i >= 0; i--)
#define clr(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef long long ll;
typedef pair<ll,ll> pll;

bool isPalindrom(const string& s)
{
	int i = 0;
	int j = s.size() - 1;
	while(i < j)
	{
		if (s[i] != s[j])
			return false;
		i++;
		j--;
	}
	return true;
}

template <class T>
inline std::string to_string (const T& t)
{
	std::stringstream ss;
	ss << t;
	return ss.str();
}
ll MAX_SIZE = 100000000000000;
int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	vector<ll> fairPalindroms;
	for (ll i = 0; i*i <= MAX_SIZE; ++i)
	{
		if (isPalindrom(to_string(i)))
		{
			if (isPalindrom(to_string(i*i)))
				fairPalindroms.push_back(i*i);
		}
	}
	forn(casenum,T)
	{
		ll A, B;
		cin >> A;
		cin >> B;
		string str;
		stringstream ss;
		ll count = 0;
		for(int i = 0; i < fairPalindroms.size(); ++i)
		{
			if (fairPalindroms[i] >= A && fairPalindroms[i] <= B)
				count++;
		}
		cout << "Case #" << casenum + 1 << ": "<< count << endl;
	}

	return 0;
}