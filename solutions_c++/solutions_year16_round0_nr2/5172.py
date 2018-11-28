#include <iostream>
#include <string>
using namespace std;

string flip(string newStr, size_t index){
	for (size_t i = 0; i < index; i++)
	{
		if (newStr.at(i) == '-'){
			newStr.at(i) = '+';
		}
		else{
			newStr.at(i) = '-';
		}
	}
	return newStr;
}

int main(){
	int iTestCases = 0;
	cin >> iTestCases;
	for (int i = 1; i <= iTestCases; i++){
		int iCount = 0;
		string sInput;
		cin >> sInput;

		for (int j = sInput.length() - 1; j >= 0; j--)
		{
			if (sInput.at(j) == '-'){
				sInput = flip(sInput, j);
				iCount++;
			}
		}
		cout << "Case #" << i << ": " << iCount << endl;
	}
	return 0;
}