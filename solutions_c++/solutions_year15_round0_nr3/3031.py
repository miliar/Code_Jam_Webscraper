// this makes no sense whatsoever...

#include <fstream>
#include <iostream>
#define min(a, b) ((a < b) ? a : b)
using namespace std;

const int prod[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};
const int val[8] = {1, 2, 3, 4, -1, -2, -3, -4};

int lv;
int stage[10], last, l, t, c, car[10010], k[10];
long long x;
string s;

int main() {
	ifstream fi("c.in");
	ofstream fo("c.out");
	fi >> t;
	int c = 0;
	while(t--) {
		c++;
		fi >> l >> x >> s;
		for (int i = 0; i < l; i++) {
			if (s[i] == 'i') car[i] = 2;
			if (s[i] == 'j') car[i] = 3;
			if (s[i] == 'k') car[i] = 4;
		}
		int last = 1;
		memset(stage, 0, sizeof(stage));
		memset(k, 0, sizeof(k));
		for (int i = 0; i < l; i++) {
			last = ((last < 0) ? (-1) : 1) * prod[abs(last) - 1][car[i] - 1];
			for (int v = 0; v < 8; v++) {
				int last_val = ((val[v] < 0) ? (-1) : 1) * ((last < 0) ? (-1) : 1) * prod[abs(val[v])-1][abs(last)-1];
				if (last_val == 2 && stage[v] == 0) 
					stage[v] = 1;
				else if (last_val == 4 && stage[v] == 1) {
					stage[v] = 2;
				}
				if (last_val == 4) k[v] = i+1;	
			}
		}
		int ok = false;
		int last_val = last;
		int total_stage = stage[0];
		if (stage[0] == 2) ok = true;
		int i, first_k = 0;
		if (k[0] and !first_k) first_k = k[0];
		for (i = 0; i < 10; i++) {
			lv = abs(last_val) + ((last_val < 0) ? 4 : 0) - 1;
			if (k[lv] and !first_k) first_k = (i+1) * l + k[lv];
			if (stage[lv] == 2) total_stage = 2, ok = true;
			else if (stage[lv] == 1 && total_stage == 0) total_stage = 1;
			else if (total_stage == 1 && k[lv]) total_stage = 2, ok = true;
			last_val = ((last_val < 0) ? (-1) : 1) * ((last < 0) ? (-1) : 1) * prod[abs(last) - 1][abs(last_val) - 1];
			if (last_val == 1) break;
		}
		int rest = (int)((long long)x % (long long)(i+2));
		//cerr << first_k;
		if (first_k && total_stage == 1) {
			//cerr << first_k + l * min(i+2, x);
			if (first_k + l * min(i+2, x) <= (long long)x*(long long)l) ok = true;
		}
		last_val = 1;
		for (i = 0; i < rest; i++) {
			last_val = ((last_val < 0) ? (-1) : 1) * ((last < 0) ? (-1) : 1) * prod[abs(last) - 1][abs(last_val) - 1];
		}

		fo << "Case #" << c << ": " << ((ok && last_val == -1) ? "YES" : "NO") << "\n";
	}
	return 0;
}