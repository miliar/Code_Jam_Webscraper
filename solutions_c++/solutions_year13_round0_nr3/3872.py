#include <cstdio>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <string>
#include <cmath>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long

using namespace std;

const int MAXN = 1e7;

ll A, B;
vector <ll> v;
bool check(ll x) {
	
	int A[100];
	A[0] = 0;

	while(x > 0) {
		A[++A[0]] = x % 10;
		x /= 10;
	}
	
	for (int ls = 1, ld = A[0] ; ls <= ld; ++ls, --ld)
		if(A[ls] != A[ld])
			return 0;
	return 1;
}
int main() {
	ifstream cin("test.in");
	ofstream cout("test.out");
	
	int T;	
	cin >> T;
	

	v.push_back(0);

	for (ll i = 1; i <= MAXN; ++i) {
		if(check(i * i) && check(i)) {
			v.push_back(i * i);
		}
	}
/*	
	for (int i = 0; i < v.size(); ++i)
		cout << v[i] << "\n" ;
	cout << "\n";
*/	for (int test = 1; test <= T; ++test) {
		cin >> A >> B;
		int r = 0, l = 0;
		
		for (int i = 0 ; i < v.size(); ++i) {
			if(B < v[i]) {
				--r;
				break;
			}
			r++;
		}
		for (int i = 0 ;i < v.size(); ++i) {
			if(A <= v[i]) {
				--l;
				break;
			}
			l++;
		}

		cout << "Case #" << test << ": "  << r - l << "\n";
	}

	return 0;
}
