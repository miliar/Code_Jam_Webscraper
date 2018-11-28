#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
	fstream in;
	in.open("C://A1.in", ios::in);
	if (in.fail()){
		cerr << "Open graph file inputfile error!" << endl;
		return false;
	}
	ofstream outfile("C://1.txt");
	if (!outfile){
		cout << "Unable to open outfile";
		exit(1); // terminate with error  
	}
	const int BUFFER_LENGTH = 100000;
	char buffer[BUFFER_LENGTH] = { 0 };
	int CaseNum = 0;
	in.getline(buffer, BUFFER_LENGTH);
	CaseNum = atoi(buffer);
	int count = 1;
	while (in.getline(buffer, BUFFER_LENGTH))
	{
		string inputString;
		inputString.assign(buffer);
		stringstream stream1;
		stream1 << inputString[0];
		string outputString = stream1.str();
		for (int i = 1; i < inputString.length(); i++)
		{
			string temp;
			stringstream stream2;
			stream2.clear();

			stream2 << inputString[i];
			temp = stream2.str();
			if (inputString[i]>outputString[0])
				outputString = temp + outputString;
			else if (inputString[i] == outputString[0])
			{
				for (int j = 0; j < outputString.length(); j++)
				{
					int a = outputString.length() - 1;
					if (inputString[i] == outputString[j] && j == outputString.length() - 1)
					{
						outputString = temp + outputString;
						break;
					}
					else if (inputString[i] == outputString[j])
						continue;
					else
					{
						if (inputString[i]>outputString[j])
						{
							outputString = temp + outputString;
							break;
						}
						else
						{
							outputString = outputString + temp;
							break;
						}
					}
				}
			}
			else
				outputString = outputString + temp;

		}
		outfile << "Case #" << count << ": " << outputString << endl;
		count++;
	}

	in.close();
	outfile.close();
	return 0;
}