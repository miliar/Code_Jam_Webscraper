#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string numbers[10] = {"ZERO","TWO","EIGHT","THREE","FOUR","SIX","ONE","NINE","FIVE","SEVEN"};
int actualNumbers[10] = {0,2,8,3,4,6,1,9,5,7};

int main(){
	int TC, c = 1;
	cin >> TC;
	while (TC--){
		string letters;
		cin >> letters;
		vector<int> answers;
		int i = 0;
		int n = 11;
		while (letters != ""){
			string num = numbers[i];
			vector<int> posToRemove;
			for (int j = 0; j < letters.length(); j++){
				char charToCheck = letters[j];
				for (int k = 0; k < num.length(); k++){
					if (num[k] == charToCheck){
							posToRemove.push_back(j);
							num.erase(k,1);
							break;
					}
				}
			}
			if (num.length() == 0){
				int count = 0;
				for (int k = 0; k < posToRemove.size(); k++){
					letters.erase(posToRemove[k]-count,1);
					count++;
				}
				answers.push_back(actualNumbers[i]);
			}
			else{
				i++;
			}
		}
		cout << "Case #" << c++ << ": ";
		sort(answers.begin(),answers.end());
		for (int i = 0; i < answers.size(); i++){
			cout << answers[i];
		}
		cout << endl;
	}
}