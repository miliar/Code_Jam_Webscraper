#include<map>
#include<set>
#include<ctime>
#include<cmath>
#include<queue>
#include<stack>
#include<bitset>
#include<vector>
#include<cstdio>
#include<string>
#include<cassert>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iterator>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long LL;
#define MM(a,x) memset(a,x,sizeof(a));
#define P(x) cout<<#x<<" = "<<x<<endl;
#define P2(x,y) cout<<#x<<" = "<<x<<", "<<#y<<" = "<<y<<endl;
#define TM(a,b) cout<<#a<<"->"<<#b<<": "<<1.*(b-a)/CLOCKS_PER_SEC<<"s\n";
template<class T>void PV(T a, T b) {for(T i = a; i < b; ++i)cout << *i << " "; cout << endl;}
template<class T>void chmin(T &t, T f) {if(t > f) t = f;}
template<class T>void chmax(T &t, T f) {if(t < f) t = f;}

const LL mod = 1000002013;

LL N, M;

LL L[1010];
LL R[1010];
LL p[1010];

LL tot;

LL calc(LL len, LL p) {
	LL tot = ((2 * N - len + 1) * len / 2 % mod) * p % mod;
	return tot;
}

int main() {
	int T;
	cin >> T;
	for(int ts = 1; ts <= T; ts++) {
		cerr << ts << endl;
		cin >> N >> M;
		vector<int> v;
		tot = 0;
		for(int i = 0; i < M; i++) {
			cin >> L[i] >> R[i] >> p[i];
			//L[i] = rand() % 1000000000;
			//R[i] = rand() % 1000000000;
		//	if(L[i] > R[i]) swap(L[i], R[i]);
		//	R[i]++;
			//p[i] = rand() % 1000000000;
			v.push_back(L[i]);
			v.push_back(R[i]);
			LL len = R[i] - L[i];
			tot += calc(len, p[i]);
		}
		//P(tot);
		sort(v.begin(), v.end());
		v.resize(unique(v.begin(), v.end()) - v.begin());
		vector<pair<LL, LL> > cur, next;
		LL cost = 0;
		for(int i = 1; i < v.size(); i++) {
			next.clear();
			for(int j = 0; j < M; j++) {
				if(L[j] < v[i] && R[j] >= v[i]) {
					int dl = v[i] - v[i - 1];
					if(cur.empty()) {
						next.push_back(make_pair(dl, p[j]));
					} else {
						int num = p[j];
						for(int k = cur.size() - 1; k >= 0 && num > 0; k--) {
							LL &len = cur[k].first;
							LL &person = cur[k].second;
							if(person == 0) continue;
							if(num <= person) {
								person -= num;
								next.push_back(make_pair(len + dl, num));
								num = 0;
								break;
							} else {
								num -= person;
								next.push_back(make_pair(len + dl, person));
								person = 0;
							}
						}
						if(num > 0) next.push_back(make_pair(dl, num));
					}
				}
			}
			for(int j = 0; j < cur.size(); j++) cost += calc(cur[j].first, cur[j].second);
			cur = next;
			sort(cur.begin(), cur.end());

			int nt[2010] = {};
			for(int j = 1; j < cur.size(); j++) {
				if(cur[j].first == cur[j - 1].first) nt[j] = nt[j - 1];
				else nt[j] = j;
				if(nt[j] != j) cur[nt[j]].second += cur[j].second;
			}
			next.clear();
			for(int j = 0; j < cur.size(); j++) if(nt[j] == j)next.push_back(cur[j]);
			cur = next;
		}
		for(int j = 0; j < cur.size(); j++) cost += calc(cur[j].first, cur[j].second);
		LL ret = ((tot - cost) % mod + mod) % mod;
		cout << "Case #" << ts << ": " << ret << endl;
	}
	return 0;
}
