#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void outputToFile(int result, int count, char* charArray = 0, double* fraction = 0)
{
	ofstream out;
	out.open("output.txt", ios::app);
	if (out.is_open())
	{
		out << "Case #" << count << ": " << result << "\n";
	}
	out.close();
}

void main()
{
			/* File reading starts here */
	
	ifstream in;
	in.open("A-small-attempt3.in");
	string inputStr;
	getline(in, inputStr);
	int cases = stoi(inputStr);
	int Mx;
	if (in.is_open())
	{

		for (int c = 0; c < cases; c++)
		{
			
			getline(in, inputStr);
			char Max[5];
			for ( Mx = 0; inputStr[Mx] != ' '; Mx++)
				Max[Mx] = inputStr[Mx];
			int Max_shy = atoi(Max);
			char* audience = new char[Max_shy + 1];

			for (int i = 0; i <= Max_shy; i++)
				audience[i] = inputStr[i+Mx+1];
			
			/* File reading ends here */
			
			/* Problem Solution */
			int result = 0, temp = 0, r1 = 0;
			int last = audience[Max_shy] - 48;

			for (int i = 1; i <= Max_shy; i++)
			{

				for (int j = i - 1; j >= 0; j--)
					r1 += audience[j] - 48;
				r1 += result;

				if (r1 < i && audience[i] != '0')
					result +=( i - r1);
				r1 = 0;
			}
			//cout << "Case #" << c + 1 << ": " << result << endl;
			outputToFile(result, c + 1);
		}
	}
}