#include<bits/stdc++.h>
#define ll long long
using namespace std;

string s;
ll n;

ll poo() {
	ll ans = 0, rev = 0;
	for(int i=n-1;i>=0;i--) {

		if(rev == 1)
			if(s[i] == '+')
				s[i] = '-';
			else
				s[i] = '+';

		if(s[i] == '-') {
			rev ^= 1;
			ans ++;
		}
	}
	return ans;
}

int main() {
	freopen("inBl.txt", "r", stdin);
	freopen("outBl.txt", "w", stdout);
	ll t;
	cin>>t;
	for(int cases = 1; cases <= t; cases++) {
		cin>>s;
		n = s.size();
		cout<<"Case #"<<cases<<": "<<poo()<<"\n";
	}
}