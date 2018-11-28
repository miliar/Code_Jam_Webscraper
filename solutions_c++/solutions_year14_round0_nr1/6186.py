#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ofstream fout("s1.out", ofstream::out);
	int T, row1, p1[4][4],row2, p2[4][4],number;
	cin >> T;
	
	char **str = new char*[T];
	for (int i = 0; i < T; i++){
		str[i] = new char[30];
	}
	for (int i = 0; i < T; i++){
		int count = 0;
		cin >> row1;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				cin >> p1[j][k];
			}
		}
		cin >> row2;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				cin >> p2[j][k];
			}
		}
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				if (p1[row1-1][j] == p2[row2-1][k]){
					number = p1[row1-1][j];
					count++;
				}
			}
		}
		if (count == 0){
			str[i] = " Volunteer cheated!";
		}
		if (count == 1){
			if (number >= 10){
				str[i][0] = ' ';
				str[i][1] = (number - number % 10) / 10 + '0';
				str[i][2] = number % 10 + '0';
				str[i][3] = '\0';
			}
			else{
				str[i][0] = ' ';
				str[i][1] = number + '0';
				str[i][2] = '\0';
			}

		}
		if (count > 1){
			str[i] = " Bad magician!";
		}
	}
	for (int i = 0; i < T; i++){
		fout << "Case #" << i + 1 << ':' << str[i]<<endl;
	}
	return 0;
}