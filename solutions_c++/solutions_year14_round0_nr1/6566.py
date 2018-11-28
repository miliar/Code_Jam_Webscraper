#include<iostream>
#include<vector>

using namespace std;

void read(int array[4][4]) {
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> array[i][j];
}

int main () {
	int T; cin >> T;
	for (int test = 0; test < T; test++) {
		int array1[4][4], array2[4][4];	
		int p1, p2; 
		
		cin >> p1;
		read(array1);
		cin >> p2;
		read(array2);
		
		int found = 0, element = -1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (array1[p1 - 1][i] == array2[p2 - 1][j])
					found++, element = array1[p1 - 1][i];
		
		cout << "Case #" << test + 1 << ": ";
		if (found == 1) cout << element << endl;
		else if (found == 0) cout << "Volunteer cheated!" << endl;
		else cout << "Bad magician!" << endl;
	}
	return 0;
}