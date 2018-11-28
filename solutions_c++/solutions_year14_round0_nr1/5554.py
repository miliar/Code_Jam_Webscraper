#include<iostream>
#include<set>
#include<vector>
#include<fstream>

using namespace std;

int main(){
	ifstream cin("A-small-attempt0.in");
	ofstream cout("A-small-attempt0.out");
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){

		int mat1[4][4];
		set<int> mat2[4];

		int ans1, ans2;
		cin >> ans1;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> mat1[i][j];
		cin >> ans2;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++){
			int x;
			cin >> x;
			mat2[i].insert(x);
		}

		ans1--; ans2--;
		int cnt = 0, y;
		for (int i = 0; i < 4; i++){
			if (mat2[ans2].find(mat1[ans1][i]) != mat2[ans2].end()){
				y = mat1[ans1][i];
				cnt++;
			}
			if (cnt == 2){
				break;
			}
		}
		cout << "Case #" << (t + 1) << ": ";
		switch (cnt){
		case 0:
			cout << "Volunteer cheated!";
			break;
		case 1:
			cout << y;
			break;
		case 2:
			cout << "Bad magician!";
			break;
		}
		cout << "\n";
	}
	cin.close();
	cout.close();
}