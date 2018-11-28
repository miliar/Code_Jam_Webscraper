#include "stdafx.h"
#include <cstdio>
#include <algorithm>
#include <string>
#include <fstream>
#include <queue>
#include <iostream>
using namespace std;
  
#define INF 3000000000LL
#define MOD 1000000007LL;
#define CHK 10000000
#define cout f
typedef long long ll;
int Q,N,M,K,L;

int main() {

	cin >> Q;
	ofstream f;
	f.open("output.txt");
	for (int qq = 0; qq < Q; qq ++) {
		ll N;
		int chk = 0;
		cin >> N;
		cout << "Case #" << qq + 1 << ": ";
		bool flag = false;
		for (int i = 1; i <= 1000000; i ++) {
			ll k = N * i;
			while (k) {
				chk |= (1<<(k%10));
				k /= 10;
			}
			if (chk == (1<<10)-1) {
				cout << N * i << endl;
				flag = true;
				break;
			}
		}
		if (!flag) cout << "INSOMNIA" << endl;
	}

	return 0;
}