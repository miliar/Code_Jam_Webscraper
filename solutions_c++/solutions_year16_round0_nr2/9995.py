/*

 *
 */

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <stack>

using namespace std;


int solve(string line)
{
	int flips = 0;
	char last = line[0];
	for(int i = 0; i < line.length(); i++)
	{
		if(line[i] != last) {
			// stop here and flip all the previous to be = line[i]
			flips++;
			last = line[i];			
		}
	}
	
	if(last == '-')	flips++;
	
	return flips;		
}


int main()
{
	ifstream inf;
	ofstream outf;
	inf.open("B-large.in", ios::in);
	outf.open("B-large-output.txt");


	int T;
	int result;
	string line;
	
	inf >> T;
	// get one test case
	for(int i = 0; i < T; i++)
	{		
		
		inf >> line;
		int result = solve(line);
		cout << "Case #" << (i+1) << ": " << result << endl;
		outf << "Case #" << (i+1) << ": " << result << endl;
	}


	inf.close();
	outf.close();
	return 0;
}
