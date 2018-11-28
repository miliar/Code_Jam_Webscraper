#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
 
int main()
{
	string Count;
	string Case;
	int Si;
	int Clapping = 0;
	int Needed = 0;
	string result;

    ifstream Opera("A-small-attempt0.in");
	ofstream Output;
	Output.open ("output.txt");

	getline (Opera,Count);
		
	int count = atoi(Count.c_str());
	
	int t1 = 1;

	while( t1 <= count ) {

		string T1 = static_cast<ostringstream*>( &(ostringstream() << t1) )->str();

		getline (Opera,Case);
		Si = (Case.c_str())[0] - '0';

		for(int i = 0; i <= Si; i++) {
			if(((Case.c_str())[i+2] - '0') != 0) {
				if(Clapping >= i)
					Clapping += (Case.c_str())[i+2] - '0';
				else {
					Needed += i - Clapping;
					Clapping += (Needed + ((Case.c_str())[i+2] - '0'));
				}
			}
		}

		stringstream ss;
		ss << Needed;
		string str = ss.str();
		
		result = "Case #" + T1 + ": " + str;

		Output << result << "\n";

		Clapping = 0;
		Needed = 0;

		t1++;
	} //while
	Opera.close();
 
    return 0;
} //main