#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

int v[10];

void mark(ll x){
	while(x){
		v[x%10] = 1;
		x/=10;
	}
}

bool check(){
	int x = 0;
	for(int i = 0; i < 10; i++){
		x+=v[i];
	}
	return x == 10;
}

int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;	
	for(int t = 1; t <= T; t++){
		ll n;
		cin >> n;
		memset(v, 0, sizeof v);
		bool ok = false;
		for(ll i = 1; i <= 10000000; i++){
			mark(i*n);
			if(check())	{
				cout << "Case #" << t << ": " << i*n << endl;
				ok = true;
				break;
			}
		}
		if(!ok){
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}
	}
	
	return 0;
}
