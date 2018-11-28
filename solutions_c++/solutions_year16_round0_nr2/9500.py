#include<bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define SZ(v) (int)v.size()
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define iter(it,s) for(__typeof(s.begin())it = s.begin();it!=s.end();it++)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<pi> vpi;


const int OO = (int) 2e9;
const double eps = 1e-9;

// 1 based
int daysInMonths[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };
#define Nd 0
#define Ed 1
#define Sd 2
#define Wd 3


int main() {
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
		freopen("out.out", "wt", stdout);
#endif
	int t,cs = 1;
	cin >> t;
	string in;
	while(t--){
		cin >> in;
		string s;
		s += in[0];
		FOR(i,1,SZ(in))
			if(in[i] != in[i-1])
				s += in[i];

		bool pos = 0;
		int res = 0;
		FOR(i,0,SZ(s))
			if(s[i] == '-')
				res += 1 + pos, pos = 1;
			else
				pos = 1;

		printf("Case #%d: %d\n", cs++, res);
	}
	return 0;
}





