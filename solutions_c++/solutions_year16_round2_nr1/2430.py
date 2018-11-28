#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int tcase = 1; tcase <= t; tcase++) {
		int val[11];
		for (int i = 0; i <= 9; i++)
			val[i] = 0;
		string str;
		cin >> str;
		int z = 0, w = 0, t = 0, h = 0;
		int g = 0, u = 0, f = 0, x = 0, s = 0, n = 0, o = 0, i = 0;
		for (unsigned int ii = 0; ii < str.size(); ii++) {
			switch(str[ii]) {
				case 'Z' : z++; break;
				case 'W' : w++; break;
				case 'T' : t++; break;
				case 'H' : h++; break;
				case 'G' : g++; break;
				case 'U' : u++; break;
				case 'F' : f++; break;
				case 'X' : x++; break;
				case 'S' : s++; break;
				case 'N' : n++; break;
				case 'O' : o++; break;
				case 'I' : i++; break;
				default: break;
			}
		}
		val[0] = z;
		val[1] = o - z - (t- h)-u;
		val[2] = t - h;
		val[3] = h - g;
		val[4] = u;
		val[5] = f - u;
		val[6] = x;
		val[7] = s -x;
		val[8] = g;
		val[9] = i - (f - u) - x - g;
		
		printf("Case #%d: ", tcase);
		for (int ii = 0; ii <= 9; ii++)
			for (int j = 1; j <= val[ii]; j++)
				printf("%d", ii);
		printf("\n");
		
	}
	return 0;
}
