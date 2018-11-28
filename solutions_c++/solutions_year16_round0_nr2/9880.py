#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include<map>
#include<iterator>
#include<set>
#include<stack>
#include<queue>
#include<fstream>
#include<iomanip>
#include<list>
#include <sstream>
#include<cmath>
#include<math.h>
#define rep(i,m,n) for(int i = (m); i < (n); i++)
#define repd(i,m,n) for(int i=(m); i > (n); i--)
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define endl '\n'
//#define x first
//#define y second
//#define b first
//#define e second
#define row first
#define col second
using namespace std;
const ll MAX = (ll)1000*1000*1000;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
	int t;
	cin >> t;
	string s;
	vector<int> res(t,0);
	rep(i,0,t)
	{
		cin >> s;
		if (s[0] == '-')
			res[i]++;
		rep(k,1,s.length())
			if (s[k] == '-' && s[k-1] == '+')
				res[i] += 2;
	}

	rep(i,0,t)
		cout <<"case #" + to_string(i + 1) + ": " << res[i] << endl;
	return 0;
}

