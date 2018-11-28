#include <iostream>
#include <vector>
using namespace std;

vector<int> parseGrid(){
	int row; 
	cin >> row;
	
	int care;
	vector<int> possible(4);
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(i == (row-1)){
				cin >> possible[j];
			} else {
				cin >> care;
			}
		}
	}
	
	return possible;
}

void JeMoeder(int caseNr){
	cout << "Case #" << (caseNr) << ": ";
	
	vector<int> run0 = parseGrid();	
	vector<int> run1 = parseGrid();

	
	int answer = -1;
	
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(run0[i] == run1[j]){
				if(answer != -1){
					cout << "Bad magician!" << endl;
					return;
				} else {
					answer = run0[i];
				}
			}
		}
	}
	
	if(answer == -1){
		cout << "Volunteer cheated!";
	} else {
		cout << answer;
	}
	
	cout << endl;
}

int main(){
	int runs; cin >> runs;
	for(int i = 1; i <= runs; i++){
		JeMoeder(i);
	}
}