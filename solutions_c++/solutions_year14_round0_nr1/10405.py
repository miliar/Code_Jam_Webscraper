#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <set>
using namespace std;

int A1[4][4];
int A2[4][4];

int main() {
	int T;
	ifstream in("A-small-attempt2.in");
	ofstream out("output.txt");
	cin >> T;
	int c = 1;
	while(T--) {
		int r1 , r2;

		cin >> r1; r1--;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
			    cin >> A1[i][j];
	
		cin >> r2; r2--;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				cin >> A2[i][j];
		
		int inters = 0;
		int index = 0;

		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				if(A1[r1][i] == A2[r2][j]) { inters++; index = i; break; }
		
		cout << "Case #" << c << ": ";
		
		if(inters == 1) cout << A1[r1][index] << '\n';
		else {
			if(inters == 0) cout << "Volunteer cheated!\n";
			else cout << "Bad magician!\n";
		}
		c++;
	}
	return 0;
}