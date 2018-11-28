#include<iostream>
#include<cstdio>
#include<cstring>
#include<set>

using namespace std;

int a[100][100];
int N, M;
set<int> h;

bool has(int n) {
	for(int i = 0; i < N; ++i) {
		for( int j = 0; j < M; ++j ) {
			if(a[i][j] <=n) return true;
		}
	}
	return false;
}

bool check(int n) {
	for(int i = 0; i < N; ++i) {
		bool f = true;
		for(int j = 0; j < M; ++j) {
			if(a[i][j] > n) {
				f = false;
				break;
			}
		}
		if(f) {
			for(int j = 0; j < M; ++j )
				a[i][j] = 0;
		}
	}
	for(int j = 0; j < M; ++j) {
		bool f = true;
		for(int i = 0; i < N; ++i) {
			if(a[i][j] > n) {
				f = false;
				break;
			}
		}
		if(f) {
			for(int i = 0; i < N; ++i )
				a[i][j] = 0;
		}
	}
	for(int i = 0; i < N; ++i) {
		for(int j = 0; j < M; ++j) {
			if(a[i][j] == 0) a[i][j] = n+1;
		}
	}
	if(has(n)) { return false; }
	return true;
}

int main()
{
	// freopen("2.in","r",stdin);
	// freopen("2.out","w",stdout);
	int T;
	cin >> T;
	for(int cases = 1; cases <= T; ++ cases) {
		memset(a, 0, sizeof(a));
		cin >> N >> M;
		for(int i = 0; i < N; ++i) {
			for( int j = 0; j < M; ++j) {
				cin >> a[i][j];
				h.insert(a[i][j]);
			}
		}
		bool f = true;
		for(typeof(h.begin()) i = h.begin(); i != h.end(); ++i) {
			if(!check(*i)) {
				f = false;
				break;
			}
		}
		if(f) {
			printf("Case #%d: YES\n", cases);
		} else {
			printf("Case #%d: NO\n", cases);
		}
	}
	return 0;
}