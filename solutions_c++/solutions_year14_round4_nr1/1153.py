#include <bits/stdc++.h>
using namespace std;
#define fr(i,a,b) for(int i = a; i < b; ++i)
#define rep(i, n) fr(i,0,n)
#define _(n) rep(i, n)
#define mp make_pair
#define ft first
#define sd second
#define pb push_back
typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long hash;

int n, x;
vector<int> files;

int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;

	for(int tt = 1; tt <= t; ++tt){
		files.clear();
		cin >> n >> x;

		_(n){
			int tmp;
			cin >> tmp;
			files.pb(tmp);
		}

		sort(files.begin(), files.end());
		int cnt = 0, ini = 0, fim = n-1;

		while(ini < fim){
			if(files[ini]+files[fim] <= x) ++ini, --fim;
			else --fim;
			++cnt;
		}

		if(ini==fim) ++cnt;

		cout << "Case #" << tt << ": " << cnt << endl;
	}
}
