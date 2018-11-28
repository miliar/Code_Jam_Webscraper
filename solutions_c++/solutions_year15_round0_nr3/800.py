#include <bits/stdc++.h>
using namespace std;

char str[11111];

int a[2222222];

const int MULTIPLY[4][4] = {
{0, 1, 2, 3},
{1, 4, 3, 6},
{2, 7, 4, 1},
{3, 2, 5, 4}
						 };

int mul(int a, int b) {

	int sig = 1;

	if (a >= 4) a -= 4, sig *= -1;
	if (b >= 4) b -= 4, sig *= -1;

	int x = MULTIPLY[a][b];
	if (x >= 4) x -= 4, sig *= -1;
	if (sig == -1) x += 4;

	return x;

}

int change(char x) {
	if (x == '1') return 0;
	if (x == 'i') return 1;
	if (x == 'j') return 2;
	if (x == 'k') return 3;
	return -1;
}

int main(void) {

	int cases; scanf("%d", &cases);
	
	int cas = 0;
	
	while (cases--) {
	
		printf("Case #%d: ", ++cas);
		
		
		int N;
		long long X;
		scanf("%d %lld", &N, &X);
		
		if (X > 16) {
			X = (X % 4 + 16);
		}
	
		scanf("%s", str);
		string s = "";
		
		for (int t = 0; t < X; ++t) {
			s += str;
		}
	
		int left = -1;
		int right = -1;
		for (int i = 0, now = 0; i < s.size(); ++i) {
		
			int x = change(s[i]);
			now = mul(now, x);
		
			if (now == 1) {
				left = i;
				break;
			}
		
		}
		
		if (left == -1) {
			puts("NO");
			continue;
		}
	
		for (int i = left+1, now = 0; i < s.size(); ++i) {
			
			int x = change(s[i]);
			now = mul(now, x);
			
			if (now == 2) {
				right = i;
				break;
			}
			
		}
		if (right == -1) {
			puts("NO");
			continue;
		}
	
	
		int now = 0;
		for (int i = right+1; i < s.size(); ++i) {
			int x = change(s[i]);
			now = mul(now, x);
		}
		
		if (now == 3) {
			puts("YES");
		} else {
			puts("NO");
		}
		
	}



	return 0;
}
