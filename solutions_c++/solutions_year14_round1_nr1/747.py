#include <cstdlib>   
#include <cctype>   
#include <cstring>   
#include <cstdio>   
#include <cmath>   
#include <algorithm>   
#include <vector>   
#include <string>   
#include <iostream>   
#include <sstream>   
#include <map>   
#include <set>   
#include <queue>   
#include <stack>   
#include <fstream>   
#include <numeric>   
#include <iomanip>   
#include <bitset>   
#include <list>   
#include <stdexcept>   
#include <functional>   
#include <utility>   
#include <ctime>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MEM(a,b) memset((a),(b),sizeof(a))
const int N = 4e5 + 10;
LL toLL(string str)
{
	LL ret = 0;
	for (int i = 0; i < str.length(); i++)
	{
		ret <<= 1;
		ret |= (str[i] - '0');
	}
	return ret;
}

int check(vector<LL> v1, vector<LL> v2, int x, int n)
{
	int ret = 0;
	LL t = v1[0] ^ v2[x];
	while (t)
	{
		ret++;
		t -= (t&-t);
	}
	t = v1[0] ^ v2[x];
	for (int i = 0; i < n; i++) v1[i] ^= t;
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	for (int i = 0; i < n; i++)
	{
		if (v1[i] != v2[i]) return -1;
	}
	return ret;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	vector<LL> v1, v2;
	string str;
	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		int n, l;
		cin >> n >> l;
		v1.clear();
		v2.clear();
		v1.resize(n);
		v2.resize(n);
		for (int i = 0; i < n; i++)
		{
			cin >> str;
			v1[i] = toLL(str);
		}
		for (int i = 0; i < n; i++)
		{
			cin >> str;
			v2[i] = toLL(str);
		}
		int ans = l+1;;
		for (int i = 0; i < n; i++)
		{
			int t;
			t = check(v1, v2, i, n);
			if (t != -1) ans = min(t, ans);
		}
		printf("Case #%d: ", ks++);
		if (ans <= l) printf("%d\n", ans);
		else printf("NOT POSSIBLE\n");
	}
	return 0;
}