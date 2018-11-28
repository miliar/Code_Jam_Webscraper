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
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
//typedef uint64_t ull;
//typedef std::pair<long double,long double> pdd;
#define for8(i) for( i = 1; i<=8; i++)
#define fori(N)          for(int i = 0; i<(N); i++)
#define forj(N)         for(int j = 0; j<(N); j++)
#define fork(N)         for(int k = 0; k<(N); k++)
#define forl(N)         for(int l = 0; l<(N); l++)
#define ford(N)         for(int d = 0; d<(N); d++)
#define fori1(N)          for(int i = 1; i<=(N); i++)
#define forj1(N)         for(int j = 1; j<=(N); j++)
#define fork1(N)         for(int k = 1; k<=(N); k++)
#define ford1(N)         for(int d = 1; d<=(N); d++)
#define PI (2*asin(1))
#define print(n) printf("%d ", (n))
#define printll(n) printf("%I64d ", (n))
#define printline() printf("\n")
#define read(n) scanf("%d", &n);
#define read2(n, m) scanf("%d%d", &n, &m);
#define readll(n) scanf("%I64d", &n);
#define mp make_pair
template <typename T>
using min_heap = std::priority_queue<T, std::vector<T>, std::greater<T> >;
template <typename T>
using max_heap = std::priority_queue<T, std::vector<T>, std::less<T> >;

bool extraFlip[5000];
bool cakes[5000];

int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int numberOfCases; cin >> numberOfCases;
	for (int currentCase = 1; currentCase <= numberOfCases; currentCase++) {
		string s; cin >> s;
		int k; cin >> k;
		int n = s.length();
		fori(n)cakes[i] = (s[i] == '-');
		bool flipped = false;
		fori(n + 1)extraFlip[i] = false;
		bool fail = 0;
		int answer = 0;
		fori(n) {
			flipped ^= extraFlip[i];
			if (flipped != cakes[i]) {
				if (n - i < k)
					fail = true;
				else {
					answer++;
					flipped = !flipped;
					extraFlip[i + k] = !extraFlip[i + k];
				}
			}
			
		}
		cout << "Case #" << currentCase << ": ";
		if (fail)cout << "IMPOSSIBLE";
		else cout << answer;

		cout << endl;
	}

	return 0;

}