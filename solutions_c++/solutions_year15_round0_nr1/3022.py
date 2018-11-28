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

int n;
string str;

int main(){
	freopen("A-Standing Ovation.in", "r", stdin);
	freopen("A-Standing Ovation.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n >> str;
		int sum = str[0] - '0', nd = 0;
		for(int i = 1; i <= n; i++){
			if(str[i] > '0')
				nd = max(nd, i - sum);
			sum += str[i] - '0';
		}
		cout << "Case #" << ++test << ": " << nd << endl;
	}
	return 0;
}
