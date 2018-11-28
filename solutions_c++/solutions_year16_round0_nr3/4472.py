#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <string.h>
#include <string>
#define ll long long
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int tt=1;tt<=t;tt++) {
		int n, k;
		cin >> n >> k;
		cout << "Case #" << tt << ":\n";
		for(ll i=1;i<(ll)(1<<n);i++) {
			vector<int> v;
			for(int j=0;j<n;j++) {
				if(i & (1<<j))v.push_back(1);
				else v.push_back(0);
			}
			if(!(v[0] == 1 and v[n-1]))continue;
			int cnt = 0;
			vector<ll> res;
			for(int j=2;j<=10;j++) {
					ll num = 0;		
					for(int l=0;l<n;l++)
						num = num*(ll)j + (ll)v[l];
					// cout << num << " \n";
					ll tnum = num;
					vector<ll> pfact;
					while(num%2 == 0)pfact.push_back(2LL), num /= 2;
					for(ll l = 3; l <= num/l; l+=2) {
						while(num%l == 0) {
							pfact.push_back(l);
							num /= l;			
						}
					}
					if(num > 1)pfact.push_back(num);
					if((int)pfact.size() >= 1 and pfact[0] != tnum)cnt++, res.push_back(pfact[0]);
			}
			if(cnt == 9) {
				for(int j=0;j < n;j++)
					cout << v[j];
				for(int j=0;j<(int)res.size();j++)
					cout << " " << res[j];
				cout << "\n";
				k--;
			}
			if(k == 0)break;
		}
	}
	return 0;
}