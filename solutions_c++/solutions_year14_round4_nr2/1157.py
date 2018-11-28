#include <bits/stdc++.h>
using namespace std;

const int N = 1005;

class BITree {
public:
    static const int SIZE = ::N;
    int u[SIZE];
    void clear(){
        memset(u,0,sizeof(u));
    }
    void modify(int x, int v){
        for(;x<SIZE;x+=x&-x) u[x]+=v;
    }
    int getsum(int x){
        int s=0;
        for(;x;x-=x&-x) s+=u[x];
        return s;
    }
} tr;

int n, a[N];

int gao(const vector<int>& v) {
	int n = v.size();
	if (n <= 1) return 0;
	tr.clear();
	int ret = 0;
	for (int i = n-1; i >= 0; --i) {
		ret += tr.getsum(v[i]);
		tr.modify(v[i], 1);
	}
	return ret;
}

int main() {
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d", &n);
		map<int,int> mp;
		for (int i = 0; i < n; ++i) {
			scanf("%d", a+i);
			mp[a[i]] = 0;
		}
		map<int,int>::iterator it = mp.begin();
		for (int i = 1; it != mp.end(); ++it, ++i) {
			it->second = i;
		}
		for (int i = 0; i < n; ++i) a[i] = mp[a[i]];
		int ans = n * n;
		for (int i = 0; i < 1<<n; ++i) {
			vector<int> u, v;
			int cnt = 0;
			for (int j = 0; j < n; ++j) {
				if (i & 1<<j) {
					cnt += j - u.size();
					u.push_back(a[j]);
				} else {
					v.push_back(a[j]);
				}
			}
			reverse(v.begin(), v.end());
			cnt += gao(u) + gao(v);
			ans = min(ans, cnt);
		}
		/*
		int ma = 0;
		for (int i = 1; i < n; ++i) {
			if (a[i] > a[ma]) ma = i;
		}
		vector<int> u, v;
		for (int j = 0; j < ma; ++j) u.push_back(a[j]);
		for (int j = n-1; j > ma; --j) v.push_back(a[j]);
		int ans = gao(u) + gao(v);
		for (int i = 0; i < ma; ++i) {
			u.clear(), v.clear();
			for (int j = 0; j < i; ++j) u.push_back(a[j]);
			for (int j = n-1; j > ma; --j) v.push_back(a[j]);
			for (int j = ma-1; j >= i; --j) v.push_back(a[j]);
			int cnt = ma - i + gao(u) + gao(v);
			ans = min(ans, cnt);
		}
		for (int i = ma+1; i < n; ++i) {
			u.clear(), v.clear();
			for (int j = 0; j < ma; ++j) u.push_back(a[j]);
			for (int j = ma+1; j <= i; ++j) u.push_back(a[j]);
			for (int j = n-1; j > i; --j) v.push_back(a[j]);
			int cnt = i - ma + gao(u) + gao(v);
			ans = min(ans, cnt);
		}
		*/
		printf("Case #%d: %d\n", cas, ans);
	}
}

