#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#define SUBMIT 1
#define SMALL 0
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>
using namespace std;
#define rep(i, n) for (i = 0; i < (n); i++)
#define rep1(i,n) for (i=1; i<=n; i++)
#define repab(i,a,b) for (i=a; i<=b; i++)
#define repr(i,n) for (i=(n)-1; i>=0; i--)
#define repr1(i,n) for (i=n; i>0; i--)
#define reprab(i,a,b) for (i=b; i>=a; i--)
#define repv(i,s) for (i=s.begin(); i!=s.end(); i++)
#define zero(a) memset(a, 0, sizeof(a))
#define sz(s) int((s).size())
#define all(s) (s).begin(),(s).end()
#define fill(x,y) memset(x,y,sizeof(x))
#define mod 1000000007
#define LL long long
#define LD long double

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

int main()
{
	if (SUBMIT) {
		if (SMALL) {
			freopen("s.in", "r", stdin);
			freopen("s.out", "w", stdout);
		}
		else {
			freopen("l.in", "r", stdin);
			freopen("l.out", "w", stdout);
		}
	}
	int t, T;
	int i, j, k;
	int ch[26];
	vector<int> ans;
	cin >> T;
	rep1(t, T) {
		string s;
		cin >> s;
		fill(ch, 0);
		ans.clear();
		i = s.length();
		rep(j, i) {
			ch[s[j] - 'A']++;
		}
		rep(k, ch['Z'-'A'])ans.push_back(0);
		rep(k, ch['W' - 'A'])ans.push_back(2);
		rep(k, ch['U'-'A'])ans.push_back(4);
		rep(k, ch['X'-'A'])ans.push_back(6);
		rep(k, ch['G'-'A'])ans.push_back(8);
		ch['E'-'A'] -= ch['Z' - 'A'];
		ch['R'-'A'] -= ch['Z' - 'A'];
		ch['O'-'A'] -= ch['Z' - 'A'];
		//////////////////
		ch['T' - 'A'] -= ch['W' - 'A'];
		ch['O' - 'A'] -= ch['W' - 'A'];
		////////////////////
		ch['F' - 'A'] -= ch['U' - 'A'];
		ch['O' - 'A'] -= ch['U' - 'A'];
		ch['R' - 'A'] -= ch['U' - 'A'];
		/////////////////////
		ch['S' - 'A'] -= ch['X' - 'A'];
		ch['I' - 'A'] -= ch['X' - 'A'];
		////////////////////
		ch['E' - 'A'] -= ch['G' - 'A'];
		ch['I' - 'A'] -= ch['G' - 'A'];
		ch['H' - 'A'] -= ch['G' - 'A'];
		ch['T' - 'A'] -= ch['G' - 'A'];
		////////////////////////
		rep(j, ch['O' - 'A'])ans.push_back(1);
		ch['N' - 'A'] -= ch['O' - 'A'];
		rep(j, ch['F' - 'A'])ans.push_back(5);
		ch['V' - 'A'] -= ch['F' - 'A'];
		rep(j, ch['V' - 'A'])ans.push_back(7);
		ch['N' - 'A'] -= ch['V' - 'A'];
		ch['N' - 'A'] /= 2;
		rep(j, ch['N' - 'A'])ans.push_back(9);
		rep(j, ch['H' - 'A'])ans.push_back(3);
		sort(all(ans));
		cout << "Case #" << t << ": ";
		j = ans.size();
		rep(i, j)cout << ans[i];
		cout << endl;
	}
	if (!SUBMIT)system("pause");
	return (0);
}