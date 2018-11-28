#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

long long compute(char str[], int length, int n) {
	if (length < n) return 0;
	int i = length - 1;
	long long v = 0;
	long long t = -1;
	long long s = 0;
	while (i >= 0) {
		while (str[i] != 'a' && str[i] != 'e' 
			&& str[i] != 'i' && str[i] != 'o' && str[i] != 'u' && i >= 0) {
			v++;
			i--;
		}
		if (v >= n) {
			t = i;
			s = v;
			break;
		}
		v = 0;
		i--;
	}		
	//printf("%d\n", v);
	//printf("%d\n", t);
	long long result = t + 1;
	if (s >= n) result += s - n + 1;
	//printf("%lld %lld %d %lld\n", s, t, n, result);
	return result + compute(str, length - 1, n);
}
int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		char str[1000000];
		int nValue;
		scanf("%s %d", &str, &nValue);
		//printf("%d\n", nValue);
		printf("Case #%d: %lld\n", i, compute(str, strlen(str), nValue));
	}
	return 0;
}