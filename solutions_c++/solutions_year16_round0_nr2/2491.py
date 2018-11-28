										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int main(){
	freopen("B-Revenge of the Pancakes.in", "r", stdin);
	freopen("B-Revenge of the Pancakes.out", "w", stdout);
	int T, test = 0;
	string str;
	for(cin >> T; T--; ){
		cin >> str;
		str += '+';
		int cnt = 0;
		for(int i = 1; i < str.length(); i++)
			cnt += str[i] != str[i - 1];
		cout << "Case #" << ++test << ": " << cnt << endl;
	}
	return 0;
}
