#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <math.h>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	string hi;
	int number;
	cin >> number;
	int result = 0;
	int cursor = 0;
	string pn;
	char abc[500];
	char current;
	abc[0]='d';
	ofstream ofs ("revenge.txt", ofstream::out);
	for (int i = 1; i <=number; i++){
		cursor = 1;
		cin >> pn;
		for (int s = 0; s < pn.length();s++){
			current = pn.at(s);
			if (abc[cursor-1]!=current){
				abc[cursor++] = current;
			}
		}
		if (abc[cursor-1]=='d'){
			result = 0;
		}
		else if (abc[cursor-1]=='+'){
			result = cursor -2;
		}
		else{
			result = cursor -1;
		}
		ofs << "Case #"<<i<<": "<<result<<endl;
	}
	return 0;
}
