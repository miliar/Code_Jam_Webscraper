#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	string s;
	vector<string> vec;

	ifstream infile ("B-large.in");
	if (infile.is_open())
	{
		infile >> T; // reads first line.
		
		while (infile >> s) // starting from second line.
		{
			vec.push_back(s); 
		}
	infile.close();
	}


	vector<int> result;
	
	for (int i = 0; i < T; i++)
	{
		// convert each string to a vector of -1 "-" and 1 "+"
		vector<int> stack;
		for(char& c : vec[i])
		{
			if (c == '+'){
				stack.push_back(1);
			}
			else{
				stack.push_back(0);
			}
		}

		// scan from the top until the first "flip" is detected. flip from there, then scan from the top again.
		int j = 0;
		int steps = 0;
		while (j < stack.size()-1) // avoid looking beyond the array!!!
		{
			if (stack[j] != stack[j+1])
			{
				vector<int> top(stack.begin(), stack.begin()+j+1);
				vector<int> bottom(stack.begin()+j+1, stack.end());
				reverse(top.begin(), top.end()); 
				transform(top.begin(), top.end(), top.begin(), logical_not<int>()); // reverse 1 and 0
				top.insert(top.end(), bottom.begin(), bottom.end()); // concat back top and bottom vectors.
				stack = top;
				steps++;
				j = 0; // continue to look from the top
				continue;
			}
			j++;
		}

		// check if in all ----- state. flip once more
		if (!stack[0]){
			steps++;
		}

		result.push_back(steps);

	}





	ofstream outfile ("q2large.txt");
	
	if(outfile.is_open())
	{
		for (size_t i=0; i != result.size(); ++i)
		{
			outfile << "Case #" << i+1 << ": " << result[i] << endl; 		
		}
		outfile.close();
	}

	return 0;
}