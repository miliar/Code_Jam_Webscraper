#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const int Maxd = 3;
const int add[Maxd][2] = {{0, 1}, {1, 2}, {0, 2}};
const string chr = "PRS";

int t;
int n;
int has[Maxd], got[Maxd];

string Get(int n, int cur)
{
	if (n == 0) return string(1, chr[cur]);
	else {
		string a = Get(n - 1, add[cur][0]);
		string b = Get(n - 1, add[cur][1]);
		if (a <= b) return a + b;
		return b + a;
	}
}

bool Check(const string &s)
{
	fill(got, got + Maxd, 0);
	for (int i = 0; i < s.length(); i++)
		got[chr.find(s[i])]++;
	for (int i = 0; i < Maxd; i++)
		if (has[i] != got[i]) return false;
	return true;
}

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d %d %d", &n, &has[1], &has[0], &has[2]);
		vector <string> V;
		for (int i = 0; i < Maxd; i++) {
			string s = Get(n, i);
			if (Check(s)) V.push_back(s);
		}
		printf("Case #%d: ", tc);
		if (V.empty()) printf("IMPOSSIBLE\n");
		else {
			sort(V.begin(), V.end());
			printf("%s\n", V[0].c_str());
		}
	}
	return 0;
}