#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:167772160000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
typedef long long ll;
typedef std::pair<ll, ll> pll;
typedef std::pair<int, int> pii;
//typedef std::pair<long double,long double> pdd;
#define forn(N)          for(int i = 0; i<(int)N; i++)
#define fornj(N)         for(int j = 0; j<(int)N; j++)
#define fornk(N)         for(int k = 0; k<(int)N; k++)
#define forn1(N)          for(int i = 1; i<=(int)N; i++)
#define fornj1(N)         for(int j = 1; j<=(int)N; j++)
#define fornk1(N)         for(int k = 1; k<=(int)N; k++)
#define PI 3.1415926535897932384626433
#define v vector
#define ll long long
#define print(n) printf("%d ", (n));
#define printll(n) printf("%I64d", (n));
#define printline() printf("\n");
#define read(n) scanf("%d", &n);
#define read2(n, m) scanf("%d%d", &n, &m);
#define readll(n) scanf("%I64d", &n);
#define mp make_pair
using namespace std;

struct pos {
	ll x, y, z;

};
pos ast[1100];
bool vis[1100];

double dist(int a, int b) {
	double ret = -sqrt((ast[a].x - ast[b].x)*(ast[a].x - ast[b].x) + (ast[a].y - ast[b].y)*(ast[a].y - ast[b].y) + (ast[a].z - ast[b].z)*(ast[a].z - ast[b].z));
	return ret;

}
int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//(File".in", "r", stdin); freopen(File".out", "w", stdout);
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
	
	int T; cin >> T;
	fornk1(T) {

		int N, S; cin >> N >> S;
		int a;
		forn(N)cin >> ast[i].x >> ast[i].y >> ast[i].z>>a>>a>>a;
		
		//forn(N)cin >> a >> a >> a;
		priority_queue<pair<double, int> >pq;
		pq.push(mp(0, 0));
		forn(N)vis[i] = 0;
		while (1) {
			pair<double, int>now = pq.top();
			pq.pop();
			if (vis[now.second])continue;
			vis[now.second] = 1;
			if (now.second == 1) {
				cout << "Case #" << k << ": " << fixed << setprecision(8) << -now.first << endl;
				break;


			}
			forn1(N-1) {
				pair<double, int> nxt;
				nxt.second = i;
				nxt.first = min(dist(now.second, i), now.first);
				pq.push(nxt);
			}

		}


	}

	
	

	return 0;

}
