#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){

	// Decleration
	ofstream fout ("A-small-attempt5.out");
	ifstream fin ("A-small-attempt5.in");
	int T, temp;
	vector<int> solutions1;
	vector<int> solutions2;

	// Get number of test Cases
	fin >> T;

	for(int i = 0; i < T; i++){
		int R;
		//First Input
		fin >> R;
		R--;
		for(int j = 0; j < 4; j++){
			for (int q = 0; q < 4; q++){
				fin >> temp;
				if(j==R){
					solutions1.push_back(temp);
				}
			}
		}

		//Second Input
		fin >> R;
		R--;
		for(int j = 0; j < 4; j++){
			for (int q = 0; q < 4; q++){
				fin >> temp;
				if(j==R){
					for(int k = 0; k < solutions1.size(); k++){
						if(temp == solutions1[k]){
							solutions2.push_back(temp);
						}
					}
				}
			}
		}
		fout << "Case #" << i+1 << ": ";
		if(solutions2.size() == 1){
			fout << solutions2[0];
		}
		else if(solutions2.size() == 0){
			fout << "Volunteer cheated!";
		}
		else{
			fout << "Bad magician!";
		}
		if(i != T-1){
			fout << "\n";
		}

		solutions1.clear();
		solutions2.clear();
	}

	fout << endl;

	return 0;
}