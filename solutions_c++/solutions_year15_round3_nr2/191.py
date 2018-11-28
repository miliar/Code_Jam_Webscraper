#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <functional>
using namespace std;

#define mp make_pair
#define lli long long int

const int N = (int)(103);

string s;
vector<int> pi;

int calcPrefix(int pos, char c) {
	if (!pos) return 0;
	int j = pi[pos-1];
	while (j > 0 && c != s[j])
		j = pi[j-1];
	if (c == s[j])  ++j;
	return j;
}

vector<int> prefix_function (string s) {
	int n = (int) s.length();
	pi.resize(n);
	for(int i = 0; i < n; ++i) pi[i] = 0;
	for (int i=1; i<n; ++i) {		
		pi[i] = calcPrefix(i, s[i]);
	}
	return pi;
}

double d[N][N][N];
double p[3030];

int main() {
//#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
//#endif
	int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq+1 << ": ";

		memset(d, 0, N*N*N*sizeof(double));
		int k, l, step;
		cin >> k >> l >> step;
		string prob;
		cin >> prob >> s;

		prefix_function(s);
		for(int i = 'A'; i <= 'Z'; ++i) p[i] = 0;
		for(int i = 0; i < prob.length(); ++i) p[prob[i]]++;
		for(int i = 'A'; i <= 'Z'; ++i) p[i]/=prob.length();

		d[0][0][0] = 1;
		int maxPref = 0;

		for(int st = 0; st < step; ++st) {
			for(int pLen = 0; pLen < s.length(); ++pLen) {
				for(int count = 0; count <= step; ++count) {
					if (d[st][pLen][count] > 0) {

						for(int ch = 'A'; ch <= 'Z'; ++ch) {
							if (ch == s[pLen]) continue;
							if (p[ch] > 0) {
								d[st + 1][ calcPrefix(pLen, ch) ][count] += p[ch] * d[st][pLen][count];
								//cout << st+1 << " " << calcPrefix(pLen, ch) << " " << count << " += " << p[ch] * d[st][pLen][count] << " by " << ch;
							}
						}

						if (p[ s[pLen] ] > 0) {
							if (pLen + 1 == s.length()) {
								d[st + 1][ calcPrefix(pLen, s[pLen]) ][count + 1] += p[s[pLen]] * d[st][pLen][count];
								//cout << st+1 << " " << calcPrefix(pLen, s[pLen]) << " " << count+1 << " += " << p[s[pLen]] * d[st][pLen][count] << " by " << s[pLen];
							} else {
								d[st + 1][ pLen + 1 ][count] += p[s[pLen]] * d[st][pLen][count];
								//cout << st+1 << " " << pLen + 1 << " " << count << " += " << p[s[pLen]] * d[st][pLen][count] << " by " << s[pLen];
							}
						}						

					}
				}
			}
		}
		
		double ans = 0;
		int maxPossible = 0;

		for(int pLen = 0; pLen < s.length(); ++pLen) {
			for(int count = 0; count <= step; ++count) {
				if (d[step][pLen][count] > 0) {
					maxPossible = max(count, maxPossible);
					ans += d[step][pLen][count] * count;
				}
			}
		}
		printf("%.12lf", maxPossible - ans);

		cout << endl;
	}
    return 0;
}   