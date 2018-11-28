#include <fstream>
#include <iostream>

using namespace std;

int main () {
	ifstream f;
	f.open("input.txt");
	
	ofstream g;
	g.open("output.txt");
	
	int n;
	f >> n;
	
	int x, y;
	int * table;
	for (int i = 0; i < n; i++) {
		f >> x >> y;
		table = new int[x*y];
		
		for (int j = 0; j < x; j++) {
			for (int k = 0; k < y; k++) {
				f >> table[j*y + k];
			}
		}
/*	
for (int j = 0; j < x; j++) {
	for (int k = 0; k < y; k++) {
		cout << table[j*y + k] << " ";
	}
	cout << endl;
}
*/
		
		bool possible = true;
		int j = 0;
		while ( j < x && possible ) {
			int k = 0;
			while ( k < y && possible) {
				int temp = j*y + k;
//cout << j+1 << " " << k+1 << endl;
				bool a = false;				// is there bigger then him
				bool b = false;
				
				int l = 0;
				while (l < x && !a) {
					if (table[temp] < table[l*y + k]) {
						a = true;
						//cout << table[temp] << "<" << table[l*y + k] << endl;
					}
					//else cout << table[temp] << ">=" << table[l*y + k] << endl;
					l++;
				}
				
				l = 0;
				while (l < y && !b) {
					if (table[temp] < table[j*y + l]) {
						b = true;
						//cout << table[temp] << "<" << table[j*y + l] << endl;
					}
					//else cout << table[temp] << ">=" << table[j*y + l] << endl;
					l++;
				}
				
				if (a && b) possible = false;
				
				k++;
			}
			
			j++;
		}
		
		g << "Case #" << i+1 << ": " << (possible ? "YES" : "NO") << endl;
	}
	
	return 0;
}
