#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;


//Published here http://oopweb.com/CPP/Documents/CPPHOWTO/Volume/C++Programming-HOWTO-7.html as a Free Liscense
void Tokenize(const string& str, vector<string>& tokens, const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}
 
int main()
{
	string Count;
	string State;

    ifstream MagicTrick("B-large.in");
	ofstream Output;
	Output.open ("output.txt");

	getline (MagicTrick,Count);
		
	int count = atoi(Count.c_str());
	double C = 1;
	double F = 1;
	double X = 1;
	
	int t1 = 1;

	while( t1 <= count ) {

		string T1 = static_cast<ostringstream*>( &(ostringstream() << t1) )->str();

		getline (MagicTrick,State);

		vector<string> Tokens;

		Tokenize(State, Tokens);

		std::string::size_type sz;     // alias of size_t

		C = atof(Tokens[0].c_str());
		F = atof(Tokens[1].c_str());
		X = atof(Tokens[2].c_str());
		double R = 2.0f;
		double TotalTime = 0.0f;

		string result;

		while(true) {

			if( (TotalTime + X / R) < ( TotalTime + C / R + X / (R+F)) ) {
				string T2 = static_cast<ostringstream*>( &(ostringstream() << std::fixed << setprecision(7) << (TotalTime + X / R) ) )->str();
				result = "Case #" + T1 + ": " + T2;
				break;
			}

			double Time1 = C / R;

			TotalTime += Time1;
			R += F;

		}	//while
		
		Output << result << "\n";
		
		t1++;
	} //while
	MagicTrick.close();
 
    return 0;
} //main