#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#define ll long long 
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int tt=1;tt<=t;tt++) {
		ll n;
		cin >> n;
		map<ll , int> prev;
		int cur = 0, fg = 0;
		for(ll i=0;i<100;i++) {
				cur = (i + 1)*n;
				ll tcur = cur;
				while(tcur != 0)prev[tcur%10] += 1, tcur /= 10;
				if(prev.size() == 10){ fg = 1; break;}
		}
		if(!fg)cout << "Case #" << tt <<": INSOMNIA\n";
		else cout << "Case #" << tt << ": " << cur << "\n";
	}
	return 0;
}