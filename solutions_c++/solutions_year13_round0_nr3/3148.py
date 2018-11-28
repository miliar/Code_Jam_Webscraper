#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>

using namespace std;
using namespace stdext;

bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile);

bool isPalindrome(int num)
{
	stack<int> st;
	while (num > 0)
	{
		st.push(num%10);
		num /= 10;
	}

	vector<int> arr;
	while (!st.empty())
	{
		arr.push_back(st.top()); 
		st.pop();
	}

	const int mid = arr.size()/2;
	for (int i = 0; i < mid; ++i)
		if (arr[i] != arr[arr.size()-1 - i])
			return false;

	return true;
}

int main()
{
	// files
	ifstream readFile;
	ofstream writeFile;
	
	//string fileIn("practice");
	string fileIn("small");
	//string fileIn("large");

	if (!openFileHandles(readFile, fileIn + ".txt", writeFile, fileIn + "_out.txt"))
		return -1;

	// read # of lines
	int T;
	readFile >> T;
	readFile.get();  // get rid of the newline

	// for each test case, ...
	for (int t = 0; t < T; ++t)
	{
		// TODO: start here
		int A, B;
		readFile >> A >> B;

		int count = 0;
		for (int i = A; i <= B; ++i)
		{
			if (isPalindrome(i))
			{
				double root = sqrt((double)i);
				double delta = root - (int)root;
				if (delta > 0)  // root is not an int
					continue;

				if (isPalindrome((int)root))
					++count;
			}
		}

		//  "Case #x: y"
		//cout << "Case #" << t+1 << ": " << count << endl;
		writeFile << "Case #" << t+1 << ": " << count << endl;
	}  // for (n)

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}

bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile)
{
	// input file
	readFile.open(inFile.c_str());
	if (!readFile)
	{
		cout << "Could not find '" << inFile << "'\n\n";
		return false;
	}

	// output file
	writeFile.open(outFile.c_str());
	if (!writeFile)
	{
		cout << "Could not find '" << outFile << "'\n\n";
		return false;
	}

	return true;
}
