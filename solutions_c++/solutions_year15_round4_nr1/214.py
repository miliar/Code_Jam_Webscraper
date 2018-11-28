#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cctype>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <int, pii> piii;
typedef long double ld;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const int int_inf = 0x3f3f3f3f;
const ll ll_inf = 0x3f3f3f3f3f3f3f3fll;
const double pi = acos(-1.0);
const double eps = 1e-8;

	template <class T>
inline T abs(const T x)
{
	return x < 0 ? -x : x;
}

	template <class T>
inline void get_min(T &a, T b)
{
	if (a > b)
		a = b;
}

	template <class T>
inline void get_max(T &a, T b)
{
	if (a < b)
		a = b;
}

	template <class T>
inline void fix(T &a, T mo)
{
	while (a >= mo)
		a -= mo;
	while (a < 0)
		a += mo;
}

	template <class T>
inline void inc(T &a, T b, T mo)
{
	a += b;
	fix(a, mo);
}

	template <class T>
inline void dec(T &a, T b, T mo)
{
	a -= b;
	fix(a, mo);
}

	template <class T>
inline T sqr(T x)
{
	return x * x;
}

	template <class T>
inline int sgn(T x)
{
	if (x > eps)
		return 1;
	if (x < -eps)
		return -1;
	return 0;
}

	template <class T>
inline void read(T &x)
{
	x = 0;
	char ch;
	bool flag = 0;
	while (ch = getchar(), !isdigit(ch) && ch != '-');
	if (ch == '-')
		flag = 1;
	else
		x = ch - '0';
	while (ch = getchar(), isdigit(ch))
		x = (x << 3) + x + x + ch - '0';
	if (flag)
		x = -x;
}
const int N = 200;

char s[N];

int r, c;
int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int in[N][N];

int iss(char ch){
	if(ch == '.')return 5;
	if(ch == '^')return 0;
	if(ch == '>')return 1;
	if(ch == 'v')return 2;
	return 3;
}
int inn(int x, int y){
	if(x == r || y == c || x < 0 || y < 0) return 0;
	return 1;
}
int main()
{
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		scanf("%d%d", &r, &c);
		for(int i=0; i<r; ++i){
			scanf("%s",s);
			for(int j = 0; j<c; ++j){
				in[i][j] = iss(s[j]);
			}
		}
		int ok = 1;
		int ans = 0;
		for(int i=0; i<r; ++i){
			for(int j = 0; j < c; ++j){
				int now = in[i][j];
				if(now == 5)continue;
				int x, y;
				x = i + dir[now][0];
				y = j + dir[now][1];
				int same = 0, dif = 0;
				while(inn(x, y)){
					if(in[x][y] != 5){
						same = 1;
						break;
					}
					x = x + dir[now][0];
					y = y + dir[now][1];
				}
				for(int k = 0; k < 4; ++k){
					x = i + dir[k][0];
					y = j + dir[k][1];
					while(inn(x, y)){
						if(in[x][y] != 5){
							dif = 1;
							break;
						}
						x = x + dir[k][0];
						y = y + dir[k][1];
					}
				}
				if(same)continue;
				if(dif) {
					ans ++;
					continue;
				}
				ok = 0;
			}
		}
		if(ok) {
			printf("Case #%d: %d\n", cc, ans);
		}else {
			printf("Case #%d: IMPOSSIBLE\n", cc);
		}
	}
	return 0;
}

