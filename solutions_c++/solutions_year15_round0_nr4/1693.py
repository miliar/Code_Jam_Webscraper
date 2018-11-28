#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define inf 1000000000
#define maxn 10

#define ll long long
#define pii pair<int, int>
#define pb push_back
#define sin scanint
#define bitcount(x) __builtin_popcount(x)
#define fill(s, p) memset(s, p, sizeof(s));

#ifdef ONLINE_JUDGE
#define gc getchar_unlocked
#endif

#ifndef ONLINE_JUDGE
#define gc getchar
//freopen("input.txt", "r", stdin)
//freopen("output.txt", "w", stdout)
#endif

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int sol[maxn][maxn][maxn];           //x, r, c

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("o2.txt", "w", stdout);
	fill(sol, 0);
	sol[2][1][1] = sol[3][1][1] = sol[4][1][1] = 1;
	sol[3][2][1] = sol[4][2][1] = 1;
	sol[3][2][2] = sol[4][2][2] = 1;
	sol[2][3][1] = sol[3][3][1] = sol[4][3][1] = 1;
	sol[4][3][2] = 1;
	sol[2][3][3] = sol[4][3][3] = 1;
	sol[3][4][1] = sol[4][4][1] = 1;
	sol[3][4][2] = sol[4][4][2] = 1;
	sol[3][4][4] = 1;
	int t, x, r, c, case_num=1;
	sin(t);
	while(t--){
		sin(x);
		sin(r);
		sin(c);
		if(c>r)
			swap(r, c);
		if(sol[x][r][c]==1)
			printf("Case #%d: RICHARD\n", case_num++);
		else
			printf("Case #%d: GABRIEL\n", case_num++);
	}
	return 0;
}