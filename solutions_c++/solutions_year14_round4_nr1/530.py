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

int T, n, s;
int arr[100000];

int main(){
	int test = 0;
	freopen("A_Data Packing.in", "r", stdin);
	freopen("A_Data Packing.out", "w", stdout);
	for(cin >> T; T--; ){
		cin >> n >> s;
		for(int i = 0; i < n; i++)
			cin >> arr[i];
		sort(arr, arr + n);
		reverse(arr, arr + n);
		int str = 0, end = n - 1;
		int cnt = 0;
		while(str <= end){
			cnt++;
			if(arr[str] + arr[end] <= s)
				end--;
			str++;
		}
		cout << "Case #" << ++test << ": " << cnt << endl;
	}
	return 0;
}
