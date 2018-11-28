#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

void evaculate_one(char senator, int senator_num) {
	while(senator_num) {
		if(senator_num>=2) {
			cout << senator << senator << " ";
			senator_num--;
			senator_num--;
		} else {
			cout << senator << " ";
			senator_num--;
		}
	}
}

void evaculate_two(char first, char second, int senator_num) {
	while(senator_num>0) {
		senator_num--;
		cout << first << second << " ";
	}
	cout << endl;
	return;
}

void evaculate(vector<int> * senators, int party_number) {
	if(party_number==2) {
		evaculate_two('A','B',senators->at(0));
	} else if (party_number==3) {
		int a = senators->at(0);
		int b = senators->at(1);
		int c = senators->at(2);
		if(a==b) {
			evaculate_one('C',c);
			evaculate_two('A','B',a);
		} else if(a==c) {
			evaculate_one('B',b);
			evaculate_two('A','C',a);
		} else if (b==c) {
			evaculate_one('A',a);
			evaculate_two('C','B',b);
		} else if (a>b && a>c) {
			senators->at(0)--;
			cout << "A ";
			evaculate(senators,party_number); 
		} else if (b>a && b>c) {
			senators->at(1)--;
			cout << "B ";
			evaculate(senators,party_number);
		} else {
			senators->at(2)--;
			cout << "C ";
			evaculate(senators,party_number);
		}
	}
}

int main() {
	string line;
	int testNum;
	getline(cin, line);
	stringstream ss(line);
	ss >> testNum;
	int ct = 1;
	while(testNum > 0) {
		int party_number;
		getline(cin, line);
		stringstream num(line);
		num >> party_number;
		cout << "Case #" << ct << ": ";
		vector<int> * senators = new vector<int>(26);
		getline(cin,line);
		stringstream ss1(line);
		for(int i = 0; i < party_number; i++) {
			int senator_num;
			ss1 >> senator_num;
			senators->at(i) = senator_num;
		}
		evaculate(senators,party_number);
		testNum--;
		ct++;
	}
	return 0;
}