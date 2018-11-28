// reading a text file
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <climits>

using namespace std;

int main () {
	// define variables
	int numTC;
	int N;

	// ifstream myfile ("A-small-practice.in");
	// ofstream savefile ("A-small-practice.out");
	
	ifstream myfile ("A-large.in");
	ofstream savefile ("A-large.out");
	
	if(!myfile.is_open())
		cout << "File not found";

	myfile >> numTC;

	for(int t = 0; t < numTC; t++) // run each test case
	{	
		string S;
		myfile >> S;
		
		int len = S.length();
		
		string ans;
		
		ans = S[0];
		
		for(int i = 1; i < len; i++)
		{
			if((int)S[i] >= (int)ans[0])
				ans = S[i] + ans;
			else
				ans = ans + S[i];
		}
		
		savefile << "Case #" << (t + 1) << ": " << ans << endl;	
	}

	myfile.close();
	savefile.close();

	return 0;
}


