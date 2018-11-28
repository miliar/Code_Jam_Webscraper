#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <utility>
#include <cstring>
#include <list>
#include <stack>
#include <tr1/unordered_map>
#include <windows.h>

using namespace std;
using namespace tr1;

#define ft first
#define sd second

typedef long long LL;
typedef unsigned int UI;

const int MAXN = 511111;
const int MOD = 1e9 + 7;
const double eps = 1e-6;
const LL MAXL = (LL)(0x7fffffffffffffff);
const int MAXI = 0x7fffffff;


int main(){

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	
	int T;
	cin >> T;
	for(int cases = 1; cases <= T; cases++){
		int sMax;
		string p;
		cin >> sMax >> p;
		int n = 0, sum = 0;
		for(int i = 0; i < p.length(); i++){
			if(n < i){
				sum += i - n;
				n = i;
			}
			n += p[i] - '0';
		}
		printf("Case #%d: %d\n", cases, sum);
	}
}
