#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int T;
int Max;
string S;
ofstream outFile("A-small-attempt2.out");
ifstream inFile("A-small-attempt2.in");
int main()
{
	inFile >> T;
	int Output, Standing;
	for (int testcase = 0; testcase < T; testcase++){
		Output = 0; Standing = 0;
		inFile >> Max;
		inFile >> S;
		
		for (int i = 0; i <= S.length(); i++){
			if ( i <= Standing){
				Standing += S[i]-'0';
			}
			else {
				Output += (i - Standing);
				Standing = i + S[i]-'0';
			}
		}
		outFile << "Case #" << testcase + 1 << ": " << Output << endl;
	}
	outFile.close();
	return 0;
}