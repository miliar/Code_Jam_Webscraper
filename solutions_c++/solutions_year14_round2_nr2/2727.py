#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <set>
#include <vector>
using namespace std;

int main()
{
	ifstream in;
	in.open("D:/B-small-attempt0.in");
	ofstream outputFile;
	outputFile.open("D:/B-small-attempt0.out");
	string str;
	getline(in, str);
	int tcNr;
	tcNr = stoi(str);
	int A = 0, B = 0, K = 0;
	
	for (int i = 0; i < tcNr; i++)
	{
		getline(in, str);
		int counter = 0;
		istringstream iss(str);
		iss >> A;
		iss >> B;
		iss >> K;

		for (int i = 0; i < A; i++)
		{
			for (int j = 0; j < B; j++)
			{
				int temp = i & j;
				if (temp < K)
				{
					counter++;
				}
			}
		}

		int nr = i + 1;
		string out = "Case #" + to_string(nr) + ": ";
		outputFile << out << counter << endl;
	}
	outputFile.close();
	system("pause");
}