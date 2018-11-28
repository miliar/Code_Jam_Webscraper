#pragma comment(linker, "/STACK:1000000000")
#define _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <locale>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#define rep(x, a, b) for(int (x) = (a); (x) < int(b); ++(x))
#define Wait cin.sync(); cin.get();
#define INF 0x3F3F3F3F
#define y1 qwerty 
#define EPS 1e-6
using namespace std;
typedef long long                  ll;
typedef pair<long long, long long> pll;
typedef pair<int, int>             pii;
typedef pair<double, int>          pdi;
typedef pair<double, double>       pdd;
typedef pair<string, string>       pss;

#define FILE

int T;
int n;
int s[100];
int sum[100];
int ans = 0;
char c;


int main(){
#ifdef FILE
   freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);

#endif
 
	cin >> T;
	for (int t = 0; t < T; ++t){
		cin >> n;
		ans = 0;
		memset(s, 0, sizeof s);
		for (int j = 1; j <= n + 1; ++j){
			cin >> c;
			s[j] = c - '0';
			//cout << "sj " << s[j] << endl;
			if (s[j] != 0 && sum[j - 1] < j - 1){
				//cout << sum[j - 1] << " < " << j - 1 << endl;
				int d = j - 1 - sum[j - 1];
				ans += d;
				sum[j - 1] += d;
			}
			sum[j] = sum[j - 1] + s[j];
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
		//for (int j = 0; j < n; ++j) cout << s[j] << " "; cout << endl;
	}

#ifdef FILE
  // printf("TIME: %.3lf\n", (long double)(clock()) / CLOCKS_PER_SEC);
#endif
   Wait
   return 0;
}