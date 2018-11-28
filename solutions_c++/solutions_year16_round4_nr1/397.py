#include <cstdio>
#include <string>
using namespace std;
const int maxn = 1 << 20;
int t, n, r, p, s;
string gao(int dep, char ch)
{
	if(!dep)
		return string(1, ch);
	string a = gao(dep - 1, ch), b = gao(dep - 1, ch == 'P' ? 'R' : (ch == 'R' ? 'S' : 'P'));
	return a < b ? a + b : b + a;
}
bool check(string str)
{
	int rc = 0, pc = 0, sc = 0;
	for(int i = 0, j = (int)str.size(); i < j; ++i)
		if(str[i] == 'R')
			++rc;
		else if(str[i] == 'P')
			++pc;
		else if(str[i] == 'S')
			++sc;
		else
			return 0;
	return rc == r && pc == p && sc == s;
}
int main()
{
	scanf("%d", &t);
	for(int Case = 1; Case <= t; ++Case)
	{
		string ans = "Z", tmp;
		scanf("%d%d%d%d", &n, &r, &p, &s);
		if(check(tmp = gao(n, 'P')) && ans > tmp)
			ans = tmp;
		if(check(tmp = gao(n, 'R')) && ans > tmp)
			ans = tmp;
		if(check(tmp = gao(n, 'S')) && ans > tmp)
			ans = tmp;
		printf("Case #%d: %s\n", Case, ans == "Z" ? "IMPOSSIBLE" : ans.c_str());
	}
	return 0;
}
