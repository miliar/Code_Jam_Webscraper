#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>

using namespace std;

#define FOR(i,a,b) for(int (i)=(a);i<(b);++i)
#define RFOR(i,b,a) for(int (i)=(b)-1;i>=(a);--i)
#define FILL(A,val) memset(A,val,sizeof(A))

#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define MP make_pair
#define PB push_back

typedef long long Int;
typedef unsigned long long UInt;
typedef vector<int> VI;
typedef pair<int, int> PII;

const double Pi = acos(-1.0);
const int INF = 1000000000;
const int MAX = 1000;
const int BASE = 1000000000;
const int ST = 1000000007;


int p[MAX];

int find_set(int v)
{
	if (v == p[v]) return v;
	return p[v] = find_set(p[v]);
}

void union_sets(int a, int b)
{
	a = find_set(a);
	b = find_set(b);
	if (a != b)
	{
		if (rand() % 2) swap(a , b);
		p[b] = a;
	}
}


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt" , "w", stdout);


	int t;
	cin >> t;
	FOR(tt,0,t)
	{
		printf("Case #%d:\n" , tt + 1);

		int n , m;
		cin >> n >> m;
		VI A(2 * (n + m));
		FOR(i,0,2 * (n + m))
		{
			cin >> A[i];
			-- A[i];
			if (A[i] < m)
			{
				A[i] = (n + 1) * (m + 1) + A[i];
				continue;
			}
			if (A[i] < n + m)
			{
				A[i] -= m;
				A[i] = (A[i] + 1) * (m + 1) - 1;
				continue;
			}
			if (A[i] < n + 2 * m)
			{
				A[i] -= n + m;
				A[i] = m - 1 - A[i];
				A[i] = (n + 1) * (m + 1) + n * m + A[i];
				continue;
			}
			A[i] -= n + 2 * m;
			A[i] = n - 1 - A[i];
			A[i] = A[i] * (m + 1);
		}

		bool fnd = 0;

		FOR(mask, 0 , 1 << (n * m))
		{

			FOR(i,0,2 * (n + 1) * (m + 1))
			{
				p[i] = i;
			}
			FOR(i,0,n)
			{
				FOR(j,0,m)
				{
					if (mask & (1 << (i * m + j)))
					{
						union_sets( (n + 1) * (m + 1) + i * m + j  , i * (m + 1) + j);
						union_sets( (n + 1) * (m + 1) + (i + 1) * m + j  , i * (m + 1) + j + 1);
					}
					else
					{
						union_sets( (n + 1) * (m + 1) + i * m + j  , i * (m + 1) + j + 1);
						union_sets( (n + 1) * (m + 1) + (i + 1) * m + j  , i * (m + 1) + j);
					}
				}
			}

			bool ok = 1;
			for(int i = 0; i < SZ(A); i += 2)
				if (find_set(A[i]) != find_set(A[i + 1]))
				{
					ok = 0;
					break;
				}

			if (ok)
			{
				fnd = 1;
				FOR(i,0,n)
				{
					FOR(j,0,m)
					{
						if (mask & (1 << (i * m + j)))
						{
							cout << "/";
						}
						else
						{
							cout << "\\";
						}
					}
					cout << endl;
				}
				break;
			}
		}



		if (!fnd) cout << "IMPOSSIBLE" << endl;

		cerr << tt << endl;

	}

	//cout << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	return 0;
}
