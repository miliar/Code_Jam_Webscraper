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

string num[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

string GetAns2(string s)
{
	int l = s.length();
	int count[270] = { 0 };
	int n[10] = { 0 };

	memset(count, 0, sizeof(int)* 270);
	memset(n, 0, sizeof(int)* 10);
	for (int i = 0; i < l; i++)
		count[s[i]]++;
	n[0] = count['Z'];
	count['E'] -= n[0];
	count['R'] -= n[0];
	count['O'] -= n[0];
	n[2] = count['W'];
	count['T'] -= n[2];
	count['O'] -= n[2];
	n[4] = count['U'];
	count['F'] -= n[4];
	count['R'] -= n[4];
	count['O'] -= n[4];
	n[1] = count['O'];
	count['N'] -= n[1];
	count['E'] -= n[1];
	n[5] = count['F'];
	count['I'] -= n[5];
	count['V'] -= n[5];
	count['E'] -= n[5];
	n[3] = count['R'];
	count['T'] -= n[3];
	count['H'] -= n[3];
	count['E'] -= n[3] * 2;
	n[6] = count['X'];
	count['S'] -= n[6];
	count['I'] -= n[6];
	n[7] = count['S'];
	count['E'] -= n[7] * 2;
	count['V'] -= n[7];
	count['N'] -= n[7];
	n[8] = count['G'];
	n[9] = count['N'] / 2;

	string ret = "";
	for (int i = 0; i < 10; i++)
	for (int j = 0; j < n[i]; j++)
		ret += std::to_string(i);


	return ret;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
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


		cout << GetAns2(s);
		printf("\n");
	}
	return 0;
}

