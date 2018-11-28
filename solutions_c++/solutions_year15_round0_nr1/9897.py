//============================================================================
// Name        : GCJ11042015.cpp
// Author      : Fei Bi
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <queue>
#include <stdint.h>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
using namespace std;

unsigned int split(const string &txt, vector<string> &strs, char ch)
{
	//this is the general case
    size_t pos = txt.find( ch );
    size_t initialPos = 0;
    strs.clear();

    // Decompose statement
    while( pos != string::npos ) {
        strs.push_back( txt.substr( initialPos, pos - initialPos + 1 ) );
        initialPos = pos + 1;

        pos = txt.find( ch, initialPos );

    }

    // Add the last one
    strs.push_back(txt.substr( initialPos, min( pos, txt.size() ) - initialPos + 1 ) );

    //return the size of the vector
    return strs.size();
}



int main() {

	ifstream fin("A-small-attempt1.in");

	string line;

	getline(fin, line);

	int num = atoi (line.c_str());

	int index = 1;

	while (getline(fin, line)) {

		cerr << "======================" << endl;
		cerr << line << endl;

		vector <string> v;
		split(line, v, ' ');

		int max = atoi (v[0].c_str());

		string seq = v[1];

		vector <int> _seq;

		for (int i = 0; i < seq.size(); i++){

			_seq.push_back(atoi( seq.substr(i,1).c_str()));
			cerr << i << " => " << _seq[i] << endl;
		}

		int count_need = 0;

		int cur_person = 0;

		for (int i = 0; i < _seq.size(); i++){
			int add = 0;
			if (i != 0 ){
				if (_seq[i] != 0 && i > cur_person){
					add= i - cur_person;
					count_need += add;
				}

			}
			cur_person += _seq[i] + add;

			cerr << i << " needs => " << count_need << endl;
			cerr << i << " persons => " << cur_person << endl;
		}

		cout << "Case #" << index << ": " << count_need << endl;
		index ++;
	}


	return 0;
}















