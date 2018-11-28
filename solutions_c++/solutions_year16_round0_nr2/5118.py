#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stack>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

string reverse(string str, int n){
	for (int i = 0; i <= n; i++){
		if (str[i] == '+'){
			str[i] = '-';
		}

		else{
			str[i] = '+';
		}
	}

	return str;
}

int solve(string str){
	//cout << "str" << str << endl;

	if (str.size() == 1){
		if (str[0] == '+'){
			return 0;
		}
		else{
			return 1;
		}
	}

	else{
	  for (int i = str.size()-1; i >=0; i--){
	  	//cout << "i" << i << endl;
		if (str[i] == '-'){
			return solve(reverse(str, i)) + 1;
		}
	  }
    }
}

int main(){
	stack<char> S;
	string temp;
	string sub;
	string line;
	int num;

	getline(cin,line);
	istringstream ss(line);
	ss >> num;

	int j = 0;
	while(getline(cin,line)){
		j++;
		istringstream ss(line);
		ss >> temp;
		cout << "Case #" << j << ": " << solve(temp) << endl;
	}
}