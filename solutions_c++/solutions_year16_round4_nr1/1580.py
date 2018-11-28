#include <bits/stdc++.h>
using namespace std;
const int N = (int)1e5 + 7;
int n, r, p, s;
char get(char a, char b) {
	if(a == 'R') {
		if(b == 'S') return a;
		else if(b == 'P') return b;
		else return 'a';
	} else if(a == 'S') {
		if(b == 'R') return b;
		else if(b == 'P') return a;
		else return 'a';
	} else {
		if(b == 'R') return a;
		else if(b == 'S') return b;
		else return 'a';
	}
}
void solve() {
	cin>>n>>r>>p>>s;
	vector<char> v;
	for(int i=0;i<p;i++) v.push_back('P');
	for(int i=0;i<r;i++) v.push_back('R');
	for(int i=0;i<s;i++) v.push_back('S');
	do {
		vector<char> vv = v;
		bool ok = true;
		for(int i=0;i<n;i++) {
			vector<char> vvv;
			for(int j=0;j<vv.size();j+=2) {
				char cc = get(vv[j],vv[j+1]);
				if(cc == 'a') {
					ok = false;
					break;
				} else vvv.push_back(cc);
			}
			if(!ok) false;
			vv = vvv;
		}
		if(ok) {
			for(auto cc : v) cout<<cc;
			cout<<'\n';
			return;
		}
	} while(next_permutation(v.begin(),v.end()));
	cout<<"IMPOSSIBLE"<<'\n';
	return;
}
int main()
{
	#ifndef ONLINE_JUDGE
		freopen("I.in","r",stdin);
		freopen("O.out","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int cases=1;cases<=t;cases++) {
		cout<<"Case #"<<cases<<": ";
		solve();
	}
	return 0;
}