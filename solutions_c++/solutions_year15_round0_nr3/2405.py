#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<queue>
#include<map>
#include<iostream>
#include<algorithm>
using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

const int maxn = 10005;
const int mod = (int)1e9 + 7;

char s[maxn];
int l;
LL x;
int mat[8][8] = { 0, 1, 2, 3, 4, 5, 6, 7,
1, 4, 3, 6, 5, 0, 7, 2,
2, 7, 4, 1, 6, 3, 0, 5,
3, 2, 5, 4, 7, 6, 1, 0,
4, 5, 6, 7, 0, 1, 2, 3,
5, 0, 7, 2, 1, 4, 3, 6,
6, 3, 0, 5, 2, 7, 4, 1,
7, 6, 1, 0, 3, 2, 5, 4 };
int val[maxn], col[maxn][10], len[maxn];
int flag[10];
PII cir[maxn];
bool mark[maxn];

int getIndex(char ch){
	if (ch == 'i') return 1;
	else if (ch == 'j') return 2;
	return 3;
}

bool judge(int vv){
	if (vv == 0) return false;
	if (vv == 4) return x % 2 == 1;
	return x % 2 == 0 && (x >> 1) % 2 == 1;
}

int main(){
	ios::sync_with_stdio(false);
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT){
		cin >> l >> x >> (s + 1);
		val[0] = 0;
		for (int i = 1; i <= l; ++i){
			val[i] = mat[val[i - 1]][getIndex(s[i])];
		}
		if (!judge(val[l])){
			printf("Case #%d: NO\n", TT);
			continue;
		}
		for (int i = 1; i <= l; ++i){
			len[i] = 1;
			col[i][0] = val[i];
		}
		int rc = val[l];
		memset(mark, 0, sizeof(mark));
		for (int i = 1; i <= l; ++i){
			memset(flag, -1, sizeof(flag));
			flag[0] = 0;
			while (len[i] < x){
				col[i][len[i]] = mat[rc][col[i][len[i]-1]];
				if (flag[col[i][len[i]]] != -1){
					cir[i] = PII(flag[col[i][len[i]]], len[i] - flag[col[i][len[i]]]);
					mark[i] = true;
					break;
				}
				flag[col[i][len[i]]] = len[i];
				len[i]++;
			}
		}
		LL fir = 1ll << 50;
		for (int i = 1; i <= l; ++i){
			for (int j = 0; j < len[i]; ++j){
				if (col[i][j] == 1){
					fir = min(fir, 1ll * l*j + i);
					break;
				}
			}
		}
		if (fir == (1ll << 50)){
			printf("Case #%d: NO\n", TT);
			continue;
		}
		LL sec = -1, c;
		for (int i = 1; i <= l; ++i){
			for (int j = 0; j < len[i]; ++j){
				if (col[i][j] == 3){
					if (mark[i] && j >= cir[i].first) c = j + (x - 1 - j) / cir[i].second*cir[i].second;
					else c = j;
					sec = max(sec, c*l + i);
				}
			}
		}
//		printf("%lld %lld\n", fir, sec);
		if (sec <= fir){
			printf("Case #%d: NO\n", TT);
		}
		else printf("Case #%d: YES\n", TT);
	}
	return 0;
}