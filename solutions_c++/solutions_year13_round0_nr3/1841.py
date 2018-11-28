#include <iostream>
#include <vector>
#include <fstream>
#include <cstdio>
#include <set>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <complex>
#include <string>
#include <cmath>
#include <deque>
#include <map>
#include <cstdlib>
#include <locale>
#include <limits>
#include <complex>
#include <sstream>
#include <utility>
//#include <list>

#define pb push_back
#define Size(x) ((int)(x.size()))
//#define X real()
//#define Y imag()

using namespace std;

typedef pair <int, int> pii;
//typedef long long int lint;
typedef unsigned long long lint;
typedef vector <lint> vi;

const int MAX = 1e3;
//const lint MAX = 1e14;

vector <int> decomp(lint n)
{
	vector <int> res;
	while (n > 0)
	{
		res.pb(n % 10);
		n /= 10;
	}
	return res;
}

bool isPal(lint n)
{
	vector <int> x = decomp(n);
	for (int i = 0; i < Size(x); i++)
		if (x[i] != x[Size(x) - i - 1])
			return false;
	return true;
}

//vi pal;
vector <int> temp;
set <lint> pal;

void makepal()
{
	lint res1 = 0, res2 = 0;
	for (int i = 0; i < Size(temp); i++)
	{
		res1 *= 10;
		res1 += temp[i];
	}
	res2 = res1;
	for (int i = Size(temp) - 1; i >= 0; i--) // 123321
	{
		res1 *= 10;
		res1 += temp[i];
		if (i < Size(temp) - 1)
		{
			res2 *= 10;
			res2 += temp[i];
		}
	}
	pal.insert(res1);
	pal.insert(res2);
}

void make(int pos = 0)
{
	if (pos == 4)
		return;
	for (int i = 0; i < 10; i++)
	{
		if (pos > 0 || i > 0)
		{
			temp.pb(i);
			makepal();
			make(pos + 1);
			temp.pop_back();
		}
	}
}

/*bool isok(lint n)
{
	double t = n;
	double r1 = sqrt(t);
	double r2 = floor(sqrt(t));
	return (r1 == r2 && binary_search(pal.begin(), pal.end(), (int) r1));
}*/

int main()
{
	ios_base::sync_with_stdio(false);
	stdin = freopen("C.in", "r", stdin);
	stdout = freopen("C.out", "w", stdout);
	make();
	set <lint>::iterator it;
	vector <lint> res;
	for (it = pal.begin(); it != pal.end(); it++)
	{
		lint t = *it;
		t *= t;
		if (isPal(t))
			res.pb(t);
	}
	int T;
	cin >> T;
	for (int q = 0; q < T; q++)
	{
		cout << "Case #" << q + 1 << ": ";
		lint a, b;
		cin >> a >> b;
		lint ans = 0;
		for (int i = 0; i < Size(res); i++)
		{
			if (a <= res[i] && res[i] <= b)
				ans ++;
		}
		cout << ans << endl;
	}
	return 0;
}
