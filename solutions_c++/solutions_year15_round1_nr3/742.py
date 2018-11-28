#include <bits/stdc++.h>

using namespace std;

#define sz(s) (int)s.size()

const double pi = 2 * acos(-1.0);

typedef long long ll;

struct pnt{
	ll x, y;
	pnt(){}
	pnt(ll _x, ll _y) : x(_x), y(_y){}
	bool operator < (const pnt &b)const{
		return (x != b.x ? x < b.x : y < b.y);
	}
	pnt operator + (const pnt &b)const{
		return pnt(x + b.x, y + b.y);
	}
	pnt operator - (const pnt &b)const{
		return pnt(x - b.x, y - b.y);
	}
	pnt operator * (const ll &k)const{
		return pnt(x * k, y * k);
	}
	ll operator * (const pnt &b)const{
		return x * b.x + y * b.y;
	}
	bool operator == (const pnt &b)const{
		return (x == b.x && y == b.y);
	}
	ll operator ^ (const pnt &b)const{
		return  x * b.y - y * b.x;
	}
};
ll myabs(ll x){
	return (x < 0 ? -x : x);
}
ll sdis(const pnt &a, const pnt &b){
	return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}
ll ccw(const pnt &a, const pnt &b, const pnt &c){
	return (b - a) ^ (c - a);
}

struct polygon{
	vector<pnt> a;
	int color;
	polygon(){if (!a.empty()) a.clear(); color = 0;}
	void add(const pnt &b){
		a.push_back(b);
	}
	ll area(){
		if (sz(a) < 3) return 0LL;
		ll s = 0LL;
		for(int i = 1; i < sz(a); ++i) s+= (a[i].x - a[i - 1].x) * (a[i].y + a[i - 1].y);
		s += (a[0].x - a.back().x) * (a[0].y + a.back().y);
		return myabs(s);
	}
	bool contain(const pnt &p)const{
		int l = 1, r = sz(a) - 1, mid;
		while (l < r){
			mid = (l + r) >> 1;
			if (ccw(a[0], a[mid], p) <= 0) r = mid;
			else l = mid + 1;
		}
		if (l == 1 || ccw(a[0], a.back(), p) >= 0LL) return false;
		return (ccw(a[l], a[l - 1], p) < 0LL);
	}
	bool strictlyContain(const polygon &b)const{
		for(int i = 0; i < sz(b.a); ++i)
			if (!contain(b.a[i])) return false;
		return true;
	}
	void getConvex(){
		vector<pnt> h;
		if (!h.empty()) h.clear();
		sort(a.begin(), a.end());
		for(int i = 0; i < sz(a); ++i){
			while (sz(h) >= 2 && ccw(h[sz(h) - 2], h.back(), a[i]) < 0LL) h.pop_back();
			h.push_back(a[i]);
		}
		int l = sz(h) + 1;
		for(int i = sz(a) - 1; i >= 0; --i){
			while (sz(h) >= l && ccw(h[h.size() - 2], h.back(), a[i]) < 0) h.pop_back();
			h.push_back(a[i]);
		}
		if (sz(h) > 1 && h[0] == h.back()) h.pop_back();
		a = h;
	}
	void prPoly(){
	    cout << sz(a) << ' ' << color << ' ';
	    for(int i = 0; i < sz(a); ++i) cout << a[i].x << ' ' << a[i].y << ' ';
	    cout << endl;
	}
} data;
vector<pnt> a;

void solve(){
	int n;
	cin >> n;
	a.resize(n);
	vector<int> ans(n, 100000);
	for(int i = 0; i < n; ++i) cin >> a[i].x >> a[i].y;
	for(int mask = 0; mask < (1<<n); ++mask){
		data.a.clear();
		for(int j = 0; j < n; ++j)
			if (mask & (1<<j)) data.a.push_back(a[j]);
		int prv = sz(data.a);
		data.getConvex();
		int nxt = sz(data.a);
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < (int)data.a.size(); ++j)
			if (a[i] == data.a[j]) ans[i] = min(ans[i], n - __builtin_popcount(mask));
	}
	for(int j = 0; j < n; ++j) cout << ans[j] << endl;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for(int t = 1; t <= tc; ++t){
		cout << "Case #" << t << ":" << endl;
		solve();
	}
	return 0;
}

