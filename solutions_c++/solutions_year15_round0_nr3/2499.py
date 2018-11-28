#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
using namespace std;

int T;
int count;
int L;
int X;
char str[10010];
char temp[10010];
int len;

char map[400][400];
int map1[400][400];
int dp1[10010][10010];
char dp[10010][10010];

char quat(int s, int e) {
	
	char res = dp[s][e];
	int flag = dp1[s][e];
	if (flag == -1)
		return 1;
	return res;
}

int main() {

	freopen("C:\\Users\\wzh22014\\Downloads\\C-small-attempt1.in", "r", stdin);
	freopen("C.out", "w", stdout);

	scanf("%d", &T);
	
	map['1']['1'] = '1';
	map['1']['i'] = 'i';
	map['1']['j'] = 'j';
	map['1']['k'] = 'k';
	
	map['i']['1'] = 'i';
	map['i']['i'] = '1';
	map['i']['j'] = 'k';
	map['i']['k'] = 'j';

	map['j']['1'] = 'j';
	map['j']['i'] = 'k';
	map['j']['j'] = '1';
	map['j']['k'] = 'i';

	map['k']['1'] = 'k';
	map['k']['i'] = 'j';
	map['k']['j'] = 'i';
	map['k']['k'] = '1';

	map1['1']['1'] = 1;
	map1['1']['i'] = 1;
	map1['1']['j'] = 1;
	map1['1']['k'] = 1;

	map1['i']['1'] = 1;
	map1['i']['i'] = -1;
	map1['i']['j'] = 1;
	map1['i']['k'] = -1;

	map1['j']['1'] = 1;
	map1['j']['i'] = -1;
	map1['j']['j'] = -1;
	map1['j']['k'] = 1;

	map1['k']['1'] = 1;
	map1['k']['i'] = 1;
	map1['k']['j'] = -1;
	map1['k']['k'] = -1;

	while (T--) {
		count++;
		scanf("%d %d", &L, &X);
		scanf("%s", str);
		len = X*L;
		for (int i = 0; i < X; i++) {
			strcpy(temp + L*i, str);
		}
		int flag = 0;
		for (int i = 0; i < len; i++) {
			dp[i][i] = temp[i];
			dp1[i][i] = 1;
		}
		for (int i = 2; i <= len; i++) {
			for (int j = 0; j < len; j++) {
				if (j + i - 1 >= len)
					break;
				dp[j][j + i - 1] = map[dp[j][j + i - 2]][temp[j + i - 1]];
				dp1[j][j + i - 1] = map1[dp[j][j + i - 2]][temp[j + i - 1]] * dp1[j][j + i - 2];
			}
		}
		for (int i = 1; i <= len - 2; i++) {
			char a = quat(0, i - 1);
			if (a != 'i')
				continue;
			for (int j = 1; j <= len - i - 1; j++) {
				char b = quat(i, i + j - 1);
				char c = quat(i + j, len - 1);
				if ( (b == 'j') && (c == 'k')) {
					flag = 1;
					break;
				}
			}
			if (flag == 1)
				break;
			
		}

		printf("Case #%d: ", count);
		if (flag == 1) {
			printf("YES\n");
		}
		else printf("NO\n");
	}

	return 0;
}