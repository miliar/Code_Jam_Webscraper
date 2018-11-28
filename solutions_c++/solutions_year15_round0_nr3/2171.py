#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

const int mult[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};
const int dive[9][9] = {{1,2,-3,4,-2,-4,3,-2,-1},
						{-2,1,4,3,0,-3,-4,-1,2},
						{3,-4,1,2,-4,-2,-1,4,-3},
						{-4,-3,-2,1,0,-1,2,3,4},
						{0,0,0,0,-1,0,0,0,0},
						{4,3,2,-1,0,1,-2,-3,-4},
						{-3,4,-1,-2,0,2,1,-4,3},
						{2,-1,-4,-3,-3,3,4,1,-2},
						{-1,-2,3,-4,0,4,-3,2,1}};
const int MAXL = 10005;

int T, X, L;
char s[MAXL];
int num[MAXL], l[MAXL], r[MAXL], total[5];

bool ans;

int mul(int aa, int bb) {
	return mult[abs(aa) - 1][abs(bb) - 1] * (aa * bb > 0 ? 1 : -1);
}
int dii(int aa, int bb) {
	return dive[aa + 4][bb + 4];
}
bool work() {
	for (int i = 0; i < 4; i ++)
		for (int j = 0; j < 4; j++) {
			if (i + j + 2 > X) break;
			int k = (X - i - j - 2) % 4;
			for (int pi = 0; pi < L; pi ++)
				if (i + pi > 0 && mul(total[i], l[pi]) == 2)
					for (int pk = 0; pk < L; pk ++)
						if (k + pk > 0 && mul(r[pk], total[k]) == 4)
							if (mul(mul(r[L - pi], total[j]), l[L - pk]) == 3) return true;
		}
	for (int i = 0; i < 4; i++) {
		if (i >= X) break;
		int k = (X - i - 1) % 4;
		for (int pi = 0; pi < L; pi ++)
			if (i + pi > 0 && mul(total[i], l[pi]) == 2)
				for (int pk = 0; pk < L; pk ++)
					if (k + pk > 0 && mul(r[pk], total[k]) == 4)
						if (L - pi - pk > 0 && dii(r[L-pi], r[pk]) == 3) return true;
	}
	return false;
}
int main(int argc, char** argv) {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	scanf("%d", &T);
	for (int times = 1; times <= T; times ++) {
		printf("Case #%d: ", times);
		scanf("%d%d", &L, &X);
		gets(s); gets(s);

		for (int i=0; i<L; i++)
			if (s[i] == '1') num[i] = 1;
			else if (s[i] == 'i') num[i] = 2;
			else if (s[i] == 'j') num[i] = 3;
			else if (s[i] == 'k') num[i] = 4;
		l[0] = 1; r[0] = 1;
		for (int i = 1; i <= L; i ++) {
			l[i] = mul(l[i-1], num[i-1]);
			r[i] = mul(num[L-i], r[i-1]);
		}
		total[0] = 1;
		for (int i = 1; i < 4; i ++) total[i] = mul(total[i-1], l[L]);
		
		ans = work();
		printf(ans ? "YES\n" : "NO\n");
	}
	return 0;
}

