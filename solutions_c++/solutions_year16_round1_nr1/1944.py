#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long ll;

string GetAns(string s)
{
	int l = s.length();
	string ret = s.substr(0, 1);
	for (int i = 1; i < l; i++)
	{
		if (s[i]>=ret[0])
			ret = s.substr(i, 1) + ret;
		else
			ret = ret + s.substr(i, 1);
	}

	return ret;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	//freopen("A.in","r",stdin);freopen("A.out","w",stdout);
	int testcase;

	string ans;

	scanf("%d", &testcase);
	for (int case_id = 1; case_id <= testcase; case_id++)
	{
		string ans;
		string s;
		printf("Case #%d: ", case_id);
		cin >> s;


		cout<< GetAns(s);
		printf("\n");
	}
	return 0;
}

