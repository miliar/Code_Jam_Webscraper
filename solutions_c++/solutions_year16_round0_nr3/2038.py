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
	freopen("C-Coin Jam.in", "r", stdin);
	freopen("C-Coin Jam.out", "w", stdout);
	int T, n, k;
	cin >> T >> n >> k;
	cout << "Case #1:" << endl;
	for(int I = 0; I < k; I++){
		string str = "1";
		for(int i = 0; i < n - 2; i++)
			str = (char)('0' + (I >> (i / 2)) % 2) + str;
		cout << "1" + str;
		for(int i = 2; i <= 10; i++)
			cout << ' ' << i + 1;
		cout << endl;
	}
	return 0;
}
