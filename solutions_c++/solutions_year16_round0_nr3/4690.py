#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <algorithm>
#define maxn  16
using namespace std;
int a[maxn];
int b[50][maxn];
string s;
int kol = 0;
FILE *in, *out;
long long int tr(int x) {
	long long int t = 1;
	long long int ans = 0;
	for (int i = 15; i >= 0; i--) {
		ans += t*a[i];
		t *= x;
	}
	return ans;
}

bool simp() {
	for (int x = 2; x <= 10; x++) {
		long long int x1 = tr(x);
		bool ans = true;
		for (int i = 2; i < 150; i++)
			if ((x1 % i) == 0) {
				ans = false;
				break;
			}
		if (ans == true)
			return true;
	}
		return false;
}

bool del() {
	for (int x = 2; x <= 10; x++) {
		long long int x1 = tr(x);
		bool ans = true;
		for (int i = 2; i < 150; i++)
			if ((x1 % i) == 0) {
				ans = false;
				cout << i << ' ';
				break;
			}
		if (ans == true)
			return true;
	}
	return false;
}

void gen(int n, int k) {
	int i = 0;
	if (n < k) {
		for (i = 0; i < 2; i++) {
			a[n] = i;
			gen(n + 1, k);
		}
	}
	else {
		if (!simp()) {
			for (int h = 0; h <= 15; h++)
				b[kol][h] = a[h];
			kol++;
		}
		if (kol == 50) {
			for (int p = 0; p < 50; p++) {
				for (int r = 0; r <= 15; r++) {
					a[r] = b[p][r];
					cout << a[r];
				}
				cout << ' ';
				del();
				cout << '\n';
			}
			fclose(in);
			fclose(out);
			exit(0);
		}
	}
}
int main(){
	in = freopen("in.txt", "r", stdin);
	out = freopen("out.txt", "w", stdout);
	int t = 1;
	a[0] = 1;
	a[15] = 1;
	gen(1,15);
	for (int i = 0; i < 10; i++);
	fclose(in);
	fclose(out);
	return 0;
}