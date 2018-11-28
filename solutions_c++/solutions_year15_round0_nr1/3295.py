#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#define int long long

using namespace std;

int n;

string S;

bool sprawdz(int x) {
	int juz = x;
	for(int i = 0; i < S.size(); ++i) {
		if(x >= i) 
			x += (S[i] - '0');
		else 
			return false;
	}
	return true;
}
 main() {
	int z; cin >> z;
	int g = z;
	while(z--) {
		cin >> n;
		cin >> S;
		int l = 0; int p = S.size();
		while(l < p) {
			int s = (l+p)/2;
			if(sprawdz(s)) 
				p = s;
			else
				l = s+1;;
		}
		cout << "Case #" << (g-z) << ": " << l<< endl;

	}
}
