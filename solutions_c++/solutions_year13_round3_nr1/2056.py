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

long long compute_(char str[], int length, int n) {
	long long output = 0;
	if (length >= n) {
		int i = 0;
		long long oldV = 0;
		int oldJ = 0;
		for (int i = n - 1; i <= length - 1; i++) {
			int j = i;
			long long v = 0;
			//long long t = -1;
			//long long s = 0;
			while (j >= 0 && str[j] != 'a' && str[j] != 'e' 
					&& str[j] != 'i' && str[j] != 'o' && str[j] != 'u') {
				v++;
				j--;
			}
			if (v >= n) {
				output += j + 1 + v - n + 1;
				oldV = v;
				oldJ = j;
			} else {
				if (oldV >= n) output += oldJ + 1 + oldV - n + 1;
			}
			
		}
	}
	
	return output;
}
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
		//printf("%d\n", n);
		scanf("%s %d", &str, &nValue);
		//printf("%d\n", nValue);
		
		
		printf("Case #%d: %lld\n", i, compute_(str, strlen(str), nValue));
	}
	return 0;
}