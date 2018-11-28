#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<map>
#include<queue>
#include<iterator>
using namespace std;
#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)
#define FOD(i,s,e) for(int i = (s); i >= (e); i--)
#define CLR(a) memset(a,0,sizeof(a))
#define ll long long
#include<ctime>
#include<cmath>
#include<vector>
#include<iostream>

int tc, tt, n, m, x, y, z, k, w, ans, A[30];
char S[30][30];
bool can;

void brute(int x, int y)
{
	bool ok = 0;
	if (x == n) { return; }
	else
	{
		FOR(i, 0, n) 
		{
			if (S[A[x]][i] == '1' && (y & (1 << i)) != 0) 
			{
				ok = 1;
				brute(x + 1, (y ^ (1 << i)));
			}
		}
		if (ok == 0) can = 0;
	}
}		

void check(int c)
{
	bool ok;
	FOR(i, 0, n) A[i] = i;
	
	can = 1;
	do { brute(0, 15); }while(next_permutation(A, A + n));
	
	if (can == 1) ans = min(ans, c);
}

void solve(int x, int y, int c)
{
	if (x == n) check(c);
	else if (y == n) solve(x + 1, 0, c);
	else
	{
		if (S[x][y] == '0') { S[x][y] = '1'; solve(x, y + 1, c + 1); S[x][y] = '0'; solve(x, y + 1, c); }
		else solve(x, y + 1, c);
	}
}
 

int main ()
{
	scanf("%d", &tc);
	while(tc--)
	{
		scanf("%d", &n);
		FOR(i, 0, n) scanf("%s", S[i]);
		
		ans = 1000;
		solve(0, 0, 0);
		
		printf("Case #%d: %d\n", ++tt, ans);
	}
	return 0;
}
