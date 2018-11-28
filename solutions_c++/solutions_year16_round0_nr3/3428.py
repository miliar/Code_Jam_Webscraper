#include<bits/stdc++.h>

using namespace std;

#define endl '\n'
#define rep(i , n) for( int i = 0; i < (n); i++ )

typedef long long ll;
typedef pair<int, int> pii;


bool isprime(ll x){
	
	for( ll i = 2; i * i <= x; i++ ){
		if(x % i == 0)
			return false;
	}
	return true;
}

ll first_div(ll x){
	
	for( ll i = 2; i * i <= x; i++ ){
		if(x % i == 0)
			return i;
	}
	assert(false);
	return -1;
}

int N , J;

ll get_num(ll x , ll b){
	
	ll res = 0;	
	for( ll i = 62; i >= 0; i-- ){
		if(x & (1LL << i))
			res = res * b + 1;
		else res = res * b + 0;
	}
	return res;
}

string base_two(ll x){
	
	string sol = "";
	do{
		sol = sol + (char)(x % 2 + '0');
		x >>= 1;
	}
	while(x > 0);
	reverse(sol.begin() , sol.end());
	return sol;
}



int main(){

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int tc;
	cin >> tc;
	cin >> N >> J;
	
	cout << "Case #1:" << endl;
	int n = N - 2;
	vector<ll> nums;
	for( int mask = 0; mask < (1 << n); mask++ ){
		ll currmask = ((mask | (1 << n)) << 1) + 1;		
			
		if(nums.size() >= J)continue;
		
		bool flag = true;
		for( int i = 2; i <= 10; i++ ){			
			ll num = get_num(currmask, i);			
			if(isprime(num)){				
				flag = false;
				break;
			}
		}
		
		if(flag){
			nums.push_back(currmask);						
		}
	}
	
	for(auto v : nums){
		cout << base_two(v) << " ";
		for( int i = 2; i <= 10; i++ ){			
			ll num = get_num(v, i);		
			cout << first_div(num) << " \n"[i == 10];
		}
	}	
}
