#include<iostream>
#include<unordered_map>
#include <limits>
#include <fstream>
#include <string>

using namespace std;


int main()
{
	int noOfTests, value, multiplier,temp,digit,out;
	bool result = true;
	unordered_map<int, bool> hash;
	cin >> noOfTests;
	for (int i = 0; i < noOfTests; i++){
		cin >> value; multiplier = 1;
		hash.clear(); result = true;
		if (value == 0){
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			result = false;
		}
		while (result){
			//cout << "Inside while" << endl;
			out = value*multiplier;
			temp = out;
			while (temp){
			   digit = temp % 10;
		       temp = temp / 10;
			   if (hash.find(digit) == hash.end()){
				   hash[digit] = true;
			   }
			}
			if (hash.size() == 10){
				result = false;
			}
			else{
				multiplier++;
			}
		}
		if (value != 0){
			cout << "Case #" << i+1 << ": " << out << endl;
		}
	}

	cin.clear();
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	getchar();
}
