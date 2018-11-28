#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define range(i,a,b) for(auto i=(a);i<(b);i++)
#define rep(i,n) range(i,0,n)
#define all(c) begin(c),end(c)
#define CLR(i,x) memset(i,x,sizeof(i))
#define clr0(i) CLR(i,0)
#define clr1(i) CLR(i,-1)
#define bit(x,i) ((x>>i)&1)
#define M(x) ((x)%MOD)
#define acc(f,x,y) x=f(x,y)
#define fst first
#define snd second
#define tup make_tuple

int work()
{
	int n;
	string line, word;
	cin >> n;
	getline(cin, line);

	unordered_map<string, int> id;
	vector<unordered_set<int>> ss(n);
	rep(i, n)
	{
		getline(cin, line);
		istringstream iss(line);
		while(iss >> word)
		{
			if(!id.count(word))
				id[word] = id.size() - 1;
			ss[i].insert(id[word]);
		}
	}

	int m = id.size();
	vi pcnt(m);
	for(auto & s : ss)
	{
		for(auto x : s)
		{
			pcnt[x]++;
		}
	}

	int ans = 2000, nn = 1 << (n - 2);
	rep(s, nn)
	{
		vi c(m);
		range(i, 1, n)
		if(i == 1 || ((s >> (i - 2)) & 1))
		for(auto x : ss[i])
			c[x]++;

		int cnt = 0;
		rep(x, m) if(c[x] != 0 && c[x] != pcnt[x])
			cnt++;

		acc(min, ans, cnt);
	}

	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	rep(i, t)
		cout << "Case #" << i + 1 << ": " << work() << endl;
	return 0;
}
