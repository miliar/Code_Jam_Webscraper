#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <math.h>
#include <string.h>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#define MAXN 100001
#define ll long long int
#define INF 0xffffff
#define PI acos(-1)
#define MOD 1000000007LL
 
using namespace std;

int T, J;
int N;

ll toDec(ll num, ll base) {
    ll ans = 0, pot = 1;
    while(num > 0) {
		ans += (num % 10) * pot;
		pot *= base;
		num /= 10;
    }
    return ans;
}

ll toDec(string num, ll base) {
	ll ans = 0, pot = 1;
    for(int i = num.size() - 1; i >= 0; i--) {
		ans += ((num[i] - '0')  % 10LL) * pot;
		pot *= base;
    }
    return ans;
}


string toBin(ll n){
	if(n == 0) return "0";
	string ans = "";
	while(n > 0){
		ans = string(1, char(n % 2 + '0')) + ans;
		n /= 2;
	}
	return ans;
}

bool isAPrime(ll n) {
    if(n <= 1) return false;
    if(n == 2) return true;
    if(n % 2 == 0) return false;

    for(ll i = 3L; i * i <= n; i += 2L) {
        if(n % i == 0) {
            return false;
        }
    }
    return true;
}

ll nonTrivial(ll n){
	if(n % 2 == 0){
		return n/2;
	}
    for(ll i = 3L; i * i <= n; i += 2L) {
        if(n % i == 0) {
            return i;
        }
    }
	return -10;
}

int main(){
	cin >> T;
	for(int test = 1; test <= T; test++){
		cout << "Case #"<<test<<":" << endl;
		cin >> N >> J;
		for(int i = (1 << (N - 1)) + 1; i < (1 << N) && J; i += 2){
			bool ok = 1;
			vector<ll> resp;
			for(int j = 2; j <= 10; j++){
			    ll inDec = toDec(toBin(i), j);
				if(!isAPrime(inDec)){
					resp.push_back(nonTrivial(inDec));
				}else{
					ok = 0;
					break;
				}
			}
			if(ok){
				J--;
				cout << toBin(i);
				for(int j = 0; j < resp.size(); j++){
					cout << " " << resp[j];
				}
				cout << endl;
			}
		}
			
		
	}
	return 0;
}
