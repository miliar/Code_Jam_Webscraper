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

//typedef __int64 ll;
//typedef unsigned __int64 ull;
typedef long long ll;
typedef unsigned long long ull;


template<typename T>
inline T ABS(T a) { return a > 0 ? a : -a; }
template<typename T>
inline T MIN(T a, T b) { return a < b ? a : b; }
template<typename T>
inline T MAX(T a, T b) { return a > b ? a : b; }
template<typename T>
inline T CHKMIN(T &a, T b) { if (a > b) a = b; return a; }
template<typename T>
inline T CHKMAX(T &a, T b) { if (a < b) a = b; return a; }
template<typename T>
inline void SWAP(T &a, T &b) { static T c; c = a; a = b; b = c; }

void Prime(int N, int *a, int *p, int &num) {
	int i, j;
	memset(a, 0, N * sizeof(a[0]));
	num = 0;
	for (i = 2; i < N; ++i) {
		if (!a[i]) a[i] = p[num++] = i;
		for (j = 0; j < num && i * p[j] < N; ++j) {
			a[i * p[j]] = p[j];
			if (!(i % p[j])) break;
		}
	}
}
int main() {
	FILE *stream;
	freopen_s(&stream, "D-small-attempt2.in", "r", stdin);
	freopen_s(&stream, "D-small-attempt2.out", "w", stdout);
	int t, x, r, c, ans = 0;
	string s;
	cin >> t;
	for (int m_case = 0; m_case < t; m_case++)
	{
		cin >> x >> r >> c;
		if (x == 1)
		{
			s = "GABRIEL";
		}
		else if (x == 2)
		{
			if ((r * c) % 2 == 0)
			{
				s = "GABRIEL";
			}
			else
			{
				s = "RICHARD";
			}
		}
		else if (x == 3)
		{
			if (r * c == 6 || r * c == 12 || r * c == 9)
			{
				s = "GABRIEL";
			}
			else
			{
				s = "RICHARD";
			}
		}
		else if (x == 4)
		{
			if (r * c == 16 || r * c == 12)
			{
				s = "GABRIEL";
			}
			else
			{
				s = "RICHARD";
			}
		}
		cout << "Case #" << m_case + 1 << ": " << s << endl;
	}
	return 0;
}