// Problem A
# include <iostream>
# include <vector>
using namespace std;

int intersect(vector<int> R, vector<int> S){
	int a = 0;
	int b = 0;
	for (int v = 0; v < 4; v++){
		for (int u = 0; u < 4; u++){
			if (R[u] == S[v]) {a = R[u]; b++;}
		}
	}
	if (a == 0) return -1;
	if (b > 1) return 0;
	return a;

}

bool debug  = false;
int main(){
	int T;
	cin >> T;
	for (int u = 1; u <= T; u++){
		int row_1;
		cin >> row_1;
		vector<vector<int> > A (4, vector<int> (4,0)) ;

		for (int i = 0; i < 4; i++)
			for (int j = 0; j<4; j++)
				cin >> A[i][j];

		vector<int> Row_1 = A[row_1-1];
		if (debug) cout << Row_1[0] << " " << Row_1[1] << " " << Row_1[2] << " " << Row_1[3] << endl;
		int row_2;
		cin >> row_2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j<4; j++)
				cin >> A[i][j];
		vector<int> Row_2 = A[row_2-1];
		if (debug) cout << Row_2[0] << " " << Row_2[1] << " " << Row_2[2] << " " << Row_2[3] << endl;
		int c = intersect(Row_1, Row_2);
		cout << "Case #" << u<<": ";
		if (c > 0) cout << c;
		if (c == 0) cout << "Bad magician!";
		if (c == -1) cout << "Volunteer cheated!";
		cout << endl;
	}

}
