#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <sstream>

using namespace std;




int main()
{
	ifstream input;
	ofstream output;
	input.open("A-large (1).in");
	output.open("output.txt");
	
	int T;
	string word, last;
	input >> T;
	
	for(int t = 1; t <= T; t++)
	{
		output << "Case #" << t << ": ";
		input >> word;
		last = "" + word.substr(0,1);
		for(int s = 1; s < word.length(); s++)
		{
			if(word[s] >= last[0])
			{
				last = word.substr(s,1) + last;
			}
			else
			{
				last = last + word.substr(s,1);
			}
		}
		output << last << endl;
		
	}
	input.close();
	output.close();
	
	return 0;
}