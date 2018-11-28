#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
VI v;

bool check(){
	for (int i = 0; i<10; ++i){
		if (v[i] == 0) return true;
	}
	return false;
}

void add(long long a){
	while (a != 0){
		v[a%10] = 1;
		a /= 10;
	}
}

int main(){
	long long T,n;
	cin >> T;
	for (int i = 0; i < T; ++i){
		cin >> n;
		v = VI (10,0);
		int counter = 1;
		while (check() and counter < 72){
			add(n*counter);
			++counter;
		}
		cout << "Case #" << i+1 <<": ";
		if (check()) cout << "INSOMNIA\n";
		else cout << (counter-1) * n <<'\n';
	}
}
