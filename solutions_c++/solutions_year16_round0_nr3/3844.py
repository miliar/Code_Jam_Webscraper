#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <string.h>
#include <set>
#include <cmath>

#define ll long long

using namespace std;

bool check(ll i, int n){

	vector<int> divisors;
	for(ll base = 2; base <= 10; ++base){
		ll val = 1;
		ll b = base;
		ll ip = i;
		for(int k=0; k<n-2; ++k){
			// val = base
			// cout<<ip<<"  aa\n";
			if(ip % 2) val += b;
			ip /= 2;
			b *= base;
		}
		// cout<<b<<" |\n";
		val += b;
		// cout<<val<<"\n";

		ll lim = sqrt(val) + 1;
		for(ll dv = 2; dv <= lim; ++dv){
			if(val % dv == 0){
				divisors.push_back(dv);
				break;
			}
		}

		if(divisors.size() != base-1) return false;
	}

	cout<<"1";
	string nmbr;
	for(int k=0; k<n-2; ++k){
		if(i % 2)
			nmbr = "1" + nmbr;
		else
			nmbr = "0" + nmbr;
		i /= 2;
	}
	cout<<nmbr;
	cout<<"1 ";
	for(int j=0; j<divisors.size(); ++j)
		cout<<divisors[j]<<" ";
	cout<<"\n";

	return true;

}


void solve(int t) {
	int n;
	int j;
	cin>>n>>j;
	cout<<"Case #1:\n";
	
	ll p2 = 1;
	int n2 = n-2;
	while(n2--) p2*=2;
	
	for(ll i = 0; i<p2; ++i){
		// cout<<"Checking: "<<i<<"\n";
		j -= check(i, n);
		if(j == 0) return;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	// cout<<check(1, 6)<<"\n";

	// return 0;
	int T;
	cin>>T;
	int t = 1;
	while(T--)
		solve(t++);

	return 0;

}