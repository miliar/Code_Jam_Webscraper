#include <bits/stdc++.h>
using namespace std;
int main() {
	puts("Case #1:");
	int N=16,J=50;
	for (int i=(1<<(N-1)), cnt=0; i<(1<<N) && cnt<J; i++) if (i%2==1) {
		vector<long long> divisors;
		for (int base=2; base<=10; base++) {
			long long v=0;
			for (int it=0;it<N;it++) {
				v *= base;
				if (i & (1<<(N-1-it))) v += 1;
			}
			bool ok=false;
			for (long long d=2; (long long)d*d<=v; d++) {
				if (v % d == 0) { divisors.push_back(d); ok=true; break; }
			}
			if (!ok) goto nxt;
		}
		{
			cnt++;
			string s;
			for(int it=0;it<N;it++)s += '0'+((i&(1<<(N-1-it))) ? 1 : 0);
			cout << s;
			for(auto d:divisors)cout<<" "<<d;
			cout<<endl;
		}
		nxt:;
	}
}
