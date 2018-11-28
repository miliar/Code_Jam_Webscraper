#include <iostream>
#include <string>
#include <fstream>

#define F_IN "A-large.in"
#define F_OUT "test.result"

using namespace std;

int main(){

	int c = 0, cnum = 0;
	string input;
	
	// file
	ifstream in;
	ofstream out;
	in.open(F_IN);
	out.open(F_OUT);
	

	in >> c;

	while(c--){
		int max;
		int sum = 0;
		int result = 0;
		input.clear();
		
		cnum++;
		in >> max;
		in >> input;

		for(int i=0;i < max+1;i++){
			if(input[i] != '0'){
				if(sum < i){
					result = result + (i-sum);
					sum = sum + (i-sum) + input[i] - '0';
				}
				else
					sum = sum + input[i] - '0';
			}
		}
		
		out << "Case #" << cnum << ": " <<result<<endl;

	}
	out.close();
	in.close();
	return 0;
}