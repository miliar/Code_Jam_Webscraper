#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
using namespace std;

typedef long long ll;

int letras[30];
string s;
vector<int> numeros;

//THREE NINE

int main() {

	int t;
	cin >> t;
	for(int i = 0; i < t; i++) {
		numeros.clear();
		memset(letras, 0, sizeof 0);
		cin >> s;
		int l = s.length();
		for(int j = 0; j < l; j++) {
			letras[(int)(s[j]-'A')]++;
		}
		while(letras[(int)('Z'-'A')] > 0) {
			numeros.pb(0);
			letras[(int)('Z'-'A')]--; letras[(int)('E'-'A')]--; letras[(int)('R'-'A')]--; letras[(int)('O'-'A')]--;
		}
		while(letras[(int)('G'-'A')] > 0) {
			numeros.pb(8);
			letras[(int)('E'-'A')]--; letras[(int)('I'-'A')]--; letras[(int)('G'-'A')]--; letras[(int)('H'-'A')]--; letras[(int)('T'-'A')]--;
		}
		while(letras[(int)('U'-'A')] > 0) {
			numeros.pb(4);
			letras[(int)('F'-'A')]--; letras[(int)('O'-'A')]--; letras[(int)('U'-'A')]--; letras[(int)('R'-'A')]--;
		}		
		while(letras[(int)('F'-'A')] > 0) {
			numeros.pb(5);
			letras[(int)('F'-'A')]--; letras[(int)('I'-'A')]--; letras[(int)('V'-'A')]--; letras[(int)('E'-'A')]--;
		}
		while(letras[(int)('X'-'A')] > 0) {
			numeros.pb(6);
			letras[(int)('S'-'A')]--; letras[(int)('I'-'A')]--; letras[(int)('X'-'A')]--;
		}
		while(letras[(int)('S'-'A')] > 0) {
			numeros.pb(7);
			letras[(int)('S'-'A')]--; letras[(int)('E'-'A')]--; letras[(int)('V'-'A')]--; letras[(int)('E'-'A')]--; letras[(int)('N'-'A')]--;
		}
		while(letras[(int)('W'-'A')] > 0) {
			numeros.pb(2);
			letras[(int)('T'-'A')]--; letras[(int)('W'-'A')]--; letras[(int)('O'-'A')]--;
		}
		while(letras[(int)('O'-'A')] > 0) {
			numeros.pb(1);
			letras[(int)('O'-'A')]--; letras[(int)('N'-'A')]--; letras[(int)('E'-'A')]--;
		}
		while(letras[(int)('T'-'A')] > 0) {
			numeros.pb(3);
			letras[(int)('T'-'A')]--; letras[(int)('H'-'A')]--; letras[(int)('R'-'A')] -= 2; letras[(int)('E'-'A')]--;
		}
		while(letras[(int)('N'-'A')] > 0) {
			numeros.pb(9);
			letras[(int)('N'-'A')] -= 2; letras[(int)('I'-'A')]--; letras[(int)('E'-'A')]--;
		}
		sort(numeros.begin(), numeros.end());
		cout << "Case #" << i + 1 << ": ";
		l = numeros.size();
		for(int j = 0; j < l; j++)
			cout << numeros[j];
		cout << endl;
	}

	return 0;
}
