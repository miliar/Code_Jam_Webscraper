#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

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
	string Answer1;
	string Line1;
	string Answer2;
	string Line2;
	string Temp;

    ifstream MagicTrick("A-small-attempt0.in");
	ofstream Output;
	Output.open ("output.txt");

	getline (MagicTrick,Count);
		
	int count = atoi(Count.c_str());
	int Ans1 = 1;
	int Ans2 = 1;
	int temp = 1;
	
	int t1 = 1;

	while( t1 <= count ) {

		string T1 = static_cast<ostringstream*>( &(ostringstream() << t1) )->str();

		getline (MagicTrick,Answer1);
		Ans1 = atoi(Answer1.c_str());

		temp = 4 - Ans1;

		while( Ans1-- )
			getline (MagicTrick,Line1);

		while( temp-- )
			getline (MagicTrick,Temp);

		getline (MagicTrick,Answer2);
		Ans2 = atoi(Answer2.c_str());

		temp = 4 - Ans2;

		while(Ans2--)
			getline (MagicTrick,Line2);

		while( temp-- )
			getline (MagicTrick,Temp);

		//Comparing Selected Rows

		vector<string> TokensL1, TokensL2;

		Tokenize(Line1, TokensL1);
		Tokenize(Line2, TokensL2);

		string result;

		for( int i = 0; i < 4; i++ ) {

			if( TokensL1[i] == TokensL2[0] )
				if( result.size() == 0 )
					result = "Case #" + T1 + ": " + TokensL1[i];
				else
					result = "Case #" + T1 + ": " + "Bad magician!";
			else if( TokensL1[i] == TokensL2[1] )
				if( result.size() == 0 )
					result = "Case #" + T1 + ": " + TokensL1[i];
				else
					result = "Case #" + T1 + ": " + "Bad magician!";
			else if( TokensL1[i] == TokensL2[2] )
				if( result.size() == 0 )
					result = "Case #" + T1 + ": " + TokensL1[i];
				else
					result = "Case #" + T1 + ": " + "Bad magician!";
			else if( TokensL1[i] == TokensL2[3] )
				if( result.size() == 0 )
					result = "Case #" + T1 + ": " + TokensL1[i];
				else
					result = "Case #" + T1 + ": " + "Bad magician!";
		} //for
		
		if( result.size() == 0 )
			result = "Case #" + T1 + ": " + "Volunteer cheated!";

		Output << result << "\n";

		t1++;
	} //while
	MagicTrick.close();
 
    return 0;
} //main