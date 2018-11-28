#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

#define pow dkfjsd

using namespace std;

const double eps = 1e-9;
const int inf = 1e9 + 23;

const int size = 2 * 1000;

long long pow[size];

long long can(int n, long long p){
	if (pow[n] <= p)
		return pow[n];
	//long long ans = can(n - 1, p);
	return 2 * can(n - 1, p) - 1;
}

long long guarant(int n, long long p){
	if (p <= pow[n - 1])
		return 1;
	return min(2 * guarant(n - 1,p - pow[n - 1]) + 1, pow[n]);
}


int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	long long p;

	int it;
	cin >> it;
	pow[0] = 1;
	for (int i = 1; i < 52; i++){
		pow[i] = pow[i - 1] * 2;
	}
	for (int t = 1; t <= it; t++){
		printf("Case #%d: ", t);
		cin >> n >> p;
		cout << guarant(n, p) - 1 << " " << can(n, p) - 1 << endl;
	}

	return 0;
}