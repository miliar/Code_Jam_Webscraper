//============================================================================
// Name        : Osmos.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <list>
using namespace std;

void binary_insert(list<int>& L, int b) {
	list<int>::iterator i;
	i = L.begin();
	int idx = 0;
	while (*i < b && idx < L.size()) {
		++i;
		++idx;
	}
	L.insert(i, b);
}

void print_list(list<int>& L) {
	list<int>::iterator i;
	for(i=L.begin(); i != L.end(); ++i) cout << *i << " ";
	cout << endl;
}

int eat(int asize, list<int>& motes) {
	list<int>::iterator i;
	i = motes.begin();
	while (*i < asize && motes.size() > 0) {
		asize += *i;
		i = motes.erase(i);
	}
	return asize;
}

int main(int argc, char** argv) {
	ifstream infile;
	int ncases;
	infile.open(argv[1]);
	infile >> ncases;
	for (int i=0; i<ncases; ++i) {
		int asize;
		int nmotes;
		list<int> motes;
		infile >> asize;
		infile >> nmotes;
		for (int j=0; j<nmotes; ++j) {
			int tmp;
			infile >> tmp;
			binary_insert(motes, tmp);
		}
		asize = eat(asize, motes);
		int minimum = motes.size();
		int j = 1;
		while (motes.size() != 0) {
			asize += asize-1;
			if (asize == 1) {
				break;
			}
			asize = eat(asize, motes);
			int tmp = j + motes.size();
			if (tmp < minimum) {
				minimum = tmp;
			}
			++j;
		}
		cout << "Case #" << i+1 << ": " << minimum << endl;
	}
}
