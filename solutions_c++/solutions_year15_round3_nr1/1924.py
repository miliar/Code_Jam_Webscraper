#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iterator>
#define REP(i,a,n) for(int i = (a); i < (int)(n); ++i)
#define foreach(itr,c) for(decltype((c).begin()) itr=(c).begin(); itr != (c).end(); itr++)
#define mp(a,b) make_pair(a,b)

using namespace std;

int a[21][21];
int main() {
	FILE *stream;
	//freopen_s(&stream, "A-small-attempt2.in", "r", stdin);
	//freopen_s(&stream, "A-small-attempt2.out", "w", stdout);
	int t, n, ans, r, c, w;
	char s[1008];
	cin >> t;
	a[1][1] = 1;
	for (int i = 1; i <= 20; i++)
	{
		a[i][1] = i;
		a[i][i] = 1;
		for (int j = 2; j <= i; j++)
		{
			a[i][j] = a[i-j][j];
		}
	}
	for (int m_case = 0; m_case < t; m_case++)
	{
		cin >> r >> c >> w;
		int tmp1 = c / w - 1;
		int tmp2 = (w + c % w) > w ? w + 1 : w;
		cout << "Case #" << m_case + 1 << ": " << r *  (tmp1 + tmp2) << endl;
	}
	return 0;
}