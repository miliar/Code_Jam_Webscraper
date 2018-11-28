#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <string.h>
using namespace std;

#define pb push_back
#define rs resize
#define mp make_pair
#define inf 1e9
#define pi 3.1415926535897932384626433832795

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <vvi> vvvi;
typedef vector <vvvi> vvvvi;
typedef vector <bool> vb;
typedef vector <vb> vvb;
typedef vector <vvb> vvvb;
typedef vector <vvvb> vvvvb;
typedef long long ll;
typedef vector <ll> vl;
typedef vector <vl> vvl;
typedef vector <vvl> vvvl;
typedef vector <vvvl> vvvvl;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef vector <vii> vvii;
typedef pair <int, ll> il;
typedef vector <il> vil;
typedef vector <vil> vvil;
typedef pair <ll, int> li;
typedef vector <li> vli;
typedef vector <vli> vvli;
typedef set <int> si;
typedef set <li> sli;
typedef set <il> sil;
typedef vector <string> vs;
typedef vector <vs> vvs;
typedef vector <vvs> vvvs;
typedef map <string, int> msi;
typedef map <char, int> mci;
typedef long double ld;
typedef vector <ld> vd;
typedef vector <vd> vvd;

const double eps = 1e-7;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		double c, f, x;
		cin >> c >> f >> x;
		int k = 0;
		double t = 0;
		while (c / (2.0 + f * k) + x / (2 + (k + 1) * f) < x / (2 + k * f) - eps)
		{
			t += c / (2.0 + f * k);
			k++;
		}
		cout.precision(7);
		cout << fixed;
		cout << "Case #" << i + 1 << ": " << t + x / (2 + k * f) << endl;
	}
}