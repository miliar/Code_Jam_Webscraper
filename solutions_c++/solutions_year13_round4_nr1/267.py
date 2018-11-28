#include <iostream>
#include <algorithm>
#include <gmpxx.h> // http://gmplib.org/
using namespace std;
int N,M;
//typedef long long ll;
typedef mpz_class ll;
ll cost(ll n) {
	return n*N - n*(n-1)/2;
//	return (n*n + n - 2) / 2;
}
struct S {
	int a,b,c;
};
const int MM = 2024;
S trips[MM];
int stops[MM];
ll usage[MM];

ll res;

void solve(int a, int b) {
	if (a==b) return;
	int bi=a;
	for(int i=a+1; i<b; ++i) {
		if (usage[i]<usage[bi]) bi=i;
	}
	ll x = usage[bi];
//	cout<<"ok "<<a<<' '<<b<<' '<<stops[a]<<' '<<stops[b]<<" : "<<bi<<' '<<x<<'\n';
	for(int i=a; i<b; ++i)
		usage[i] -= x;
	res += cost(stops[b]-stops[a]) * x;
	solve(a, bi);
	solve(bi+1, b);
}

int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N>>M;
		ll res0=0;
		for(int i=0; i<M; ++i) {
			int a,b,c;
			cin>>a>>b>>c;
			trips[i] = (S){a,b,c};
			stops[2*i] = a;
			stops[2*i+1] = b;
			res0 += cost(b-a)*c;
		}
		sort(stops,stops+2*M);
		int K = unique(stops,stops+2*M)-stops;
//		cout<<"K "<<K<<'\n';
		for(int i=0; i<M; ++i) {
			S s = trips[i];
			int a = lower_bound(stops, stops+K, s.a)-stops;
			int b = lower_bound(stops, stops+K, s.b)-stops;
			for(int j=a; j<b; ++j) usage[j] += s.c;
		}
//		for(int i=0; i<K; ++i) cout<<stops[i]<<' ';cout<<'\n';
//		for(int i=0; i<K; ++i) cout<<usage[i]<<' ';cout<<'\n';
		res=0;
		solve(0, K-1);
//		cout<<res0<<' '<<res<<'\n';
		cout<<"Case #"<<a<<": "<<res0-res<<'\n';
	}
}
