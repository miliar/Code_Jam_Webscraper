#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
using namespace std;

const int Maxn = 5005;

int T;
int n;
string s;
map <string, int> M;
int arein[Maxn];
int res;

int getInd(const string &s)
{
	if (M.find(s) == M.end()) {
		int cur = M.size();
		arein[cur] = 0;
		M[s] = cur;
	}
	return M[s];
}

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d", &n); getline(cin, s);
		M.clear();
		for (int i = 0; i < n; i++) {
			getline(cin, s);
			stringstream ss(s);
			while (ss >> s) arein[getInd(s)] |= 1 << i;
		}
		res = Maxn;
		int mut = 0;
		vector <int> V;
		for (int i = 0; i < M.size(); i++)
			if (arein[i] == 3) mut++;
			else if (arein[i] >> 2) V.push_back(arein[i]);
		for (int i = 0; i < 1 << (n - 2); i++) {
			int msk = (i << 2) | 1;
			int imsk = ((1 << n) - 1) ^ msk;
			int cur = mut;
			for (int j = 0; j < V.size(); j++)
				if ((V[j] & msk) && (V[j] & imsk)) cur++;
			res = min(res, cur);
		}
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}