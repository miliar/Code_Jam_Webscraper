#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int readInputInt(std::ifstream& infile);
int readLongInputInt(std::ifstream& infile);

int main(int argc, char** arg){
	//Input & Output
	ofstream outfile("output.txt");
	ifstream infile(arg[1]);

	if (infile.is_open())
	{
		int testCases = 0;

		//read number of test cases
		testCases = readLongInputInt(infile);

		for (int i = 0; i < testCases; i++)
		{
			char ch;
			int maxShy = 0;
			int standing = 0;
			int friendsNeeded = 0;

			maxShy = readInputInt(infile);

			for (int x = 0; x <= maxShy; x++)
			{
					if (standing >= x)
						standing = standing + readInputInt(infile);
					else{
						int newFriends = 0;
						newFriends = x - standing;
						friendsNeeded = friendsNeeded + newFriends;
						standing = standing + newFriends + readInputInt(infile);
					}
			}
			outfile << "Case #" << i + 1 << ": " << friendsNeeded << endl;

		}

		infile.close();
		outfile.close();
	}
	else
		cout << "Could not open input file.\n";

	return 0;
}

int readInputInt(std::ifstream& infile)
{
	char ch;
	int value = 0;

	infile.get(ch);
	if (ch == '\n' || ch == ' ')
		infile.get(ch);

	if (ch >= 48 && ch <= 57)
	{
		value = ch - 48;
		return value;
	}
	else 
		return -1;
}

int readLongInputInt(std::ifstream& infile)
{
	char ch;
	int value = 0;

	infile.get(ch);
	while (ch >= 48 && ch <= 57)
	{
		value *= 10;
		value += ch - 48;
		infile.get(ch);
	}

	return value;
}