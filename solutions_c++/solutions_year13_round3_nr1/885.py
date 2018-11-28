#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int T, n, N;
char str[1000100];
int voice[255];
int end[1000100], cons[1000100];

void solve(int t) {
	scanf("%s %d\n", str, &n);
	N = strlen(str);
	for (int i = 0 ; i <= n ; i++) {
		end[i] = 0;
		cons[i] = 0;
	}
	if (voice[str[0]]) 
		cons[0] = 1;
	if (cons[0] >= n) {
		end[0] ++;
	}
	for (int i = 1 ; i < N ; i ++) {
		if (voice[str[i]])
			cons[i] = cons[i-1] + 1;
		else 
			cons[i] = 0;
		if (cons[i] >= n) {
			end[i] = i + 2 - n;
		} else {
			end[i] = end[i-1];
		}
	}
	//for (int i = 0 ; i < N ; i ++)
		//printf("%d ", end[i]);
	long long res = 0;
	for (int i = 0 ; i < N ; i ++)
		res += end[i];
	printf("Case #%d: %lld\n", t, res);

	
}


int main() {
	string vow = "aeiou";
	for (int i = 0 ; i < 26 ; i ++) {
		char c = 'a' + i;
		if (vow.find(c) < vow.length())
			voice[c] = 0;
		else
			voice[c] = 1; // consonant
	}
	scanf("%d\n", &T);
	for (int i = 1 ; i <= T; i ++) solve(i);
	
	return 0;
}