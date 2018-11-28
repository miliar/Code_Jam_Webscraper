#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int main()
{
	ofstream OutputFile;
	OutputFile.open ("C:/Users/Joseph/Desktop/CSII/Practice/Output.txt");
	ifstream InputFile;
	InputFile.open ("C:/Users/Joseph/Desktop/CSII/Practice/A-small-attempt7.in");

/*	if (!InputFile) {
  cerr << "Can't open input file " << "Input.txt" << endl;
  exit(1);
}

	if (!OutputFile) {
  cerr << "Can't open input file " << "Output.txt" << endl;
  exit(1);
}
*/

string cases; // number of cases
int cases2;
string MaxShyness = "6"; // The Highest Shyness in the Audience
string AudienceShyness = "1111111"; // The levels shyness and number of people in those levels
int friends; // number of friends you should bring for a standing ovation
int NumStand; // number of people standing for the ovation
int i;
int j;
int flag = 0;

//cout << "input the number of cases" << endl;
//cin >> cases;
InputFile >> cases;

// conversion for cases
	istringstream convert ( cases ); // convert the string to a int

	if ( !( convert >> cases2 ) ) // if it doesn't work, set numcases = 0;
		cases2 = 0;

for ( i = 1; i < cases2 +1; i ++ ) // does not require casting because the character '0' - the integer 48 = the integer 0
{
	friends = 0;
	NumStand = 0;
	MaxShyness[0] = 0;

	AudienceShyness[0] = 0;
	
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	//cout << "\ninput the max shyness level of the audience" << endl;
	//cin >> MaxShyness;
	InputFile >> MaxShyness;

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	//cout << "\ninput the Audience Shyness levels and numbers" <<endl;
	//cin >> AudienceShyness;
	InputFile >> AudienceShyness;

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	// intitalize NumStand
	NumStand = AudienceShyness[0]-48;
	//cout<< "WOOHOO " << AudienceShyness[0]-48 <<endl;
	cout << NumStand << endl; 

	for ( j = 0; j < MaxShyness[0]-48; j++ )
	{
		//cout<<"Entered Loop" <<endl;
		if ( NumStand < j + 1 )
		{
			friends++;
			NumStand = NumStand + (AudienceShyness[j+1] - 48) + 1;
			cout << "friends " << NumStand <<endl;
		}
		else
			NumStand = NumStand + (AudienceShyness[j+1] - 48);
			cout << NumStand <<endl;
		//cout << endl;
	}
	
	OutputFile << "Case #" << i << ": " << friends << endl;
	cout<< endl;
} // end cases loop

OutputFile.close();
InputFile.close();

return 0;

}