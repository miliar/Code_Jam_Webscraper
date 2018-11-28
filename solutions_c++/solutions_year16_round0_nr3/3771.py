#include "stdafx.h"
#include <cstdio>
#include <algorithm>
#include <string>
#include <queue>
#include <iostream>
using namespace std;
  
#define INF 3000000000LL
#define MOD 1000000007LL;
#define CHK 10000000
typedef long long ll;
int Q,N,M,K,L;
ll arr[11];
ll po[11][51];
vector<string> sr;
vector<ll> si[11];

ll isPrime(ll n) {
	for (ll i = 2; i * i < n; i ++)
		if (n % i == 0) return i;
	return 0;
}



int main() {

	for (int i = 1; i < 11; i ++) po[i][0] = 1;
	for (int i = 1; i < 11; i ++)
		for (int j = 1; j < 51; j ++)
			po[i][j] = po[i][j - 1] * i;

	cin >> Q;
	for (int qq = 0; qq < Q; qq ++) {
		cin >> N >> M;
		cout << "Case #" << qq + 1 << endl;
		int k = (1 << N) - 1;
		while (k) {
			if (k <= pow(2, N - 1)) break;
			if (!M) break;
			if (k % 2 == 0) {
				k --;
				continue;
			}
			int p = k;
			int m = 0;
			for (int i = 2; i < 11; i ++) arr[i] = 0;
			while (p) {
				if (p & 1) {
					for (int i = 2; i < 11; i ++) {
						arr[i] += po[i][m];
					}
				}
				m ++;
				p = (p >> 1);
			}
			bool flag = true;
			int z = 0;
			for (int i = 2; i < 11; i ++) {
				ll pn = isPrime(arr[i]);
				if (!pn) {
					flag = false;
					z = i - 1;
					break;
				}
				si[i].push_back(pn);
			}
			if (!flag) {
				for (int i = 2; i <= z; i ++)
					si[i].pop_back();
				k --;
				continue;
			}
			p = k;
			string s;
			while (p) {
				s += to_string((p & 1));
				p = (p >> 1);
			}
			reverse(s.begin(), s.end());
			sr.push_back(s);
			k --;
			M --;
		}
		for (int i = 0; i < sr.size(); i ++) {
			cout << sr[i] << " ";
			for (int j = 2; j < 11; j ++)
				cout << si[j][i] << " " ;
			cout << endl;
		}
	}
	cin >> N;

	return 0;
}