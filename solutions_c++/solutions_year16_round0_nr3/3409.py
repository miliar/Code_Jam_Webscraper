#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <string>
#include <climits>
#define ull unsigned long long
#define ll long long
#define ul unsigned long
#define vi vector<int>
#define vll vector<long long>
#define pb push_back
#define pii pair<int, int>
#define pll pair<long long, long long>
#define mp make_pair
#define pq priority_queue

using namespace std;

vi primes;
bool np[1000005];

int main() {
	np[0] = np[1] = true;
	for(int i = 4; i <= 1000000; i += 2) np[i] = true;
	
	primes.pb(2);
	for(int i = 3; i <= 1000000; i += 2) {
		if(np[i]) continue;
		for(int j = 3 * i; j <= 1000000; j += 2 * i) np[j] = true;
		primes.pb(i);
	}
	
	
	scanf("%*d");
	int n, j;
	scanf("%d %d", &n, &j);
	printf("Case #1:\n");
	
	int arr[16];
	for(int bin = (1 << (n - 1)) + 1; j > 0; bin += 2) {
		int base;
		
		memset(arr, -1, sizeof arr);
		for(base = 2; base <= 10; ++base) {
			ll num = 0ll;
			for(int i = n - 1; i >= 0; --i) {
				num = num * base + ((bin & (1 << i)) > 0);
			}
			
			for(int p: primes) {
				if(p < num && num % p == 0ll) {
					arr[base] = p;
					break;
				}
			}
			
			if(arr[base] == -1) {
				break;
			}
		}
		
		if(base > 10) {
			--j;
			for(int i = n - 1; i >= 0; --i) {
				printf("%d", (bin & (1 << i)) > 0);
			}
			
			for(int b = 2; b <= 10; ++b) {
				printf(" %d", arr[b]);
			}
			puts("");
		}
	}
	
	return 0;
}
