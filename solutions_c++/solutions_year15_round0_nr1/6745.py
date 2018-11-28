//#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
#include <cstdio>
#include <cstring>
#include <ciso646>
#include <set>
#include <algorithm>
#include <map>
#include <iomanip>
#include <string>
#include <list>
#include <bitset>
#include <stack>
#include <queue>
#include <sstream>
using namespace std;
//look at my code my code is amazing
#define FOR(i, a, b) for (int i = int(a); i < int(b); i++)
#define ROF(i, a, b) for (int i = int(a); i >= int(b); i--)
#define REP(i, a) for (int i = 0; i < int(a); i++)
#define INF 1000000000
#define ALL(x) x.begin(), x.end()
#define MP(a, b) make_pair((a), (b))
#define X first
#define Y second
#define EPS 1e-9

#define DEBUG(x) cerr << #x << ": " << x << " "
#define DEBUGLN(x) cerr << #x << ": " << x << " \n"
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef long long ll;
typedef vector<bool> vb;
//ios::sync_with_stdio(0);//fast entrada/salida ;-)

string s;

void solve(int caso)
{
	int S;

	cin >> S >> s;

	int paradas = 0;
	int acarreados = 0;

	REP(i, S+1)
	{
		if(paradas < i)
		{
			acarreados += i - paradas;
			paradas += i - paradas;
		}
		paradas += s[i] - '0';
	}

	cout << "Case #" << caso << ": " << acarreados << "\n";
}

int main()
{
	ios::sync_with_stdio(0);//fast entrada/salida ;-)
	int T;


	cin >> T;

	REP(i, T)
	{
		solve(i+1);

	}

	return 0;
}