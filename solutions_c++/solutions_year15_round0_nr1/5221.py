#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream infile("A-large.in");
ofstream outfile("ovationLarge.out");
int T;
string input;

int main(){
	infile>>T;
	getline(infile,input);
	
	for( int t = 1 ; t<= T ; ++t ){
		int smax = 0;
		int friends = 0, audience = 0;
		infile>>smax;
		getline(infile, input);
		int space = input.find_first_of(' ');
		input = input.substr(space+1);
		
		for( int k = 0 ; k <= smax ; ++k ){
			//k is the people needed
			if( audience >= k ) audience += (input[k]-48);
			else {
				//not enough people
				int nec = k - audience;
				friends += nec;
				audience = k + (input[k]-48);
			}
		}
		
		outfile<<"Case #"<<t<<": "<<friends<<endl;
	}
	
	return 0;
}