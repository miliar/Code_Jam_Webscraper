#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

int mm, k, n, a[1111];

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> k;
	
	for (int p = 0; p < k; p++){
		cin >> n;
		for (int i = 0; i < n; i++){
			cin >> a[i];
		}
		mm = 1000000000;
		for (int i = 1; i < 1000; i++){
			int kol = 0;
			for (int j = 0; j < n; j++){
				int x = a[j] - i;
				if (x <= 0) continue;
				kol +=  x / i;
				if (x % i != 0) kol++;
			}
			if (kol + i < mm) mm = kol + i;
		}
		cout << "Case #" << p + 1 << ":" << " " << mm << endl; 	
	}


	return 0;
}