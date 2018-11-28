#include <iostream>
#include <cmath>
#include <deque>
#include <algorithm>
#include <map>
#include <cstdio>
#include <sstream>
#include <deque>

using namespace std;

#define MAXN 12000
#define pi pair <int, int>
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a.size())

using namespace std;

typedef deque<int> VI;
typedef deque<VI> VVI;
typedef long long ll;
typedef deque<ll> VL;
typedef deque<VL> VVL;
typedef double D;
typedef deque<D> VD;
typedef deque<VD> VVD;
typedef pair<int, int> PI;
typedef deque<PI> VPI;

int T;
int N, M, flag;
VVI x;
VI a, b;
string S[2] = {"NO", "YES"};

int main (int argc, char const* argv[])
{
	cin >> T;

	for (int cs = 1; cs <= T; cs += 1)
	{
		cin >> N >> M;
		x = VVI(N,VI(M));
		a = VI(N,0);
		b = VI(M,0);
		for (int i = 0; i < N; i += 1)
		{
			for (int j = 0; j < M; j += 1)
			{
				cin >> x[i][j];
				a[i] = max(a[i],x[i][j]);
				b[j] = max(b[j],x[i][j]);
			}
		}

		flag = 1;
		
		for (int i = 0; i < N; i += 1)
		{
			for (int j = 0; j < M; j += 1)
			{
				if (x[i][j] != min(a[i],b[j]))
				{
					flag = 0;
				}
			}
		}
		for (int i = 0; i < N; i += 1)
		{
			for (int j = 0; j < M; j += 1)
			{
				cout << x[i][j] - min(a[i],b[j]) << '\t';
			}
			cout << '\n';
		}
		
		
		cout << "Case #" << cs << ": " << S[flag] << '\n';
	}
	
	
	return 0;
}










