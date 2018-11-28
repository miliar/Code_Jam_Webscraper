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
	
    int tc;
	cin >> tc;
	
	long long power[11][32];
	
	for (int i = 2; i < 11; i++) {
		power[i][0] = 1LL;
		for (int j = 1; j < 32; j++) {
			power[i][j] = power[i][j - 1] * i;
		}
	}
	
    for (int tc_i = 0; tc_i < tc; tc_i++) {
		int N, J;
		cin >> N >> J;
				
		cout << "Case #" << (tc_i + 1) << ":" << endl;

		for (int i = 0; i < (1 << N - 2); i++) {
			int pos = 1;
			int x = i;
			
			int bit[32] = {0};
			bit[0] = bit[N - 1] = 1;
			
			while (x) {
				bit[pos] = x % 2;
				x /= 2;
				pos++;
			}
			
			vector<int> res;
			bool good = true;
			
			for (int j = 2; good && j < 11; j++) {
				long long num = 0;
				
				for (int k = 0; k < N; k++) {
					num += power[j][k] * bit[k];
				}
				
				good = false;
				
				for (int k = 2; k < sqrt(.0 + num) + 1; k++) {
					if (num % k == 0) {
						good = true;
						res.push_back(k);
						break;
					}
				}
			}
			
			if (good) {
				J--;
				for (int j = 0; j < N; j++) {
					cout << bit[N - 1 - j];
				}
				cout << " ";
				
				for (int j = 0; j < res.size(); j++) {
					cout << res[j] << " ";
				}
				cout << endl;
			}
			
			if (J == 0) {
				break;
			}
		}
    }

    return 0;
}