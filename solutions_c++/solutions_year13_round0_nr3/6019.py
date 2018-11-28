#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <sstream>

using namespace std;
#define LL long long int
inline void inp2(int *n) {
	register char c = 0;
	*n = 0;

	while (c < 33)
		c = getchar_unlocked();

	while (c > 33) {
		*n = *n * 10 + c - '0';
		c = getchar_unlocked();
	}
}

bool isPalin(char *num) {
	int len = strlen(num);
	for (int i = 0, j = len - 1; i < len / 2; ++i, --j) {
		if (num[i] != num[j])
			return false;
	}
	return true;
}

bool isPalin(LL n) {
	char num[15];
	sprintf(num, "%lld", n);
	return isPalin(num);
}

set<LL> pals;
void generatePalindrome(LL n) {

	if(isPalin(n) && isPalin(n*n)){
		pals.insert(n*n);
	}
	char num[15], reversed[30], reversed2[30];
	sprintf(num, "%lld", n);

	int i, j, k, len = strlen(num);
	//cout << len;

	for (i = 0; i < len; ++i) {
		reversed[i] = num[i];
		reversed2[i] = num[i];
	}

	k = i;
	// exact mirror, 12 - 1221
	for (j = strlen(num) - 1; j >= 0; --j) {
		reversed2[k++] = num[j];
	}
	reversed2[k] = '\0';

	// one less mirror, 12 - 121
	for (j = strlen(num) - 2; j >= 0; --j) {
		reversed[i++] = num[j];
	}
	reversed[i] = '\0';

	LL a = atoll(reversed), b = atoll(reversed2);
	a *= a;
	b *= b;
	if (isPalin(a))
		pals.insert(a);
	if (isPalin(b))
		pals.insert(b);
//	cout << reversed << endl;
//	cout << reversed2 << endl;

}

int _MAIN() {
	int T, N, i, j, k, l;
	inp2(&T);
	//T = 1;
	N = 0;

	pals.insert(1);
	pals.insert(4);
	pals.insert(9);
	pals.insert(121);

	for (i = 10; i < 10000; ++i) {
		generatePalindrome(i);
	}

	set<LL>::iterator it;

//	for (it = pals.begin(); it != pals.end(); it++) {
//		cout << *it << "," << endl;
//	}

	while (T-- > 0) {
		N++;
		int low, high;
		inp2(&low);
		//getchar_unlocked();
		inp2(&high);

		it = pals.begin();
		while (*it < low)
			it++;

		j = 0;
		while (*it <= high) {
			j++;
			it++;
		}
		//cout << *it;
		printf("Case #%d: %d\n", N, j);
		//getchar_unlocked(); //eat \n
	}

	//cout << "Total " << pals.size() << endl;

	return 0;
}

int main() {
//	generatePalindrome(12);
//	return 0;

	return _MAIN();
}
