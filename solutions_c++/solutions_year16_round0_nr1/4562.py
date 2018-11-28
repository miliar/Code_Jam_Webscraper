#include "fstream"
#include "vector"
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

vector<long long int> Digits(long long int n)
{
	vector<long long int> v;
	do {
		int digit = n % 10;
		v.push_back(digit);		
		n /= 10;
	} while (n > 0);
	return v;
}

int main()
{

	ifstream inputFile;
	inputFile.open("A-large.in");
	//inputFile.open("Test.txt");
	ofstream outputFile;
	outputFile.open("result");
	vector<int> myMap;
	int T;
	inputFile >> T;
	for (int t = 1; t <= T; t++)
	{
		int N;
		inputFile >> N;
		int lastNum=0;
		bool found = false;
		for (int i = 1; i <= 100 && !found; i++)
		{
			
			long long int no = N*i;
			vector<long long int> digits= Digits(no);
			for (int d = 0; d < digits.size(); d++)
			{
				vector<int>::iterator it = find(myMap.begin(), myMap.end(),digits[d]);
				if (it == myMap.end())
				{
					myMap.push_back(digits[d]);
				}
				if (myMap.size() == 10)
				{
					lastNum = no;
					found = true;
					break;
				}
			}
		}
		if (lastNum == 0)
		{
			cout << "Case #" << t << ": INSOMNIA" << endl;
			outputFile << "Case #" << t << ": INSOMNIA" << endl;
		}
		else 
		{
			cout << "Case #" << t << ": " << lastNum << endl;
			outputFile << "Case #" << t << ": " << lastNum << endl;
		}
		myMap.clear();
		lastNum = 0;
	}
}
