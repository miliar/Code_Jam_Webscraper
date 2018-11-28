#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;

int main(int argc, char** argv) {
	
	int T = 0;
	int i = 0;
	
	ofstream op;
	op.open("output.txt");
	
	ifstream in;
	in.open("input.in");
	
	if(!in){
		cout << "cant open the file";
	}
	
	//reading total case no
	in >> T;
	for( i = 0 ; i < T ; i++ ){
		string s;
		int Smax = 0;
		int val = 0;
		int SP = 0;
		int ef = 0;
		int j = 0;
		
		
		in >> Smax;
		in >> s;
		
		for ( j = 0 ; j <= Smax; j++ ){

			val = s.at(j) -'0';
		
			if( val > 0 ){
				if( j == 0 ){
					SP = val;
				}else if( SP >= j ){
					SP += val;
				}else if( SP < j ){
					ef += j-SP;
					SP += val + (j- SP);
				}
			}
		}
		
		op << "Case #" << i+1 << ": " << ef << endl;
	
	}
	
	op.close();
	in.close();
	return 0;
}
