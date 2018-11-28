#define _CRT_SECURE_NO_WARNINGS
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <bitset>
#include <fstream>

using namespace std;

#define V vector
#define se second
#define fr first
#define all(v)  ((v).begin()), ((v).end())
#define allr(v) ((v).rbegin()), ((v).rend())
#define clr(v, d) memset(v, d, sizeof(v))
#define sf(x) scanf("%d", &x);
#define sf2(x, y) scanf("%d %d", &x, &y);
#define sf3(x, y, z) scanf("%d %d %d", &x, &y, &z);
#define sfll(x) scanf("%I64d", &x);
#define sfll2(x, y) scanf("%I64d %I64d", &x, &y);
#define sfll3(x, y, z) scanf("%I64d %I64d %I64d", &x, &y, &z);
int dx[]{1, -1, 0, 0, 1, -1, 1, -1};
int dy[]{0, 0, 1, -1, 1, -1, -1, 1};
typedef unsigned long long          ull;
typedef long long                   ll;
typedef long double                 LD;

int main()
{
	
	freopen("out.txt", "w", stdout);
	freopen("Ems.txt", "r", stdin);
	string s[] = { "ZERO", "TWO", "EIGHT", "SIX", "FOUR", "FIVE", "SEVEN", "ONE", "THREE", "NINE" };
	int S[] = { 0, 2, 8, 6, 4, 5, 7, 1, 3, 9 };
	int T;
	cin >> T;
	int c = 1;
	while (T--){
		string st;
		cin >> st;
		V<int>v(26), ans(10);
		for (int i = 0; i < st.size(); i++){
			v[st[i] - 'A']++;
		}
		for (int i = 0; i < 10; i++){
			int mn = INT_MAX;
			for (int j = 0; j < s[i].size(); j++){
				mn = min(mn, v[s[i][j] - 'A']);
			}
			ans[S[i]] = mn;
			for (int j = 0; j < s[i].size(); j++){
				v[s[i][j] - 'A'] -= mn;
			}
		}
		cout << "Case #" <<c++<< ": ";
		for (int i = 0; i < 10; i++){
			for (int j = 0; j < ans[i]; j++)
				cout<< i;
		}
		cout << endl;
	}
	  

	return 0;
}