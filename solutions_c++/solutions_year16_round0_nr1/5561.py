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
#define MAXN 20350
#define ll long long int
#define INF 0xffffff
#define PI acos(-1)
#define MOD 1000000007LL
 
using namespace std;
 
int func(ll n){
	int mask = 0;
	if(n == 0) mask = 1;
	while(n > 0){
		mask |= (1 << (n % 10));
		n /= 10;
	}
	return mask;
}

string print(int n){
	string ans = "";
	if(n == 0) ans = "0";
	while(n > 0){
		ans = string(1,char('0'+(n%2)) ) + ans;
		n /= 2;
	}
	return ans;
}

ll track(ll n, int mask){
	ll total = 1;
	while(mask != (1 << 10) - 1 && total < 1000){
		mask |= func(n*total);
		total++;
	}
	if(mask != (1 << 10) - 1){
		return -1;
	}
	return (total - 1) * n;
}

int T;
ll N;

int main(){
	cin >> T;
	for(int test = 1; test <= T; test++){
		cin >> N;
	    ll ans = track(N, 0);
		if(ans == -1){
			cout << "Case #"<< test <<": INSOMNIA" << endl;
		}else{
			cout << "Case #"<< test <<": " << ans << endl;
		}
	}
	return 0;
}
