#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	ifstream ifs("C:/yoshiko/programming/gcj/2014/QR/A/A-small-attempt0.in");
	ofstream ofs("C:/yoshiko/programming/gcj/2014/QR/A/A-small-attempt0.out");
	string line;

	getline(ifs, line);
	int nCases = 0;
	sscanf(line.c_str(), "%d", &nCases);

	cout << "cases:" << nCases << endl;

	for(int i=0; i<nCases; ++i)
	{
		getline(ifs, line);
		int iFirstChoice = 0;
		sscanf(line.c_str(), "%d", &iFirstChoice);
		cout << "First choice:" << iFirstChoice << endl;

		int firstCandidates[4];
		for(int j=0; j<4; ++j)
		{
			getline(ifs, line);

			if(iFirstChoice == j + 1)
			{
				sscanf(line.c_str(), "%d %d %d %d", &firstCandidates[0], &firstCandidates[1], &firstCandidates[2], &firstCandidates[3]);
				cout << "First candidates:";
				for(int k=0; k<4; ++k)
				{
					cout << firstCandidates[k] << ",";
				}
				cout << endl;
			}
		}

		getline(ifs, line);
		int iSecondChoice = 0;
		sscanf(line.c_str(), "%d", &iSecondChoice);
		cout << "Second choice:" << iSecondChoice << endl;

		int secondCandidates[4];
		for(int j=0; j<4; ++j)
		{
			getline(ifs, line);

			if(iSecondChoice == j + 1)
			{
				sscanf(line.c_str(), "%d %d %d %d", &secondCandidates[0], &secondCandidates[1], &secondCandidates[2], &secondCandidates[3]);
				cout << "Second candidates:";
				for(int k=0; k<4; ++k)
				{
					cout << secondCandidates[k] << ",";
				}
				cout << endl;
			}
		}

		int nMatch = 0;
		int answer = -1;
		for(int j=0; j<4; ++j)
		{
			for(int k=0; k<4; ++k)
			{
				if(firstCandidates[j] == secondCandidates[k])
				{
					nMatch++;
					answer = firstCandidates[j];
					break;
				}
			}
		}

		if(nMatch == 1)
		{
			ofs << "Case #" << i+1 << ": " << answer << endl;
		}
		else if(nMatch == 0)
		{
			ofs << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
		}
		else
		{
			ofs << "Case #" << i+1 << ": " << "Bad magician!" << endl;
		}
	}
}