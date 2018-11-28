#pragma comment(linker, "/STACK:134217728")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <complex>
#include <functional>
#include <cmath>
#include <time.h>

using namespace std;

typedef long long LL;

int base = 10;

void printNumber(vector<int> digit) {
	reverse(digit.begin(), digit.end());
	for (int i = 0; i < digit.size(); i++) {
		printf("%d", digit[i]);
	}
}



vector<int> generateDigit(int n) {
	vector<int> answer;
	while (n) {
		int digit = n % 10;
		answer.push_back(digit);
		n /= 10;
	}
	return answer;
}

vector<int> mul(vector<int>  digit, int val) {
	int carry = 0;
	for (int i = 0; i < digit.size() || carry; i++) {
		if (digit.size() == i)
			digit.push_back(0);
		LL cur = digit[i] * val + carry;
		digit[i] = cur % base;
		carry = cur / base;
	}
	while (digit.size() > 1 && digit.back() == 0)
		digit.pop_back();
	return digit;
}
vector<int> calc(vector<int> digit) {
	set<int> s;

	for (int i = 1;; i++) {
		vector<int> res = mul(digit, i);
		for (int j = 0; j < res.size(); j++) {
			s.insert(res[j]);
		}
		if (s.size() == 10) {
			return res;
		}
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d",&t);
	int numberTest = 1;
	while (t--) {
		int n;
		scanf("%d",&n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", numberTest++);
		}
		else {
			vector<int> res = calc(generateDigit(n));
			printf("Case #%d: ",numberTest++);
			printNumber(res);
			printf("\n");
		}
	}
	return 0;
}