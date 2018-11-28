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

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int c = 0; c < t; ++c)
	{
		set <int> s, s1;
		int x;
		cin >> x;
		int a[4][4];
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> a[i][j];
		for (int i = 0; i < 4; ++i)
			s.insert(a[x - 1][i]);
		cin >> x;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> a[i][j];
		for (int i = 0; i < 4; ++i)
		{
			if (s.count(a[x - 1][i]))
				s1.insert(a[x - 1][i]);
		}
		cout << "Case #" << c + 1 << ": ";
		if (s1.size() == 1)
			cout << *s1.begin() << endl;
		else if (s1.empty())
			cout << "Volunteer cheated!\n";
		else
			cout << "Bad magician!\n";
	}
}