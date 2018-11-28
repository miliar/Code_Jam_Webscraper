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
#include <iomanip>  

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


int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	forn(casenum,t)
	{
		double c,f,x;
		cin >> c >> f >> x;
		double a = 0.0f;
		double b = 0.0f;
		double step = 2.0f;
		double sum = 0.0f;
		do
		{
			a = sum + x / step;
			double new_step = step + f;
			b = sum + c / step + x / new_step;
			sum += c / step;
			step = new_step;
		}
		while (a >= b);
			
		cout << setprecision(9);
		cout << "Case #" << casenum+1  << ": " << a << endl;
	}
	

	return 0;
}