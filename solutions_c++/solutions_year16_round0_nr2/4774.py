#include <iostream>
#include <fstream>
#include <string>
#include<cstdlib>
#include<vector>
#include <sstream>
#include <algorithm>
#include <Iterator>
using namespace std;

void printStack(vector<char>* pancakes) {
	for (vector<char>::const_iterator i = pancakes->begin(); i != pancakes->end(); ++i)
	    cout << *i << ' ';
	cout<<"\n";
}
int readNextInt(ifstream *file) {
	string str;
	getline(*file, str);
	return(atoi(str.c_str()));
}

int find_back(vector<char>* pancakes, int start, char val) {
	int i=start;
	while (i>-1) {
		if (pancakes->at(i) == '+') {
			return i;
		}
		i--;
	}
	return -1;
}

void stackflip(vector<char>* pancakes, int start, int end) {
	//cout<<"Flipping "<<start <<" to "<<end<<"\n";
	int i = 0;
	for(i=start; i<=end; i++) {
		if(pancakes->at(i) == '+') {
			pancakes->at(i) = '-';
		}
		else {
			pancakes->at(i) = '+';
		}
	}
	reverse(pancakes->begin()+start, pancakes->begin()+end+1);
	//printStack(pancakes);
}

long solve (string S) {
	int length = S.length();
	if (length == 0) {
		return 0;
	}
	long count = 0;
	std::vector<char> pancakes(S.begin(), S.end());
	int i=0,j=0, firstPlus=0;
	for(i=length-1;  i>-1; i--, j++) {
		//printStack(&pancakes);
		if(pancakes[i] == '-') {
			if(pancakes[0]=='+' ) { //if you have a '+' on top, flipping [0...i] will give you a - at i, and you won't have done anything
				firstPlus = find_back(&pancakes, i, '+') ;	//find first instance of '+' above [i]
				//cout<<"firstPlus" << firstPlus<<"\n";
				if(firstPlus>0) {
					stackflip(&pancakes, 0, firstPlus);			//flip from lowest instance of + to top
					count ++;
				}
				else {
					pancakes[0] = '-';
					count ++;
					//printStack(&pancakes);
				}
			}
			stackflip(&pancakes,0,i);
			count ++;
		}
	}
	//printStack(&pancakes);
	return count;
}

int main() {
	ifstream file("test.txt");
	string str, S="";
	int n=0, T = readNextInt(&file);
	long rslt =0;
    for(n=0; n<T;n++) {
    	getline(file,S);
		rslt = solve(S);
		cout<<"Case #" << n+1<<": "<<rslt<<"\n";

    }
    return 0;
}
