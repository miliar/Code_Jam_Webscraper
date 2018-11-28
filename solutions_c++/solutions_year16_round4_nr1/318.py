#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
using namespace std;

string s[3][13], t1, t2;
int num[3][13][3], z[256], num_case, n, a, b, c;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	s[0][0] = 'P';
	s[1][0] = 'R';
	s[2][0] = 'S';
	z['P'] = 0;
	z['R'] = 1;
	z['S'] = 2;
	for (int i = 1; i <= 12; i++)
	{
		t1 = s[0][i - 1] + s[1][i - 1];
		t2 = s[1][i - 1] + s[0][i - 1];
		if (t1 < t2) s[0][i] = t1;
		else s[0][i] = t2;
		
		t1 = s[1][i - 1] + s[2][i - 1];
		t2 = s[2][i - 1] + s[1][i - 1];
		if (t1 < t2) s[1][i] = t1;
		else s[1][i] = t2;
		
		t1 = s[2][i - 1] + s[0][i - 1];
		t2 = s[0][i - 1] + s[2][i - 1];
		if (t1 < t2) s[2][i] = t1;
		else s[2][i] = t2;
	}
	for (int i = 0; i < 3; i++)
		for (int j = 0; j <= 12; j++)
		{
			for (int k = 0; k < s[i][j].size(); k++)
				num[i][j][z[s[i][j][k]]]++;
		}
	scanf("%d", &num_case);
	for (int icase = 1; icase <= num_case; icase++)
	{
		scanf("%d %d %d %d", &n, &b, &a, &c);
		/*
		printf("%d %d %d\n", a, b, c);
		printf("%d %d %d\n", num[0][n][0], num[0][n][1], num[0][n][2]);
		printf("%d %d %d\n", num[1][n][0], num[1][n][1], num[1][n][2]);
		printf("%d %d %d\n", num[2][n][0], num[2][n][1], num[2][n][2]);
		*/
		printf("Case #%d: ", icase);
		if (num[0][n][0] == a && num[0][n][1] == b && num[0][n][2] == c)
		{
			cout << s[0][n] << endl;
			continue;
		}
		if (num[1][n][0] == a && num[1][n][1] == b && num[1][n][2] == c)
		{
			cout << s[1][n] << endl;
			continue;
		}
		if (num[2][n][0] == a && num[2][n][1] == b && num[2][n][2] == c)
		{
			cout << s[2][n] << endl;
			continue;
		}
		printf("IMPOSSIBLE\n");
	}
	return 0;
}
