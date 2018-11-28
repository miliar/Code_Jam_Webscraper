#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

int T, N;
int p, r, s;

string res[20][3];
int p_res[20][3];
int r_res[20][3];
int s_res[20][3];

void build()
{
	res[0][0] = 'P';
	res[0][1] = 'R';
	res[0][2] = 'S';
	p_res[0][0] = 1;
	r_res[0][0] = 0;
	s_res[0][0] = 0;
	p_res[0][1] = 0;
	r_res[0][1] = 1;
	s_res[0][1] = 0;
	p_res[0][2] = 0;
	r_res[0][2] = 0;
	s_res[0][2] = 1;

	for (int i = 1; i <= 15; i++) {
		res[i][0] = res[i-1][0] + res[i-1][1];
		res[i][1] = res[i-1][0] + res[i-1][2];
		res[i][2] = res[i-1][1] + res[i-1][2];

		p_res[i][0] = p_res[i-1][0] + p_res[i-1][1];
		p_res[i][1] = p_res[i-1][0] + p_res[i-1][2];
		p_res[i][2] = p_res[i-1][1] + p_res[i-1][2];

		r_res[i][0] = r_res[i-1][0] + r_res[i-1][1];
		r_res[i][1] = r_res[i-1][0] + r_res[i-1][2];
		r_res[i][2] = r_res[i-1][1] + r_res[i-1][2];

		s_res[i][0] = s_res[i-1][0] + s_res[i-1][1];
		s_res[i][1] = s_res[i-1][0] + s_res[i-1][2];
		s_res[i][2] = s_res[i-1][1] + s_res[i-1][2];
	}
}

string solve()
{
	for (int i = 0; i < 3; i++) {
		if (p == p_res[N][i] && r == r_res[N][i] && s == s_res[N][i])
			return res[N][i];
	}
	return "IMPOSSIBLE";
}

int main()
{
	build();
	scanf(" %d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf(" %d %d %d %d", &N, &r, &p, &s);
		printf("Case #%d: ", cas);
		cout << solve() << endl;
	}

	return 0;
}
