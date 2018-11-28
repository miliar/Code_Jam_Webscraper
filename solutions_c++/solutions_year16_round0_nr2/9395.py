// ProblemA-CountingSheep.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	string line;
	unsigned long long minNumberOfTimes = 0;
	
	int caseN = 1;

	ifstream in("input.in");
	ofstream out("output.out");

	getline(in, line);
	cout << "trials = " << line << endl;

	int i = stoi(line);
	for (; i > 0 ; i--)
	{
		minNumberOfTimes = 0;
		getline(in, line);

		cout << line << "    ";

		while (1)
		{
			string temp;

			string::size_type pos = string::npos;
			for (int j = 0; j < line.length(); j++) {
				if (line[j] == '-') {
					pos = j;
				}
			}

			if (pos == string::npos)
				break;
			else if (line[0] == '+')
			{
				for (int k = 0; k < line.length(); k++) {
					if (line[k] == '+')
						line[k] = '-';
					else if (line[k] == '-')
						break;
				}
				minNumberOfTimes++;
			}
			
			temp = line;
			for (int j = pos; j >= 0; j--) {
				if (temp[j] == '+')
					line[pos - j] = '-';
				else if (temp[j] == '-')
					line[pos - j] = '+';
			}
			minNumberOfTimes++;
		}
		cout << "Case #" << caseN << ": " << minNumberOfTimes << endl;
		out << "Case #"<< caseN <<": " << minNumberOfTimes << endl;
		caseN++;
	}

	in.close();
	out.close();
    return 0;
}

