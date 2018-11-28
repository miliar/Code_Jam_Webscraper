//Author: Bret Aston
//Problem A

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int ASCIIBUF = 48;

int main()
{
	int T;
	int shyMax;
	int standing;
	int friends;
	int caseNum = 1;
	string shyString;

	ifstream in;
	string inFile;
	cout << "Input file: ";
	getline(cin, inFile);
	in.open(inFile);

	ofstream out;
	string outFile;
	cout << "Output file: ";
	getline(cin, outFile);
	out.open(outFile);

	in >> T;
	in.ignore();

	while (in >> shyMax)
	{
		int *audience = new int[shyMax + 1];
		friends = 0;

		in >> shyString;
		for (int i = 0; i < shyString.size(); ++i){
			audience[i] = shyString[i] - ASCIIBUF;
		}
		
		standing = audience[0];
		for (int j = 1; j < shyMax + 1; ++j)
		{
			while (standing < j)
			{
				++friends;
				++standing;
			}
			standing += audience[j];
		}
		delete[] audience;

		out << "Case #" << caseNum << ": " << friends << endl;
		cout << "Case #" << caseNum << ": " << friends << endl;
		++caseNum;
	}
	
	system("PAUSE");
	return 0;
}