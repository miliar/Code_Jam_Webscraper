#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;



int main()
{
	fstream in;
	in.open("C://input_large.in", ios::in);
	if (in.fail()){
		cerr << "Open graph file inputfile error!" << endl;
		return false;
	}
	ofstream outfile("C://output1.txt");
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
		int length = inputString.length();
		int needFlip = length - 1;
		while (needFlip >= 0)
		{
			if (inputString[needFlip] == '-')
				break;
			needFlip--;
		}
		if (needFlip == -1)
		{
			outfile << "Case #" << count << ": " << 0 << endl;
			cout << 0 << endl;
			count++;
			continue;
		}
		int result = 0;
		char lastSig = '+';
		for (; needFlip >= 0; needFlip--)
		{
			if (inputString[needFlip] == lastSig)
				continue;
			else
			{
				result++;
				lastSig = inputString[needFlip];
			}

		}
		outfile << "Case #" << count << ": " << result << endl;
		cout << result << endl;
		count++;
	}
	in.close();
	outfile.close();

	return 0;
	
	
}