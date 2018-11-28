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

int n, m, x, y, z, k, w;
int tc, tt;
int a, b, c;
int A[5005], B[5005], C[5005], ANS[5005];
bool ok;

void solve(int t, int x, int l, int r)
{
	if (l == r) 
	{
		
		 if (t == 0) A[l] = x; else if (t == 1) B[l] = x; else if (t == 2) C[l] = x;
	}
	else
	{
		int mid = (l + r) / 2;
		if (x == 0) { solve(t, 0, l, mid); solve(t, 2, mid + 1, r); }
		else if (x == 1) { solve(t, 1, l, mid); solve(t, 0, mid + 1, r); }
		else if (x == 2) { solve(t, 1, l, mid); solve(t, 2, mid + 1, r); }
	}
}

void change(int *A)
{
	FOE(i, 1, m) if (A[i] == 0) A[i] = 1; else if (A[i] == 1) A[i] = 0;
	
//	FOE(i, 1, m) printf("%d", A[i]); printf("\n");
	
	FOR(i, 0, n)
	{
		for (int j = 1; j <= m; j += (1 << (i + 1)))
		{
			FOR(k, j, j + (1 << i))
			{
				if (A[k] < A[k + (1 << i)]) break;
				else if (A[k] > A[k + (1 << i)])
				{
					FOR(l, j, j + (1 << i)) swap(A[l], A[l + (1 << i)]);
					break;
				}
			}
		}
	}
	
//	FOE(i, 1, m) printf("%d", A[i]); printf("\n");
}

void check(int *A)
{
	int ta, tb, tc;
	int x, y;
	ta = tb = tc = 0;
	FOE(i, 1, m) if (A[i] == 0) ta++; else if (A[i] == 1) tb++; else tc++;
	if (ta == a && tb == b && tc == c && ok == 0) 
	{
		change(A);
		ok = 1;
		FOE(i, 1, m) ANS[i] = A[i];
	}
	else if (ta == a && tb == b && tc == c && ok == 1)
	{
		change(A);
		FOE(i, 1, m) 
		{
			if (ANS[i] == 0) x = 1; else if (ANS[i] == 1) x = 0; else x = 2;
			if (A[i] == 0) y = 1; else if (A[i] == 1) y = 0; else y = 2;
			if (x < y) break;
			else if (y < x)
			{
				FOE(j, 1, m) ANS[j] = A[j];
				break;
			}
		}
	}
}

int main ()
{
	scanf("%d", &tc);
	
	while(tc--)
	{
		scanf("%d %d %d %d", &n, &a, &b, &c);
		
		FOR(i, 0, 5000) A[i] = B[i] = C[i] = 0;
		
		m = 1 << n;
		
		solve(0, 0, 1, m);
		solve(1, 1, 1, m);
		solve(2, 2, 1, m);
		
		ok = 0;
		
		check(A);
		check(B);
		check(C);
		
		printf("Case #%d: ", ++tt);
		if (ok == 1) 
		FOE(i, 1, m) if (ANS[i] == 0) printf("P"); else if (ANS[i] == 1) printf("R"); else printf("S");
		else printf("IMPOSSIBLE");
		
		printf("\n");
	}
	
	return 0;
}
