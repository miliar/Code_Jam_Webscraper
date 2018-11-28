#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream cin("a0.in");
ofstream cout("a0.out");
int t, n, m, o, e, p;
const int mod = 1000002013;
vector<pair<int,long long> > sum;
int s, lg;
vector<vector<int> > pre;
long long ans;

int rmq(int i, int j)
{
	int idx = 0;
	for (int k = j-i; k > 1; k >>= 1)
		idx++;
	int stp = 1<<idx;
	return(sum[pre[i][idx]].second < sum[pre[j-stp+1][idx]].second ? pre[i][idx] : pre[j-stp+1][idx]);
}

long long fee(int length)
{
	long long ret = 2*n-length+1;
	ret *= length;
	ret /= 2;
	ret %= mod;
	return ret;
}

void dq(int i, int j, int used)
{
	if (i > j) return;
	int m = rmq(i,j);
//	cerr << i << ' ' << j << ' ' << used << endl;
	ans -= fee(sum[j+1].first-sum[i].first)*(sum[m].second-used);
	//cerr << ans << endl;
	ans %= mod;
	dq(i,m-1,sum[m].second);
	dq(m+1,j,sum[m].second);
}


int main()
{
	cin >> t;
	for (int k = 1; k <= t; ++k) {
		ans = 0;
		cin >> n >> m;
		vector<pair<int,int> > event;
		for (int i = 0; i < m; ++i) {
			cin >> o >> e >> p;
			ans += fee(e-o)*p;
			ans %= mod;
			event.push_back(pair<int,int>(o,p));
			event.push_back(pair<int,int>(e,-p));
		}
		sort(event.begin(), event.end());

		sum.resize(1);
		sum[0] = pair<int,long long>(0,0);
		for (int i = 0; i < 2*m; ++i) {
			if (sum.back().first == event[i].first)
				sum.back().second += event[i].second;
			else {
				pair<int,long long> tmp;
				tmp.first = event[i].first;
				tmp.second = sum.back().second+event[i].second;
				sum.push_back(tmp);
			}
		}

		s = sum.size();
	//	for (int i = 0; i < s; ++i)
	//		cerr << sum[i].first << ' ' << sum[i].second << endl;
		lg = 1;
		for (int i = 1; i < s; i <<= 1)
			++lg;
		pre.resize(s);
		for (int i = 0; i < s; ++i)
			pre[i].resize(lg);
		for (int i = 0; i < s; ++i)
			pre[i][0] = i;
		for (int j = 1, stp = 1; j < lg; ++j, stp <<= 1)
			for (int i = 0; i <= s-2*stp; ++i)
				pre[i][j] = (sum[pre[i][j-1]].second < sum[pre[i+stp][j-1]].second? pre[i][j-1] : pre[i+stp][j-1]);
	//	cerr << ans << endl;
/*
		for (int i = 0; i < s; ++i) {
			for (int j = 0; j < lg; ++j)
				cout << pre[i][j] << ' ';
			cout << endl;
		}
*/		dq(1,s-2,0);
		cout << "Case #" << k << ": " << (ans+mod)%mod << '\n';
	}
	return 0;
}
	
