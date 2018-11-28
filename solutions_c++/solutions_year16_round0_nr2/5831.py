#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#define maxn  100
using namespace std;
bool a[maxn];
string s;
int main(){
	FILE *in, *out;
	in = freopen("in.txt", "r", stdin);
	out = freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> s;
		int ans = 0;
		int n = s.length();
		int j = 0;
		if (s[j] == '-')
			ans = 1;
		while (s[j] == '-') {
			s[j] = '+';
			j++;
		}
		while (j < n) {
			while (s[j] == '+')
				j++;
			if (j != n)
				ans += 2;
			while (s[j] == '-') {
				s[j] = '+';
				j++;
			}
		}
		fprintf(out, "Case #%d: %d\n", i, ans);
	}
	fclose(in);
	fclose(out);
	return 0;
}