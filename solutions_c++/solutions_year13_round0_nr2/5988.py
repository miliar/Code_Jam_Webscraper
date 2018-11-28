#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
int main(int argc, char *argv[]) {
	ifstream indata ("B-small-attempt0.in");
	ofstream outdata ("B-small-attempt0.out");
	string line;
	int t;

	if (indata.is_open()) {
		getline (indata, line);
		istringstream(line) >> t;
			
		for (int i=0; i<t; i++) {
			int n, m;
			getline (indata, line);
			istringstream(line) >> n >> m;
			
			int lawn[n][m];
			int rows[n];
			int cols[m];
			
			for (int j=0; j<n; j++) {
				rows[j] = 0;
			}
			
			for (int k=0; k<m; k++) {
				cols[k] = 0;
			}
			
			for (int j=0; j<n; j++) {
				getline (indata, line);
				
				for (int k=0; k<m; k++) {
					istringstream(line) >> lawn[j][k];
					rows[j] = max(rows[j], lawn[j][k]);
					cols[k] = max(cols[k], lawn[j][k]);
					if (k+1 != m)
						line = line.substr(2);
 				}
			}
			
			string outcome = "YES";
			// Time to cut grass
			for (int j=0; j<n; j++) {
				for (int k=0; k<m; k++) {
					// cout << min(rows[j], cols[k]) << " ";
					if (lawn[j][k] != min(rows[j], cols[k])) {
						outcome = "NO";
					}
				}
				// cout << endl;
			}
			
			outdata << "Case #" << i+1 << ": " << outcome << endl;
			cout << "Case #" << i+1 << ": " << outcome << endl;
		}
			
		outdata.close();
		indata.close();
	} else {
		cout << "File not found :( " << endl;
	}

}