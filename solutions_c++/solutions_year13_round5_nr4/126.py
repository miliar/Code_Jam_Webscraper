#include <algorithm>
#include <iostream>
#include <iomanip>
#include <complex>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
using namespace std;

string s;
int len;
double F[1<<20];
bool done[1<<20];

int findNext(int mask, int x)
{
	int ret = 0;
	while((mask & (1<<((x+ret)%len))) > 0)
		ret ++;
	return ret;
}

double f(int mask)
{
	if(mask == (1<<len)-1) return 0;
	if(done[mask]) return F[mask];
	done[mask] = true;
	double &ret = F[mask];
	ret = 0;
	for(int i = 0; i < len; i++)
	{
		int t = findNext(mask, i);
		ret += (1.0 / len) * (len-t + f(mask | (1<<((i+t)%len))));
	}

	return ret;
}

void solve()
{
	cin >> s;
	int curMask = 0;
	len = s.length();
	for(int i = 0; i < s.length(); i++)
		if(s[i] == 'X')
			curMask += 1<<i;
	memset(done, false, sizeof(done));
	cout << f(curMask) << endl;
}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	//srand((unsigned)time(NULL));
	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	return MAIN();
}
