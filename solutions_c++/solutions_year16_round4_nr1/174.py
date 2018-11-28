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

int a[3];
int numb[5000];
void findnum(int beg, int en, int now) {
	if (beg == en) {
		numb[beg] = now;
		return;
	}
	findnum(beg, (beg + en) / 2, now);
	findnum((beg + en) / 2 + 1, en, (now + 1) % 3);

}
void srt(int beg, int en) {
	if (beg == en)return;
	srt(beg, (beg + en) / 2);
	srt((beg + en) / 2+1,en);
	int hal = (en - beg+1) / 2;
	for (int i = beg; i < beg + hal; i++) {
		if (numb[i] < numb[i + hal])
			break;
		if (numb[i] > numb[i + hal]) {
			for (int j = beg; j < beg + hal; j++)swap(numb[j], numb[j + hal]);

			break;
		}


	}


}

v<int>cnt(int N) {
	v<int>ret;
	forn(3)ret.push_back(0);
	forn(N)ret[numb[i]]++;
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
		v<string>pos;
		int n; cin >> n;
		v<int> a;
		forn(3)a.push_back(0);
		cin >> a[1] >> a[0] >> a[2];
		forn(3) {
			findnum(0, (1 << n) - 1, i);
			v<int>b = cnt(1<<n);
			if (b != a)continue;
			srt(0,(1<<n)-1);
			string s = "";
			forn(1 << n) {
				if (numb[i] == 0)s += 'P';
				if (numb[i] == 1)s += 'R';
				if (numb[i] == 2)s += 'S';

			}
			pos.push_back(s);
		}
		sort(pos.begin(), pos.end());
		cout << "Case #" << k << ": ";
		if (!pos.empty())cout << pos[0];
		else cout << "IMPOSSIBLE";
		cout << endl;

	}

	return 0;

}
