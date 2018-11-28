#include <iostream>
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>

using namespace std;

string lastWord( string input ){
	vector<char> output;
	output.push_back(input.at(0));
	for( int i=1; i<input.size(); i++ ){

		if( output.front() > input.at(i) )output.push_back(input.at(i));
		else output.insert(output.begin(), input.at(i) );
	}
	string result(output.begin(), output.end());
	return result;
}


int main(){
	int lines;
	string line;
	cin >> lines;
	for(int i=0; i<lines; i++){
		cin >> line;
		printf("Case #%i: %s\n", i+1, lastWord(line).c_str());
	}
	return 0;
}