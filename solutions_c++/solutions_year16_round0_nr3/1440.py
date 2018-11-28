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
const LL INF = 1e9 + 7;
const int N = 1e6 + 10;
int a[N];
vector<int> prime;
void init()
{
	MEM(a, 0);
	for (int i = 2; i < N; i++)
	{
		if (a[i]) continue;
		prime.push_back(i);
		for (int j = i + i; j < N; j += i) a[j] = 1;
	}
}


bool check(LL x, int b, int p)
{
	LL ans = 0;
	LL t = 1;
	for (int i = 32; i >= 0; i--)
	{
		ans *= b;
		if ((1LL << i)&x)
		{
			ans++;
		}
		if (ans > p)
		{
			break;
		}
	}
	if (ans == p) return false;
	LL r = 0;
	for (int i = 32; i >= 0; i--)
	{
		r *= b;
		if ((1LL << i)&x) r++;
		r %= p;
	}
	return r == 0;
}

string num2str(LL n)
{
	string ans;
	while (n)
	{
		ans.push_back(n % 2 + '0');
		n /= 2;
	}
	reverse(ans.begin(), ans.end());
	return ans;
}
int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	ofstream fout("output.txt");
	//int ncase;
	//cin >> ncase;
	//string str;
	//int ks = 1;
	//while (ncase--)
	//{
	//	cin >> str;
	//	int ans = getans(str);
	//	printf("Case #%d: %d\n", ks++, ans);
	//}
	init();
	int n;
	vector<int> ans;
	fout << "Case #1:" << endl;
	int ks = 1;
	for (LL i = (1LL << 31) + 1; i < (1LL << 32); i+=2)
	{
		//cout << i << endl;
		vector<int> v;
		for (int j = 2; j <= 10; j++)
		{
			for (auto p : prime)
			{
				
				if (check(i, j, p))
				{
					v.push_back(p);
					break;
				}
			}
		
		}
		
		if (v.size() == 9)
		{
			ans.push_back(i);
			cout << ks++ << endl;
			cout << i << ' ' << num2str(i) << endl;
			fout << num2str(i);
			for (auto &x : v) fout << " " << x;
			fout << endl;
		}
		if (ans.size() >= 500) break;
		
	}
	//cout << endl;
	//for (auto &x : ans) cout << x << endl;
	return 0;
}