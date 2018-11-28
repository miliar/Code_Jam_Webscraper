#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		int input1, input2;
		int matrix[4][4];
		int answers[4];
		
		cin >> input1;
		input1 -= 1;
		cin >> matrix[0][0] >> matrix[0][1] >> matrix[0][2] >> matrix[0][3];
		cin >> matrix[1][0] >> matrix[1][1] >> matrix[1][2] >> matrix[1][3];
		cin >> matrix[2][0] >> matrix[2][1] >> matrix[2][2] >> matrix[2][3];
		cin >> matrix[3][0] >> matrix[3][1] >> matrix[3][2] >> matrix[3][3];
		
		answers[0] = matrix[input1][0];
		answers[1] = matrix[input1][1];
		answers[2] = matrix[input1][2];
		answers[3] = matrix[input1][3];

		cin >> input2;
		input2 -= 1;
		cin >> matrix[0][0] >> matrix[0][1] >> matrix[0][2] >> matrix[0][3];
		cin >> matrix[1][0] >> matrix[1][1] >> matrix[1][2] >> matrix[1][3];
		cin >> matrix[2][0] >> matrix[2][1] >> matrix[2][2] >> matrix[2][3];
		cin >> matrix[3][0] >> matrix[3][1] >> matrix[3][2] >> matrix[3][3];
		
		int correct = 0;
		int correctCount = 0;
		for(int j = 0; j <= 3; j++){
			for(int h = 0; h <=3; h++){
				if(matrix[input2][j] == answers[h]){
					correctCount++;
					correct = answers[h];
				}
			}
		}
		
		if(correctCount == 0){
			cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
		}else if(correctCount == 1){
			cout << "Case #" << i + 1 << ": " << correct << endl;
		}else if(correctCount > 1){
			cout << "Case #" << i + 1 << ": Bad magician!" << endl;
		}
	}
	return 0;
}