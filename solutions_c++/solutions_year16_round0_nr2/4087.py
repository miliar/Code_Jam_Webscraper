#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <vector>

using namespace std;

void print(vector<char> *myVec) {
	for(int i = 0; i < myVec->size(); i++) {
		cerr << myVec->at(i) << " ";
	}
	cerr << endl;
}

void flip(vector<char> * myVec, char first) {
	//cerr << "flip " << endl;
	//print(myVec);
	int range = myVec->size();
	if(first == '+') {
		for(int j = myVec->size()-1; j >= 0; j--) {
			if(myVec->at(j)=='+') {
				range = j+1;
				break;
			}
		}
	}
	//cerr<< "range is " << range << endl;
	for(int i = 0; i < range; i++) {
		if(myVec->at(i)=='+') {
			myVec->at(i) = '-';
		} else {
			myVec->at(i) = '+';
		}
	}
	reverse(myVec->begin(),myVec->end());
	//cerr << "after " << endl;
	//print(myVec);
}

int pancake(vector<char> * myVec, char first, int counter) {
    //cerr << "counter is " << counter << endl;
    //print(myVec);
	while (myVec->size() && myVec->back() == '+') {
		myVec->pop_back();
	}
	if(myVec->size() == 0) return counter;
	flip(myVec,first);
	counter++;
	return pancake(myVec,myVec->at(0),counter);
}

int main() {
	string line;
	int testNum;
	getline(cin, line);
	stringstream ss(line);
	ss >> testNum;
	int ct = 1;
	while(testNum > 0) {
		int number;
		getline(cin, line);
		vector<char> * myVec = new vector<char>;
		for(int i = 0; i < line.size(); i++) {
			myVec->push_back(line[i]);
		}
		int flip_num = pancake(myVec,line[0],0);
		cout << "Case #" << ct << ": " << flip_num << endl;
		testNum--;
		ct++;
	}
	return 0;
}