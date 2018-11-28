#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (n); i++)
#define fornn(i, q, n) for (int i = (q); i < (n); i++)
#define times clock() * 1.0 / CLOCKS_PER_SEC

using namespace std;

typedef long long ll;

set<int> S;


void up(ll v){
	while(v > 0){
		S.insert(v % 10);
		v /= 10;
	}
}

int main(){
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int count;
	cin >> count; 
	forn(i, count){
		ll n;
		cin >> n;
		ll t = n;  
		if (n == 0){
			cout << "Case #" << i + 1 << ": ";
			puts("INSOMNIA");
			continue;
		}
		S.clear();
		do{
			up(n);
			n += t;
		} while (S.size() < 10);
		cout << "Case #" << i + 1 << ": " << n - t << endl;
	}
	return 0;
}