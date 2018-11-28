#include <iostream>
#include <string>
using namespace std;

string GetLastWord(string str){
	int strLen = str.length();
	int i = 0;
	string temp = "";
	temp += str.at(i);
	i++;
	while (i < strLen)
	{
		if (temp.at(0) <= str.at(i)){
			temp = str.at(i) + temp;
		}
		else{
			temp += str.at(i);
		}
		i++;
	}
	return temp;
}

int main(){
	int testCases = 0;
	string word;
	cin >> testCases;
	for (int i = 1; i <= testCases; i++)
	{
		cin >> word;
		word = GetLastWord(word);
		cout << "Case #" << i << ": " << word << endl;
	}
	
	return 0;
}