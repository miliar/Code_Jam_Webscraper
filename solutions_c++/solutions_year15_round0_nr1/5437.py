#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

int n, k;
string s;

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> k;
	
	for (int p = 0; p < k; p++){
		cin >> n >> s;
		int kol = 0;
		int ans = 0;
		for (int j = 0; j <= n; j++){
			if (kol >= j) kol += (s[j] - 48);else{
				ans += (j - kol);
				kol = j;
				kol += (s[j] - 48);
			}
		}
		
		cout << "Case #" << p + 1 << ":" << " " << ans << endl; 	
	}


	return 0;
}