/*
    Author: Zhouxing Shi
    Created on Apr11, 2014
*/
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define drep(i, a, b) for (int i = (a); i >= (b); --i)
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define pb(x) push_back(x)
#define mp(x, y) (make_pair(x, y))
#define clr(x) memset(x, 0, sizeof(x))
#define xx first
#define yy second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
const int inf = ~0U >> 1;
const ll INF = ~0ULL >> 1;

//***************************

char s[20000000];
int L;
int a[20000000], pre[20000000];

int translate(char c)
{
	if (c == 'i') return 2;
	if (c == 'j') return 3;
	if (c == 'k') return 4;
}

const int MUL[5][5] = 
{ {0, 0, 0, 0, 0},
  {0, 1, 2, 3, 4},
  {0, 2, -1, 4, -3},
  {0, 3, -4, -1, 2},
  {0, 4, 3, -2, -1} };

int mul(int x, int y)
{
	int flag = 1;
	if (x < 0) flag *= -1;
	if (y < 0) flag *= -1;
	x = abs(x); y = abs(y);
	return MUL[x][y] * flag;
}

int divi(int x, int y)
{
	int flag = 1;
	if (x < 0) flag *= -1;
	if (y < 0) flag *= -1;
	x = abs(x); y = abs(y);
	rep(k, 1, 4) 
		if (MUL[k][y] == x) return k * flag;
		else if (MUL[k][y] == -x) return k * flag * -1;
}

map<int, int> hi, hj;

ll X;

string solve()
{
	hi.clear(); hj.clear();
	scanf("%d%lld", &L, &X);
	
	if (X > 20) X -= (X - 20) / 4 * 4;
	scanf("%s", s + 1);
	rep(i, 1, L * X) s[i + L] = s[i];
	pre[0] = 1;
	rep(i, 1, L * X)
	{
		a[i] = translate(s[i]);
		pre[i] = mul(pre[i - 1], a[i]);
		
		if (pre[i] == 2) 
			hi[2] = i;
		
		int last = divi(pre[i], 3);
		if (hi[last]) 
			hj[pre[i]] = i;
		
		last = divi(pre[i], 4);
		if (hj[last] && i == L * X) return "YES";
	}
	
	return "NO";
}

int main()
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases) printf("Case #%d: %s\n", _, solve().c_str());
    return 0;
}


