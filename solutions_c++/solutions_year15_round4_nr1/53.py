#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<ctime>
#include<map>
#include<string>
#include<vector>
#include<set>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define Fill(a,b) memset(a,b,sizeof(a))
#define FI first
#define SE second
#define MP make_pair
#define PII pair<int,int>
#define flt double
#define INF (0x3f3f3f3f)
#define MaxN 1020304
#define MaxNode 1020304
#define MD 1000000007

long long getLL() {
	long long ret = 0;
	char c;
	while (1) {
		c = getchar();
		if (c >= '0' && c <= '9') break ;
	}
	while (1) {
		ret = ret * 10 + c - '0';
		c = getchar();
		if (c < '0' || c > '9') break ;
	}
	return ret;
}

int getInt() {
	int ret = 0;
	char c;
	while (1) {
		c = getchar();
		if (c >= '0' && c <= '9') break ;
	}
	while (1) {
		ret = ret * 10 + c - '0';
		c = getchar();
		if (c < '0' || c > '9') break ;
	}
	return ret;
}

const int px[] = {1,0,-1,0};
const int py[] = {0,1,0,-1};

int R, C;
char A[233][233];
int main() {
	//freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		cin >> R >> C;
		For(i,1,R) scanf("%s", A[i] + 1);
		int ans = 0;
		For(i,1,R) For(j,1,C) if (A[i][j] != '.') {
			char c = A[i][j];
			int dx = 0, dy = 0;
			if (c == '^') {
				dx = -1; dy = 0;
			}
			if (c == '>') {
				dx = 0; dy = 1;
			}
			if (c == '<') {
				dx = 0; dy = -1;
			}
			if (c == 'v') {
				dx = 1; dy = 0;
			}
			int cx = i + dx, cy = j + dy;
			bool fl = false ;
			while (1 <= cx && cx <= R && 1 <= cy && cy <= C) {
				if (A[cx][cy] != '.') {
					fl = true; break ;
				}
				cx += dx; cy += dy;
			}
			if (fl) continue ;
			++ans;
			fl = false ;
			For(p,0,3) {
				cx = i + px[p], cy = j + py[p];
				while (1 <= cx && cx <= R && 1 <= cy && cy <= C) {
					if (A[cx][cy] != '.') {
						fl = true; break ;
					}
					cx += px[p]; cy += py[p];
				}
				if (fl) break ;		 
			}
			if (!fl) ans = INF;
		}
		if (ans >= INF) puts("IMPOSSIBLE");
		else cout << ans << endl;
	}
	return 0;
}

