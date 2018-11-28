#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(int argc, char* argv[])
{
	fstream inFile(argv[1], ios_base::in);
	fstream outFile(argv[2], ios_base::out);
	int cases;
	inFile >> cases;
	for (int i = 0; i < cases; i++)
	{
		string curstring;
		inFile >> curstring;
		string tempstring;
		tempstring.push_back(curstring[0]);
		for (int j = 1; j < curstring.length(); j++)
		{
			string temp1 = tempstring + curstring[j];
			string temp2 = curstring[j] + tempstring;
			tempstring = temp1;
			for (int k = 0; k <= j; k++)
			{
				if (temp1[k] > temp2[k])
				{
					break;
				}
				else if (temp1[k] < temp2[k])
				{
					tempstring = temp2;
					break;
				}
			}
		}
		outFile << "Case #" << i+1 << ": " << tempstring << endl;
	}
	inFile.close();
	outFile.close();
}