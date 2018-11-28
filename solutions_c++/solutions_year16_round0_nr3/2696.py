#include <iostream> 
#include <fstream>
#include <vector>
#include <queue>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <functional>
#include "stdlib.h" 
#include "time.h"
#include <set>
#include <map>
#include <numeric>

#define INF 800
using namespace std;
#define LL long long


LL baseparse(LL ori, int base) {
	LL exp = 1;
	LL result10 = 0;
	while (ori) {
		result10 += (ori % base) * exp;
		exp *= base;
		ori /= base;
	}
	return result10;
}
LL bitparse(LL ori2As10, int base) {
	LL exp = 1;
	LL result10 = 0;
	while (ori2As10) {
		result10 += (ori2As10 % 2) * exp;
		exp *= base;
		ori2As10 /= 2;
	}
	return result10;
}
string bitstr(LL ori2As10, LL length) {
	string r(length,'0');
	for (LL i = length - 1; i >= 0; i--)
	{
		r[i] = '0' + ori2As10 % 2;
		ori2As10 /= 2;
	}
	return r;
}
LL strparse(string ori, int base) {
	LL exp = 1;
	LL result10 = 0;
	for (LL i = ori.size() - 1; i >= 0; i--)
	{
		result10 += ori[i] * exp;
		exp *= base;
	}
	return result10;
}
LL finddiv(LL tofind) {
	LL maxf = (int)((double)sqrt(tofind) + 1);
	for (LL i = 2; i < maxf; i++)
	{
		if (tofind % i == 0)
		{
			return i;
		}
	}
	return -1;
}

LL isprime() {
	return 0;
}

LL numgen(LL x, LL length) {
	return (1 << (length - 1)) + (x << 1) + 1;
}

int main() {
#ifdef __ACM
	ifstream fin("C-small-attempt0.in");	streambuf *cinbackup;  	cinbackup = cin.rdbuf(fin.rdbuf());
#endif
	int cas = 1;
	int T;
	cin >> T;
	while (T--) {
		LL divs[11];
		LL N, J;
		cin >> N >> J;
		cout << "Case #" << cas << ": " << endl;
		LL x = 0;
		while (J) {
			LL current2as10 = numgen(x, N);
			memset(divs, 0, sizeof(LL) * 11);
			for (int i = 2; i <= 10; i++) {
				LL currentasbase = bitparse(current2as10, i);
				divs[i] = finddiv(currentasbase);
				if (divs[i] == -1)
					goto FAIL;
			}
			J--;
			cout << bitstr(current2as10, N) ;
			for (int i = 2; i <= 10; i++) {
				cout << " " << divs[i];
			}
			cout << endl;
			FAIL:
			x++;
		}
		cas++;
	}
#ifdef __ACM
	system("pause");
#endif
}

