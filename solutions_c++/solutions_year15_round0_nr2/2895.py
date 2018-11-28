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
int arr[1010];

int main(){
	freopen("B-Infinite House of Pancakes.in", "r", stdin);
	freopen("B-Infinite House of Pancakes.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n;
		for(int i = 0; i < n; i++)
			cin >> arr[i];
		int mn = 10000;
		for(int i = 1; i <= 1000; i++){
			int cnt = i;
			for(int j = 0; j < n; j++)
				cnt += (arr[j] - 1) / i;
			mn = min(mn, cnt);
		}
		cout << "Case #" << ++test << ": " << mn << endl;
	}
	return 0;
}
