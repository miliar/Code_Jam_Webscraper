#include <iostream>
#include <cstdio>
#include <vector>
#include <set>

using namespace std;

#define ll long long
#define f first
#define s second
#define mp make_pair
#define pb push_back


int t, n, sum;
pair <int, int> a[20000];
set <pair <int, int> > q;
vector <int>  res;
void out(int v, int x) {
 	cout << char(v + 'A' - 1);
 	if (x == 0) cout << " ";
}


int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	cin >> t;
	int qq = 0;
	while (t--) {
	 	cin >> n;
	 	sum = 0;
	 	qq++;
	 	cout << "Case #" << qq << ": ";
	 	for (int i = 1; i <= n; i++) {
	 		cin >> a[i].f;
	 		a[i].s = i;
	 		sum += a[i].f;
	 	}
	 	q.clear();
	 	res.clear();
	 	int last = -1;

		for (int i = 1; i <= n; i++)
			q.insert(mp(-a[i].f,a[i].s));
		while (1) {
		 	pair <int, int> vv = *q.begin();
		 	int v = vv.f;
		 	int cnt = vv.s;
		 	q.erase(vv);
		 	if (q.size() == 1 && q.begin()->first == v) {
		 		last = cnt;
		 	 	break;
		 	}
		 	res.pb(cnt);
		 	if (v != -1)q.insert(mp(v+1, cnt));
		}
		for (int i = 0; i < res.size(); i++)
			out(res[i], 0);

	     	int szz = q.begin()->first;
	     	for (int i = 0; i < -szz; i++) {
			out(last, 1);	
			out(q.begin()->second, 0);
		}
		cout << endl;
	}

 	return 0;
}