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

int n, arr[1010];
vector <P> srt;
int bef[1010], aft[1010];

int main(){
	freopen("B_Up and Down.in", "r", stdin);
	freopen("B_Up and Down.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		memset(bef, 0, sizeof bef);
		memset(aft, 0, sizeof aft);
		srt.clear();

		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> arr[i];
			srt.push_back(P(arr[i], i));
		}
		sort(srt.begin(), srt.end());
		for(int i = 0; i < n; i++){
			int idx = srt[i].second;
			for(int j = 0; j < idx; j++)
				if(arr[j] > arr[idx])
					bef[i]++;
			for(int j = idx + 1; j < n; j++)
				if(arr[j] > arr[idx])
					aft[i]++;
		}
		int res = 0;
		for(int i = 0; i < n; i++)
			res += min(bef[i], aft[i]);

		cout << "Case #" << ++test << ": " << res << endl;
	}
	return 0;
}
