#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<stdint.h>
using namespace std;

const long long size = 10000ll;
const long long mod = 1000000ll;
const long long mod2 = 1000000000000ll;
int t;
long long L[20000010], lcnt, a, b;

char str[40];
char str1[40];
bool IsSquare (long long num) {
	long long a = num % mod, b = num / mod;
	
	long long p1 = a * a;
	long long p2 = a * b;
	long long h1 = p1 + p2 * 2 * mod;
	long long h2 = b * b + h1 / mod2;
	h1 %= mod2;
	
	sprintf (str1, "%lld", h1);
	if (h2 != 0) {
		for (int i = 11, len = strlen (str1); i >= 0; i --)
			if (len-1-i >= 0)
				str1[i] = str1[len-1+i-11];
			else
				str1[i] = '0';
		str1[12] = 0;
		sprintf (str, "%lld%s", h2, str1);
	} else {
		sprintf (str, "%s", str1);
	}
	
	//if (strlen (str) < 6)
	//	printf ("%s\n", str);
	
	for (int i = 0, len = strlen (str); 2 * i < len; i ++)
		if (str[i] != str[len-i-1])
			return false;
	return true;	
}

void test (long long num) {
	sprintf (str, "%lld", num);
	int len = strlen (str);
	str[2 * len] = 0;
	for (int i = 0; i < len; i ++) {
		str[2 * len - i - 1] = str[i];
	}
	long long num1;
	sscanf (str, "%lld", &num1);
	for (int i = 0; i < len; i ++) {
		str[2 * len - i - 2] = str[i];
	}
	str[2 * len - 1] = 0;
	long long num2;
	sscanf (str, "%lld", &num2);
	
	if (IsSquare (num1))
		L[lcnt ++] = num1 * num1;
	if (IsSquare (num2))
		L[lcnt ++] = num2 * num2;
		
}

int main() {

	for (long long i = 1; i < size; i ++) {
		test (i);
	}
	
	sort (L, L + lcnt);
	
//	for (int i = 0; i < lcnt; i ++)
//		printf ("%lld ", L[i]);

	scanf ("%d", &t);
	int caze = 0;
	while (t --) {
		caze ++;
		
		int ans = 0;
		scanf ("%lld%lld", &a, &b);
		for (int i = 0; i < lcnt; i ++)
			if (L[i] >= a and L[i] <= b)
				ans ++;
		printf ("Case #%d: %d\n", caze, ans);
	}
	return 0;
}
