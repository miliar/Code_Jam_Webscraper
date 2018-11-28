#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<deque>
using namespace std;


int main(){
	ifstream cin;
	ofstream cout;
	cin.open("A-small-attempt1.in");
	cout.open("outputz.txt");

	int t;
	cin >> t;
	for (int kh = 0; kh < t; kh++){
		int r;
		cin >> r;
		int a[5][5];
		vector<int> v1, v2;
		for (int i = 1; i <= 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> a[i][j];
				if (i  == r) v1.push_back(a[i][j]);
			}
		}
		cin >> r;
		for (int i = 1; i <= 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> a[i][j];
				if (i  == r) v2.push_back(a[i][j]);
			}
		}
		int cnt = 0;
		int number = -1;
		for (int i = 0; i < v1.size(); i++){

			for (int j = 0; j < v2.size(); j++){
				if (v1[i] == v2[j]) {
					cnt++;
					number = v1[i];
				}

			}
		}
		

		cout << "Case #" << kh + 1 << ": ";
		if (cnt == 1) cout << number;
		else if (cnt == 0) cout << "Volunteer cheated!"; 
		else cout << "Bad magician!";


		cout << endl;

	}



	return 0;
}