#if 1
#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <string>
#include <numeric>
#include <cstring>
#include <ctime>


using namespace std;
#define mp make_pair
#define X first
#define Y second
#define pb push_back

typedef pair<int, int> pii ;
typedef long long LL;
typedef long double LD;
typedef vector<int> vi;

const LL inf = 1e9;
const LD eps = 1e-9;

int m, n;
vector <int> a;
vector <string> s;
LL maxV = -1;
LL maxCnt = 0;
int mod = 1e+9 + 7;
void go(int t)
{
	if (t == m)
	{
		LL sum = 0;
		vector<set<string> > sp(n);
		for (int i = 0; i < m; i++)
		{
			string t = "";
			sp[a[i]].insert(t);
			for (int k = 0; k < s[i].size(); k++)
			{
				t += s[i][k];
				sp[a[i]].insert(t);
			}
		}
		for (int i = 0; i < n; i++)
			sum += sp[i].size();

		if (sum >= maxV)
		{
			if (sum > maxV)
			{
				maxV = sum;
				maxCnt = 1;
			}
			else
			{
				maxCnt++;
			}
		}
	}
	else
	{
		for (int i = 0; i < n; i++)
		{
			a[t] = i;
			go(t + 1);
		}
	}
}
int main()        
{
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int q = 0; q < T; q++)
	{
		scanf("%d %d", &m, &n);
		a.assign(m, 0);
		s.resize(m);
		for (int i = 0; i < m; i++)
		{
			char ch[1024] = {};
			scanf("%s", ch);
			s[i] = ch;
		}
		maxV = -1;
		maxCnt = 0;
		go(0);
		cout << "Case #" << q + 1 << ": " << maxV << " " << maxCnt << endl;
	}
    return 0;
}
#endif