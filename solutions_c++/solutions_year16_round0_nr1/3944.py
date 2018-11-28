#include<bits/stdc++.h>

using namespace std;

#define endl '\n'
#define rep(i , n) for( int i = 0; i < (n); i++ )

typedef long long ll;
typedef pair<int, int> pii;

bool d[10];
int get(){
	int res = 0;
	for( int i = 0; i < 10; i++ )
		if(d[i])res++;
	return res;
}

void add(ll x){
	do{
		d[x % 10] = true;
		x /= 10;
	}while(x > 0);
}

ll solve(ll x){
	memset(d , 0 , sizeof d);
	ll it = 0;
	do{
		
		add(x * ++it);
	}while(get() != 10);
	
	return x * it;
}

int main(){

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int tc;
	cin >> tc;
	for(int cc = 1; cc <= tc; cc++ ){
		cout << "Case #" << cc << ": ";
		ll x;
		cin >> x;
		if(x == 0)
			cout << "INSOMNIA" << endl;
		else cout << solve(x) << endl;
	}
	
	/*
	//cerr << solve(1692) << endl;
	for( int i = 1;  i <= 1000000; i++ ){
		solve(i);
		//cout << solve(i) << endl;
	}
	
	cerr << "OK" << endl;
	*/
}
