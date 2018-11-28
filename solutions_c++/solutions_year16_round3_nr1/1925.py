#include <bits/stdc++.h>
using namespace std;
#define ll long long

//string res[] = { "First", "Second" };
//const double pi = 3.1415926535897932384626433832795;
//int dx[] = {-1,0,1,0};
//int dy[] = {0,-1,0,1};

/*
 bool valid(int r,int c){
 return (r >= 0 && r < n && c >= 0 && c < m);
 }
 */
//ll gcd(ll a, ll b) { return (b == 0 ? a : gcd(b, a % b)); }
//ll lcm(ll a, ll b) { return (a * (b / gcd(a, b))); }



int main() {
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	ios_base::sync_with_stdio(0);

	int T;
	cin >> T;
	for(int t=1;t <= T; ++t) {

		int n;
		cin >> n;
		int sum = 0;
		priority_queue<pair<int,char> > pq;
		for(int i=0;i<n;++i) {
			int x;
			cin >> x;
			char c = 'A' + i;
			pq.push({x,c});
		}

		cout << "Case #" << t << ": ";
		while(!pq.empty()) {
			int sz = pq.size();
			pair<int,char> x = pq.top();
			pq.pop();
			if(!pq.empty()) {
				pair<int,char> y = pq.top();
				pq.pop();

				if (x.first == y.first && sz == 2) {
					x.first--;
					y.first--;
					cout << x.second << y.second << " ";
				} else {
					cout << x.second << " ";
					x.first -= 1;
				}

				if(x.first > 0) pq.push(x);
				if(y.first > 0) pq.push(y);
			}
			else {
				if(x.first > 1) {
					cout << x.second << x.second << " ";
					x.first -= 2;
					if(x.first > 0) pq.push(x);
				}
				else {
					cout << x.second << " ";
					x.first--;
				}
			}

		}
		cout << endl;

	}
}
