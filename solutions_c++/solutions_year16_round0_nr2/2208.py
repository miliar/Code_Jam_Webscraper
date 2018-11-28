#include <stdio.h>
#include <vector>
#include <stdlib.h>
#include <string.h>
#include <cmath>

using namespace std;

vector<int> pa, pb;

int T;
char S[200];

int solve(vector<int> &p)
{
	int res = 0;
	for (int i = 0; i < int(p.size()); i++) {
		if (p[i] == 0 && i != (int(p.size()) -1))
			res += 1;
		else if (p[i] == 1)
			res += 1;
	}
	return res;
}

int main()
{
	scanf(" %d", &T);
	gets(S);
	for (int cas = 1; cas <= T; cas++) {
		pa.clear();
		pb.clear();
		gets(S);
		int len = strlen(S);
		for (int i = 0; i < len; i++) {
			int a = (S[i] == '+') ? 0 : 1;
			int b = (S[i] == '-') ? 0 : 1;

			if (int(pa.size()) == 0 || pa[int(pa.size())-1] != a)
				pa.push_back(a);
			if (int(pb.size()) == 0 || pb[int(pb.size())-1] != b)
				pb.push_back(b);
		}

		int res_a = solve(pa);
		int res_b = solve(pb) + 1;
		printf("Case #%d: %d\n", cas, min(res_a, res_b));
	}

	return 0;
}