#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define FOR(i,a,n) for(int i=a;i<(int)(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),(a).end()
#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define F first
#define S second
const int INF = 2000000000;
const int DX[4]={0,1,0,-1}, DY[4]={-1,0,1,0};
struct P{int x;int y;P(int X=0,int Y=0){x=X;y=Y;}};

struct hoge{
	vector<int> p;
	int n;
	int sum;
	hoge():n(0),sum(0){}
	hoge(const hoge& h) {
		n = h.n;
		sum = h.sum;
		int s = h.p.size();
		p.reserve(s);
		copy(h.p.begin(),h.p.end(),back_inserter(p));
	}
	void sort_p() {
		sort(ALL(p),greater<int>());
	}
};

int main() {
	int T;
	cin >> T;
	REP(t,T) {
		int D;
		cin >> D;

		hoge sh;
		sh.p.resize(D);
		REP(i,D) {
			cin >> sh.p[i];
			sh.sum += sh.p[i];
		}
		sh.sort_p();

		queue<hoge> q;
		q.push(sh);
		int ans = INF;
		while(!q.empty()) {
			hoge h = q.front(); q.pop();

			if(h.n > ans) continue;
			if(h.sum == 0) {
				// cout << h.n << endl;
				ans = min(ans, h.n);
				continue;
			}

			if(h.p[0] > 3) {
				FOR(k,2,10) {
					if(h.p[0]/k > 0) {
						hoge nh(h);
						int s = h.p.size();
						int s_ = 0;
						REP(i,s) {
							if(h.p[0] != h.p[i]) break;
							int t1 = h.p[0]/k;
							int t2 = h.p[0] - t1;
							nh.p[i] = t1;
							nh.p.PB(t2);
							s_++;
						}
						nh.n += s_;
						nh.sort_p();
						q.push(nh);
					}
				}
			}

			int s = h.p.size();
			REP(i,s) {
				if(h.p[i]>0) {
					h.p[i]--;
					h.sum--;
				}
			}
			h.n++;
			h.sort_p();
			q.push(h);
		}

		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}
