#include <iostream>
using namespace std;

int T;

int multab[4][4] = {
	{1, 2, 3, 4},
	{2, -1, 4, -3},
	{3, -4, -1, 2},
	{4, 3, -2, -1}
};

int mul(int a, int b) { return multab[abs(a)-1][abs(b)-1]*(a < 0? -1: +1)*(b < 0? -1: +1); }

int l, x;
string s;
int pm[10010];

bool yes() {
	int a = 1;
	for (int i = 0; i+1+1 < l*x; i++) {
		a = mul(a, s[i - i/l*l]-'i'+2);
		int b = 1;
		for (int j = i+1; j+1 < l*x; j++) {
			b = mul(b, s[j - j/l*l]-'i'+2);
			int c = pm[j+1];
			
			if (a == 2 && b == 3 && c == 4)
				return true;
		}
	}
	return false;
}

int main() {
	cin >> T;
	
	for (int lacase = 1; lacase <= T; lacase++) {
		cin >> l;
		cin >> x;
		
		cin >> s;
		
		pm[l*x] = 1;
		for (int i = l*x-1; i >= 0; i--)
			pm[i] = mul(s[i - i/l*l]-'i'+2, pm[i+1]);
		
		cout << "Case #" << lacase << ": " << (yes() ?"YES" :"NO") << "\n";
	}
	
	
	return 0;
}
