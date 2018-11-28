#include <bits/stdc++.h>
using namespace std;
int main (){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int z;
	cin >> z;
	for (int i = 0; i < z; ++i){
		int x = 0;
		int a;
		cin >> a;
		int num = 0;
		int b = a;
		if (b){
			vector <bool> A (10, 0);
			while (num != 10){
				++x;
				function <void(int)> f = [&](int c){
					if (c >= 10)f(c/10);
					if (A[c%10] == 0){
						A[c%10] = 1;
						++num;
					}
				};
				f(b);
				b += a;		
			}
		}
		b -= a;
		if (a)cout << "Case #" << i+1 << ": " << b<<'\n'; 
		if(!a){
			cout << "Case #" << i+1 << ": " << "INSOMNIA\n"; 
		}
	}
}
