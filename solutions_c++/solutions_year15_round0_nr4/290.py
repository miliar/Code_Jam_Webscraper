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

const string lose = "GABRIEL";
const string win = "RICHARD";

string solve()
{
	int X, R, C;
	scanf("%d%d%d", &X, &R, &C);
	if (X == 1) return lose;
	if (X == 2) return ((R * C) & 1) ? win : lose;
	if (X == 3) 
	{
		if (R != 3) swap(R, C);
		if (R != 3) return win;
		if (C == 2 || C == 3 || C == 4) return lose;
		else return win;
	}
	else
	{
		if ((R * C) % 4) return win;
		if (R > C) swap(R, C);
		if (R == 1 && C == 4) return win;
		if (R == 2 && C == 2) return win;
		if (R == 2 && C == 4) return win;
		if (R == 3 && C == 4) return lose;
		if (R == 4 && C == 4) return lose;
	}
}

int main()
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases) printf("Case #%d: %s\n", _, solve().c_str());
    return 0;
}


