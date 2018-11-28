#include <cstdio>
#include <complex>
#include <iostream>
#include <cassert>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <iomanip>
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define REPE(i,x,y) for (int i=(x);i<(y);i++)
#define REP(i,x,y) for (int i=(x);i<=(y);i++)
#define DREP(i,x,y) for (int i=(x);i>=(y);i--)
#define mp make_pair
#define pb push_back
#define MAXN 100100
#define endc '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

void solve(int tc) {
	cout<<"Case #"<<tc<<": "; int n; cin>>n;
	ld V,X,r1,c1,r2,c2,v1,v2; cin>>V>>X; 
	if (n == 1){
		cin>>r1>>c1;
		if (c1 == X) { cout<<(V/r1)<<endl; return; }
		else { cout<<"IMPOSSIBLE"<<endl; return; }
	}
	cin>>r1>>c1>>r2>>c2;
	if (c1 == c2) {
		if (X!=c1) { cout<<"IMPOSSIBLE"<<endl; return; }
		else {
			cout<<(V/(r1 + r2))<<endl; return; 
		}
	} else {
		if (c1 == X) {
			cout<<V/r1<<endl; return;
		}
		if (c2 == X) {
			cout<<V/r2<<endl; return;
		}
		if (((c1 > X) and (c2 > X)) or ((c1 < X) and (c2 < X))) {
			cout<<"IMPOSSIBLE"<<endl;
			return;
		}
		v1 = (V*X - V*c2)/(c1 - c2);
		v2 = V - v1;
		//cout<<v1<<" "<<v2<<endl
		if ((v1 > V) or (v2 > V)) {
			cout<<"IMPOSSIBLE"<<endl; return;
		}
		//cout<<v1<<" "<<v2<<endl;
		cout<<MAX(v1/r1,v2/r2)<<endl;
	}
}


int main() {
	ios::sync_with_stdio(false); 
	//cin.tie(0);
	cout<<setprecision(12);
	cout<<std::fixed;
	int t; cin>>t; REP(i,1,t) solve(i);
	return 0;
}
