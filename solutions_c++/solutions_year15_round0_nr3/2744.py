#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <string.h>
#include <string>
#include <limits.h>
#include <algorithm>
#include <set>
#include <ctime>
using namespace std;
#define SZ(x) ((int)(x).size())
#define rep(i,a,n) for (int i=a; i<(int)n; i++)
#define per(i,n,a) for (int i=n; i>=a; i--)
#define hk push_back
#define pk pop_back
#define mp make_pair
#define PI 3.141592653589793
#define clr(a) memset(a, 0, sizeof(a))
#define clr1(a) memset(a, -1, sizeof(a))
typedef vector<int> VI;
typedef vector< pair<int, int> > VIP;
typedef vector< pair<int, pair<int, double> > > VIPP;
typedef vector<string> VS;
typedef vector <double> VD;
typedef vector <bool> VB;
typedef long long ll;
#define MAX_V 1000
const ll mod = 1000000007;
ll powmod(ll a, ll b) {
	ll res = 1; a %= mod; for (; b; b >>= 1){ if (b & 1)res = res*a%mod; a = a*a%mod; }return res;
}

int T, L, X;
string s;

int main() {
	cout.precision(12);
	cin >> T;
	int T1 = 0;
	while (T1++ < T) {
		cin >> L >> X >> s;

		char c = s[0];
		bool positive = true;
		rep(i, 1, L) {
			if (c == s[i]) {
				positive = !positive;
				c = 'l';
			}
			else if (c == 'l') c = s[i];
			else if (c == 'i') {
				if (s[i] == 'j') c = 'k';
				else {
					c = 'j'; positive = !positive;
				}
			}
			else if (c == 'j') {
				if (s[i] == 'k') c = 'i';
				else {
					c = 'k'; positive = !positive;
				}
			}
			else if (c == 'k') {
				if (s[i] == 'i') c = 'j';
				else {
					c = 'i'; positive = !positive;
				}
			}
		}


		if ((c == 'l' && (X % 2) && !positive) || ((c != 'l') && (X % 4) == 2)) {
			if (((c != 'l') && (X % 4) == 2)) {
				s += s;
				X /= 2;
				L *= 2;
			}
			int recursiveIdx = 0;
			int idx_i = -1;
			if (s[0] == 'i') idx_i = 0;
			//find i idx start
			if (idx_i == -1) {
				char c = s[0];
				bool positive = true;
				int idx_i1 = -1;
				int idx_i2 = -1;
				rep(i, 1, L + 1) {
					if (c == 'i' && positive) {
						if (i == L) recursiveIdx++;
						idx_i1 = i - 1; break;
					}
					if (c == 'i' && !positive && idx_i2 == -1) {
						if (i == L) recursiveIdx++;
						idx_i2 = i - 1;
					}

					char cNext = s[i % L];
					if (c == cNext) {
						positive = !positive;
						c == 'l';
					}
					else if (c == 'l') c = cNext;
					else if (c == 'i') {
						if (cNext == 'j') c = 'k';
						else {
							c = 'j'; positive = !positive;
						}
					}
					else if (c == 'j') {
						if (cNext == 'k') c = 'i';
						else {
							c = 'k'; positive = !positive;
						}
					}
					else if (c == 'k') {
						if (cNext == 'i') c = 'j';
						else {
							c = 'i'; positive = !positive;
						}
					}
				}

				if (idx_i1 != -1) idx_i = idx_i1;
				else if (idx_i2 != -1) {
					idx_i = idx_i2; recursiveIdx++;
				}
			}
			//find i idx end

			int idx_j = -1;
			if (s[(idx_i + 1) % L] == 'j') {
				if (idx_i + 1 >= L) recursiveIdx++;
				idx_j = 0;
			}
			//find j idx start
			if (idx_j == -1) {
				char c = s[(idx_i + 1) % L];
				bool positive = true;
				int idx_j1 = -1;
				int idx_j2 = -1;
				rep(i, idx_i + 2, idx_i + L + 2) {
					if (c == 'j' && positive) {
						if (i >= L) recursiveIdx++;
						idx_j1 = i - 1; break;
					}
					if (c == 'j' && !positive && idx_j2 == -1) {
						if (i >= L) recursiveIdx++;
						idx_j2 = i - 1;
					}

					char cNext = s[i % L];
					if (c == cNext) {
						positive = !positive;
						c == 'l';
					}
					else if (c == 'l') c = cNext;
					else if (c == 'i') {
						if (cNext == 'j') c = 'k';
						else {
							c = 'j'; positive = !positive;
						}
					}
					else if (c == 'j') {
						if (cNext == 'k') c = 'i';
						else {
							c = 'k'; positive = !positive;
						}
					}
					else if (c == 'k') {
						if (cNext == 'i') c = 'j';
						else {
							c = 'i'; positive = !positive;
						}
					}
				}

				if (idx_j1 != -1) idx_j = idx_j1;
				else if (idx_j2 != -1) {
					idx_j = idx_j2; recursiveIdx++;
				}
			}
			//find j idx end
			if (idx_i != -1 && idx_j != -1 && recursiveIdx < X) {
				cout << "Case #" << T1 << ": YES" << endl;
			}
			else 
				cout << "Case #" << T1 << ": NO" << endl;
		}
		else {
			cout << "Case #" << T1 << ": NO" << endl;
		}
	}

	return 0;
}