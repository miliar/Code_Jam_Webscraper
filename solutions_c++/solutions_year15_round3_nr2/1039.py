#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

char ch[10];

int recur(int idx, int k, int l, int s, int &maxs, string &ks, string &t)
{
    if (idx == s)
    {
	int cnt = 0;
	for (int i = 0; i < s; ++ i)
	{
	    int j = i, pos = 0;
	    while (j < s && pos < t.length())
	    {
		if (ch[j] != t[pos]) break;
		++ j;
		++ pos;
	    }
	    if (pos == t.length()) ++ cnt;
	}
	if (cnt > maxs) maxs = cnt;
	return cnt;
    }
    int res = 0;
    for (int i = 0; i < ks.length(); ++ i)
    {
	ch[idx] = ks[i];
	res += recur(idx + 1, k, l, s, maxs, ks, t);
    }
    return res;
}

double solve(int k, int l, int s, string &keys, string &tar)
{
    int maxs = 0;
    double tot = recur(0, k, l, s, maxs, keys, tar);
    int div = 1;
    for (int i = 0; i < s; ++ i) div *= k;
    double res = tot / div;
    return maxs - res;
}

int main()
{
    int T, K, L, S;
    cin >> T;
    for (int i = 1; i <= T; ++ i)
    {
	cin >> K >> L >> S;
	string keys, tar;
	cin >> keys >> tar;
	double res = solve(K, L, S, keys, tar);
	printf("Case #%d: %.10f\n", i, res);
    }
    return 0;
}
