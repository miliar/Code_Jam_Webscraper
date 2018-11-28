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
class Result {
public:
	virtual LL myPow(LL a, LL n) const = 0;
	virtual int check(LL val) const = 0;
	
};
class Small: public Result {
public:
	virtual LL myPow(LL a, LL n) const {
		 return powl(a, n);
	 }
	virtual int check(LL val) const {
		if (val % 2 == 0)
			return -1;
		 for (int i = 3; i * i <= val; i+=2) {
			 if (val % i == 0) {
				 return i;
			 }
			 if (i >= 10000 ) {
				 break;
			 }
		 }
		 return -1;
	 }
 };
class Large: public Result {
public:
	int mod = 100;
	virtual LL myPow(LL a, LL n) const {
		if (n == 0)
			return 1;
		if (n % 2 == 0) {
			return myPow(a * a % mod, n / 2);
		}
		else {
			return a * myPow(a, n - 1) % mod;
		}
	}
	virtual int check(LL val) const {
		/*if (val % 2 == 0)
			return 2;*/
		if (val % 5 == 0 && val % 2 != 0)
			return 5;
		return -1;
	}
};
LL getDiv(int val, int digit, Result *res) {
	LL nVal = 0;
	for (int i = 0; i <= 31; i++) {
		if (val & (1 << i)) {
			nVal += res->myPow(digit, i);
		}
	}
	return res->check(nVal);

}
void printNumber(int val, int len) {
	for (int i = len; i >= 0; i--) {
		printf("%d", (val & (1 << i)) != 0);
	}
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d",&t);
	int numberTest = 1;
	while (t--) {
		int n, j;
		scanf("%d%d", &n, &j);
		n--;
		printf("Case #%d:\n", numberTest++);
		int val = 1 << n;
		Result *res;
		if (n <= 15) {
			res = new Small();
		}
		else {
			res = new Large();
		}
		
		for (int i = val; j > 0; i++) {
			vector<LL> divs;
			for (int k = 2; k <= 10; k++) {
				int div = getDiv(i,k,res);
				if (div != -1) {
					divs.push_back(div);
				}
			}
			if (divs.size() == 9) {
				j--;
				printNumber(i, n);
				for (int k = 0; k < divs.size(); k++) {
					printf(" %lld", divs[k]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}