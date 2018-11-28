#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <fstream>
using namespace std;
int main(){
	ifstream input;
	input.open("A-large.in");
	ofstream output;
	output.open("A-large-output.txt");
	int cases,N,sheep,currentCase = 1;;
	string digits;
	set<char> seen;
	input>>cases;
	while(currentCase <= cases){
		sheep = 0;
		seen.clear();
		input >> N;
		while(seen.size() < 10 && N != 0){
			sheep += N;
			ostringstream ss;
     		ss << sheep;
    		digits =  ss.str();
			for(int i = 0; i < digits.length();i++){
				seen.insert(digits[i]);
			}
		}
		output<<"Case #"<<currentCase<<": ";
		if(N  == 0)
			output<<"INSOMNIA"<<endl;
		else
			output<<sheep<<endl;
		currentCase++;
	}


}