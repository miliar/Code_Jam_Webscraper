#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <unordered_set>
#include <stack> 
#include <algorithm>
#include <math.h>
#include <sstream>
#include <functional>
#include <bitset>
#pragma comment (linker, "/STACK:167177216")
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
#define sz(a) (int)a.size()
#define pb push_back
const int MAXN = 2 * 1000 * 1000 + 500;
const double EPS = 1e-9;



int main(int argc, char* argv[]) {

#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("numbers.in", "r", stdin); freopen("numbers.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);

	int ttt;
	cin >> ttt;
	forn(tt, 0, ttt){
		string s;
		cin >> s;
		vector<int> ans(10);

		vector<int> count(1050);
		for (int i = 0; i < s.size(); ++i){
			count[s[i]]++;
		}

		vector<string> d(10);
		d[0] = "ZERO";
		d[1] = "TWO";
		d[2] = "EIGHT";
		d[3] = "SIX";
		d[4] = "FOUR";
		d[5] = "THREE";
		d[6] = "ONE";
		d[7] = "SEVEN";
		d[8] = "FIVE";
		d[9] = "NINE";

		string good = "ZWGXUROSVN";
		string good2 = "0286431759";

		for (int i = 0; i < good.size(); ++i){
			while (count[good[i]] > 0){
				ans[good2[i] - '0']++;
				for (int j = 0; j < d[i].size(); ++j){
					count[d[i][j]]--;
				}
			}
		}

		printf("Case #%d: ", tt + 1);
		forn(i, 0, 10){
			for (int j = 0; j < ans[i]; ++j){
				printf("%d", i);
			}
		}

		printf("\n");
	}

	return 0;
}