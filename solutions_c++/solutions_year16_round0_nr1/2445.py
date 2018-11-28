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
#define Max 1000001

int last[Max];

int main(){
	freopen("A-Counting Sheep.in", "r", stdin);
	freopen("A-Counting Sheep.out", "w", stdout);
	for(int i = 1; i <= Max; i++){
		int mask = 0, j = 0;
		while(mask != 1023){
			int t = i * ++j;
			for(; t; t /= 10)
				mask |= 1 << t % 10;
		}
		last[i] = i * j;
	}
	int T, test = 0, x;
	for(cin >> T; T--; ){
		cin >> x;
		cout << "Case #" << ++test << ": ";
		if(x == 0) cout << "INSOMNIA" << endl;
		else cout << last[x] << endl;
	}
	return 0;
}
