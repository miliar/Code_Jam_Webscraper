/***************
 * Viktor Kvaternjak
 * Google Code Jam 2014
 * **************/

#include <iostream>

using namespace std;

void solve(int test_case){
	int first_answer, second_answer;
	int first_matrix[4][4], second_matrix[4][4];
	
	cin >> first_answer;
	
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j<4; ++j)
			cin >> first_matrix[i][j];
			
	cin >> second_answer;
	
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j<4; ++j)
			cin >> second_matrix[i][j];
	
	first_answer --; 
	second_answer --;
	
	int num_sol = 0;
	int last_sol = 0;
	for (int i = 0; i < 4; ++i){
		for (int j = 0; j<4; ++j){
			if (first_matrix[first_answer][i] == second_matrix[second_answer][j]){
				num_sol ++;
				last_sol = first_matrix[first_answer][i];
			}
		}
	}
	cout << "Case #"<< test_case << ": ";
	if (num_sol == 0)
		cout << "Volunteer cheated!";
	else if (num_sol == 1)
		cout << last_sol;
	else cout << "Bad magician!";
	cout << endl;	
}

int main(void){
	int n;
	cin >> n;
	for (int i = 0; i < n; i++){
		solve(i+1);
	}
	return 0;
}
