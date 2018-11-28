#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define maxn 100000000

long long ans[11];

long long get (long long num, long long base) {//把10进制的num转化成base进制
	long long ans = 0, cur = 1;
	while (num) {
		ans += (num&1)*cur;
		num >>= 1;
		cur *= base;
	}
	return ans;
}

bool ok (long long num, int base) {//判断十进制num在base进制下是不是素数
	if (num%2 == 0) //末尾是1 
		return 0;
	//cout << num << " " << base << endl;
	num = get (num, base);// cout << num << endl;
	for (long long i = 2; i*i <= num; i++) {
		if (num%i == 0) {
			ans[base] = i;
			return 1;
		}
	}
	return 0;
}
int bit[222];
long long n, tot;

int main () {
	freopen ("in", "r", stdin);
	freopen ("out", "w", stdout);
	int t, kase = 0;
	//init (); //cout << ".." << endl;
	scanf ("%d", &t);
	while (t--) {
		cin >> n >> tot;
		printf ("Case #%d:\n", ++kase);
		int cnt = 0;
		long long num, l;
		for (long long i = (1<<(n-1)); i < (1<<n); i++) {// cout << "i:" << i << endl;
			for (int base = 2; base <= 10; base++) {
				if (!ok (i, base))
					goto out;
			}
			cnt++;
			num = i, l = 0;
			memset (bit, 0, sizeof bit);
			while (num) {
				bit[l++] = (num&1);
				num >>= 1;
			}
			while (l--) {
				cout << bit[l];
			} cout << " ";
			for (int j = 2; j <= 10; j++) cout << ans[j] << (j == 10 ? '\n' : ' ');
			if (tot == cnt)
				break;
			out: ;
		}
	}
	return 0;
}