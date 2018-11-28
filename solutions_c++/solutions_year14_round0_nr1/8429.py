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
	in.open("D:/A-small-attempt1.in");
	ofstream outputFile;
	outputFile.open("D:/A-small-attempt1.out");
	string str;
	getline(in, str);
	int tcNr;
	tcNr = stoi(str);
	int lineNr1 = 0, lineNr2 = 0;
	string line1, line2, ret;
	set <int> cards;
	vector <int> cardsvect;
	for (int i = 0; i < tcNr; i++)
	{
		getline(in, str);
		lineNr1 = stoi(str);
		for (int j = 1; j < 5; j++)
		{
			getline(in, str);
			if (j == lineNr1)
				line1 = str;
		}
		//-------------------------------
		getline(in, str);
		lineNr2 = stoi(str);
		for (int j = 1; j < 5; j++)
		{
			getline(in, str);
			if (j == lineNr2)
				line2 = str;
		}
		//--------------------------------------------------

		istringstream iss1(line1), iss2(line2);

		for (int z = 1; z < 5;z++)
		{
			string sub1, sub2;
			int temp1, temp2;
			iss1 >> sub1;
			iss2 >> sub2;
			temp1 = stoi(sub1);
			temp2 = stoi(sub2);
			cards.insert(temp1);
			cards.insert(temp2);
			cardsvect.push_back(temp1);
			cardsvect.push_back(temp2);
		}

		if (cards.size() == 8) ret = "Volunteer cheated!";
		if (cards.size() < 7) ret = "Bad magician!";
		int sol = 0;
		if (cards.size() == 7)
		{
			for (int i = 0; i < 7; i++)
			{
				for (int j = i + 1; j < 8; j++)
				{
					if (cardsvect.at(i) == cardsvect.at(j)) sol = cardsvect.at(i);
				}
			}
			ret = to_string(sol);
		}
		int nr = i + 1;
		string out = "Case #" + to_string(nr) + ": "+ret;
		outputFile << out << endl;

		cards.clear();
		cardsvect.clear();
	}

	outputFile.close();
	system("pause");
}