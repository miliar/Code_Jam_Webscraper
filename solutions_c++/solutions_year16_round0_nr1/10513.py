#include <iostream>
#include <algorithm>
#include <set>
#include <cmath>
#include <cstdio>
#include <map>

using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

ll t, n;
bool used[12];
string res = "";

void make(ll m){
	while(m > 0){
		used[m%10] = 1;
		m/=10;
	}
}
bool check(){
	for(int i = 0; i < 10; i++){
		if(used[i] == false) return false;
	}
	return true;
}


int main(){
    cin >> t;
    freopen("output.txt", "w", stdout);
    for(ll i = 1ll; i <= t; i++){
    	cin >> n;
    	ll j = 2ll, r = n;
    	memset(used, false, sizeof used);
    	if(n == 0){
    		cout << "Case #" << i << ": " << "INSOMNIA\n";
    		continue;
    	}
		int cnt = 100;
		bool ok = false;
		while(cnt --){
		//	cout << r << endl;
			make(r);
			if(check()){
				ok = 1;
				cout << "Case #" << i << ": " << r << endl;
				break;
			}
			r = n*1ll*j;
			j++;
		}
		if(!ok){
    		cout << "Case #" << i << ": " << "INSOMNIA\n";			
		}
    	
    }
	return 0;
}