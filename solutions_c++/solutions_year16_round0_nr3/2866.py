#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

#define INF 2000000000
#define MOD 1000000007

using namespace std;

int primes[6000000];

int main() {
	freopen("primes.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int primeCnt;
	scanf("%d", &primeCnt);
	for (int i = 0; i < primeCnt; i++)
		scanf("%d", primes + i);
	freopen("input.txt", "r", stdin);
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": " << endl;
		int n, J;
		cin >> n >> J;
		vector<int> divs[J];
		vector<int> nums;
		for (int i = 0; i < (1 << (n - 2)) && nums.size() < J; i++) {
			long long bin = ((1LL << (n - 1)) | 1) | (i << 1);
			bool isGood = true;
			for (int j = 2; j <= 10; j++) {
				long long num = 0;
				long long p = 1;
				for (int k = 0; k < n; k++) {
					if (bin & (1LL << k)) {
						num += p;
					}
					p *= j;
				}
				bool found = false;
				for (int k = 1; k < primeCnt && primes[k] < num; k++) {
					if (num % primes[k] == 0) {
						found = true;
						divs[nums.size()].push_back(primes[k]);
						break;
					}
				}
				if (!found) {
					divs[nums.size()].clear();
					isGood = false;
					break;
				}
			}
			if (isGood) 
				nums.push_back(bin);
		}
		for (int i = 0; i < nums.size(); i++) {
			for (int j = n - 1; j >= 0; j--) {
				if ((1 << j) & nums[i])
					cout << 1;
				else
					cout << 0;
			}
			cout << " ";
			for (int j = 0; j <= 8; j++) 
				cout << divs[i][j] << " ";
			cout << endl;
		}
	}
	return 0;
}
