/*
 * main.cpp
 *
 *  Created on: 12/04/2013
 *      Author: Eden
 */
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool isRezef(string str){
	for (unsigned int i=0;i<str.length();i++){
		if (str[i] == 'a'||str[i] == 'e'||str[i] == 'i'||str[i] == 'o'||str[i] == 'u'){
			return false;
		}
	}
	return true;
}

int findRezef(string name, int i, int n, int* s, int* e) {
	if (i+n-1 > name.length()-1)
		return -1;
	string sub = name.substr(i,n);
	if (isRezef(sub)) {
		*s = i;
		*e = i + n - 1;
		return 0;
	}
	i++;
	while (i + n - 1 < name.length()) {
		sub = name.substr(i,n);
		if (isRezef(sub)) {
			*s = i;
			*e = i + n - 1;
			return 0;
		}
		++i;
	}
	return -1;
}

int main() {
	ifstream myfile("C:\\users\\eden\\jam\\a.in");
	ofstream output("C:\\users\\eden\\jam\\out.txt");
	if (!myfile || !output) {
		cout << "FAIL";
		return 0;
	}
	int T, n, s, e, first, sum = 0,last;
	;
	string name;
	myfile >> T;
	for (int i = 1; i <= T; i++) {
		output << "Case #" << i << ": ";
		myfile >> name;
		myfile >> n;
		int temp = findRezef(name, 0, n, &s, &e);
		if (temp == -1){
			output<<0<<endl;
			continue;
		}
		//first = s;
		last = s;
		sum += (s + 1) * (name.length() - e);
		while (findRezef(name, s + 1, n, &s, &e) != -1) {
			sum += (s -last) * (name.length() - e);
			last = s;
		}
		output << sum << endl;
		sum = 0;
	}
	myfile.close();
	output.close();
	return 0;
}

