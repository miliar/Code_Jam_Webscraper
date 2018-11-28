#include <iostream>
#include <vector>
#include <fstream>
#include <cstdio>
#include <set>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <complex>
#include <string>
#include <cmath>
#include <deque>
#include <map>
#include <cstdlib>
#include <locale>
#include <limits>
#include <complex>
#include <sstream>
#include <utility>
//#include <list>

#define pb push_back
#define Size(x) ((int)(x.size()))
//#define X real()
//#define Y imag()

using namespace std;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef long long int lint;
//typedef unsigned long long lint;

void init(vector <vector <int> > &a, vector <vector <int> > &v, int N, int  M)
{
	a.resize(N);
	v.resize(N);
	for (int i = 0; i < N; i++)
	{
		a[i].resize(M, 100);
		v[i].resize(M);
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	stdin = freopen("B.in", "r", stdin);
	stdout = freopen("B.out", "w", stdout);
	int T;
	cin >> T;
	for (int q = 0; q < T; q++)
	{
		cout << "Case #" << q + 1 << ": ";
		vector <vector <int> > a, v;
		int N, M;
		cin >> N >> M;
		init(a, v, N, M);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				cin >> v[i][j];
		for (int i = 0; i < N; i++)
		{
			int m = *max_element(v[i].begin(), v[i].end());
			for (int j = 0; j < M; j++)
				a[i][j] = min(m, a[i][j]);
		}
		for (int j = 0; j < M; j++)
		{
			int m = -1;
			for (int i = 0; i < N; i++)
				m = max(m, v[i][j]);
			for (int i = 0; i < N; i++)
				a[i][j] = min(m, a[i][j]);
		}
		bool ok = true;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (a[i][j] != v[i][j])
					ok = false;
		ok ? cout << "YES" : cout << "NO";
		cout << endl;
	}
	
	return 0;
}
