#include <iostream>
#include <vector>
using namespace std;

vector<int> compareLists(vector<int> row1, vector<int> row2){
	vector<int> results;
	for(int i = 0; i < row1.size(); i++){
		for(int j = 0; j < row2.size(); j++){
			if(row1[i] == row2[j]){
				results.push_back(row1[i]);
			}
		}
	}
	return results;
}

int main() {
	int tests = 0;
	cin >> tests;
	int testcase = 1;
	while(tests){
		int choice1 = 0;
		int choice2 = 0;
		cin >> choice1;
		choice1 -= 1;
		vector<int> layout1;
		int card = 0;
		for(int i = 0; i < 16; i++){
			cin >> card;
			layout1.push_back(card);
		}
		vector<int> chosenrow1;
		for(int i = choice1*4; i < (16-(4-(choice1+1))*4); i++){
			chosenrow1.push_back(layout1[i]);
		}
		cin >> choice2;
		choice2 -= 1;
		vector<int> layout2;
		for(int i = 0; i < 16; i++){
			cin >> card;
			layout2.push_back(card);
		}
		vector<int> chosenrow2;
		for(int i = choice2*4; i < (16-(4-(choice2+1))*4); i++){
			chosenrow2.push_back(layout2[i]);
		}
		vector<int> results = compareLists(chosenrow1, chosenrow2);
		if(results.size() == 1){
			cout << "Case #" << testcase << ": " << results[0] << endl;
		}
		else if(results.size() > 1){
			cout << "Case #" << testcase << ": Bad magician!" << endl;
		}
		else{
			cout << "Case #" << testcase << ": Volunteer cheated!" << endl;
		}
		testcase++;
		tests--;
	}
	return 0;
}