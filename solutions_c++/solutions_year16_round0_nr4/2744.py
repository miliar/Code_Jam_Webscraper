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


int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": ";
		long long k, c, s;
		long long p = 1;
		cin >> k >> c >> s;
		for (int i = 0; i < c - 1; i++)
			p *= k;
		for (long long i = 0; i < s; i++) {
			cout << i * p + 1 << " ";
		}
		cout << endl;
	}
	return 0;
}
