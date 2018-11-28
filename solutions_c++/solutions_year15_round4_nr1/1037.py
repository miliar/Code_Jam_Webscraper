#include <bits/stdc++.h>

using namespace std;

const int N = 100 + 10;

int r, c;
char s[N][N];

bool check(int i, int j, char c2) {
	if(c2 == '.')	return true;
	if(c2 == '<')
		for(int k = j-1; k >= 0; k--)
			if(s[i][k] != '.')	return true;
	if(c2 == '^')
		for(int k = i-1; k >= 0; k--)
			if(s[k][j] != '.')	return true;
	if(c2 == '>')
		for(int k = j+1; k < c; k++)
			if(s[i][k] != '.')	return true;
	if(c2 == 'v')
		for(int k = i+1; k < r; k++)
			if(s[k][j] != '.')	return true;
	return false;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int kase = 1; kase <= t; kase++) {
		scanf("%d%d", &r, &c);
		for(int i = 0; i < r; i++)	scanf("%s", s[i]);

		bool GG = false;
		int ans = 0;
		for(int i = 0; i < r && !GG; i++) {
			for(int j = 0; j < c && !GG; j++) {
				char tmp = s[i][j];
				if(check(i, j, tmp))	continue;

				bool flag = false;
				ans++;
				// <<<
				for(int k = j-1; k >= 0; k--)
					if(s[i][k] != '.')	flag = true;
				// ^^^
				for(int k = i-1; k >= 0; k--)
					if(s[k][j] != '.')	flag = true;
				// >>>
				for(int k = j+1; k < c; k++)
					if(s[i][k] != '.')	flag = true;
				// vvv
				for(int k = i+1; k < r; k++)
					if(s[k][j] != '.')	flag = true;

				if(!flag)	GG = true;
			}
		}


		if(!GG)	printf("Case #%d: %d\n", kase, ans);
		else	printf("Case #%d: IMPOSSIBLE\n", kase);
	}
}
