#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second


VI move(VI s, int mv){
	VI r(s);
	if(mv == 0){
		reverse(r.begin(), r.end());
		while(!r.empty() && r.back() == 1)
			r.pop_back();
		reverse(r.begin(), r.end());
		foreach(r, it)
			(*it)--;
	}
	else if(!r.empty()){
		int v = r.back();
		r.back() = (v+1)/2 + mv-1;
		if(v > 1)
			r.push_back(v/2 - (mv-1));
		sort(r.begin(), r.end());
	}
	return r;
}

int h(VI s){
	if(s.empty())
		return 0;
	int r = 0;
	int v = s.back();
	while(v){
		v /= 2;
		r++;
	}
	return r;
}

int ans;

void BT(VI s, int g){
	if(s.empty() || g+h(s) >= ans){
		ans = min(ans,g+h(s));
		return;
	}

	BT(move(s,0),g+1);
	//if(s.back() > 1)
	FOR(i,0,s.back()/2)
		BT(move(s,1+i),g+1);
}

int main(){
	int T;
	cin >> T;
	FOR(cnt,0,T){
		int n;
		ans = 1<<30;
		cin >> n;
		VI(s);
		s.resize(n);
		FOR(i,0,n)
			cin >> s[i];
		sort(s.begin(), s.end());
		BT(s,0);
		cout << "Case #" << cnt+1 << ": " << ans << '\n';
	}
	
	return 0;
}
