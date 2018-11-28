#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h> 
#include <sstream>
#include <map>
using namespace std;
int stringtoInt(string input);
string IntToString(int input);
int main(){
	int input,nothing;
	cin >> input;
	string number;
	map<char, bool> bigMap;
	
	for (int i = 0; i <input; i++){
		number = "";
		cin >> number;
		if (stringtoInt(number) == 0){
			cout << "Case #" + IntToString(i+1) + ": INSOMNIA" << endl;
		}
		else{
			bigMap['0'] = false; bigMap['1'] = false; bigMap['2'] = false; bigMap['3'] = false;
			bigMap['4'] = false; bigMap['5'] = false; bigMap['6'] = false; bigMap['7'] = false;
			bigMap['8'] = false; bigMap['9'] = false;
			int multiplier = 1;
			string checker="";
			while (!(bigMap['0'] && bigMap['1'] && bigMap['2'] && bigMap['3'] && bigMap['4'] && bigMap['5'] &&
				bigMap['6'] && bigMap['7'] && bigMap['8'] && bigMap['9'])){
				checker = IntToString(stringtoInt(number)*multiplier);
				for (int j = 0; j < checker.length(); j++){
					
					bigMap[checker[j]] = true;
				}
				multiplier=multiplier+1;
			}
			cout<< "Case #" << i+1 << ": "<< checker << endl;
		}

	}

}

int stringtoInt(string input){
	stringstream ss(input);
	int x;
	ss >> x;
	return x;
}


string IntToString(int input){
	stringstream ss;
	ss << input;
	return ss.str();
}