#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define MOD 1000000007
#define MAXN 100001

#define PRIME 1000008259

using namespace std;

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

	int tc; cin >> tc;
	
	for (int tc_i = 0; tc_i < tc; tc_i++) {
		int n;
		cin >> n;
		pair<int, int> arr[30];
		int total = 0;
		
		for (int i = 0; i < n; i++) {
			cin >> arr[i].first;
			arr[i].second = i;
			total += arr[i].first;
		}
				
		bool empty = false;
		
		cout << "Case #" << (tc_i + 1) << ":";
		
		while (!empty) {
			sort(arr, arr + n);
			
			if (arr[n - 2].first > ((total - 1) / 2)) {
				arr[n - 2].first--;
				arr[n - 1].first--;
				
				cout << " " << (char)('A' + arr[n - 2].second) << (char)('A' + arr[n - 1].second);
				total -= 2;
			}
			else {
				arr[n - 1].first--;

				cout << " " << (char)('A' + arr[n - 1].second);
				total--;
			}
			
			if (arr[n - 1].first == 0) {
				n--;
			}

			if (arr[n - 1].first == 0) {
				n--;
			}
			
			empty = total == 0;
		}
		
		cout << endl;
	}
    return 0;
}