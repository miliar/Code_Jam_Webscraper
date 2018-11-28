// ProblemA-CountingSheep.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int temp = 0;
	string line;
	unsigned long long number = 0;
	
	int caseN = 1;
	int j = 0;
	//string numbers[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	ifstream in("input.in");
	ofstream out("output.in");

	getline(in, line);
	cout << "trials = " << line << endl;

	int i = stoi(line);
	for (; i > 0 ; i--)
	{
		int flags[10] = { 0 };
		getline(in, line);
		number = stoi(line);
		temp = number;
		if (number == 0)
		{
			cout << "Case #" << caseN << ": " << temp << ": INSOMNIA" << endl;
			out << "Case #" << caseN << ": INSOMNIA" << endl;
			caseN++;
			continue;
		}
		for (unsigned long long k=2; ; k++)
		{
			for (j = 0; j < 10; j++)
				if (to_string(number).find(to_string(j)) != std::string::npos)
					flags[j] = 1;

			for (j = 0; j < 10; j++)
				if (flags[j] == 0)
					break;
			if (j == 10)
				break;

			number = temp * k;
		}
		cout << "Case #" << caseN << ": " << temp << ": " << number << endl;
		out << "Case #"<< caseN <<": " << number << endl;
		caseN++;
	}

	in.close();
	out.close();
    return 0;
}

