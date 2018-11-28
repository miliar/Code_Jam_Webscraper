#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int popaudience(string);

int main(int argc, char** argv)
{
	ifstream input;
	string line;
	input.open("file");
	int outputresult = 0;

	ofstream output;
	output.open("output");
	
	int i=0;

	if(input.is_open())
	{
		while(getline(input,line))
		{
			//cout << line << '\n';
			if(i>0)
			{
				outputresult = popaudience(line);
				output << "Case #" << i << ": " << outputresult << "\n";
			}
			i++;
		}
	}

	system("pause");
	return 0;
}

int popaudience(string line)
{
	int friendstoadd = 0;
	int standing = 0;
	vector<int> audience(line.length()-1);
	ofstream output;

	for (int j=0; j<line.length(); j++)
	{
		if(j>1)
		{
			audience[j-2] = stoi(line.substr(j,1));
		}
	}


	for (int i=0; i<audience.size();i++)
	{
		if (i>standing)
		{
			friendstoadd = friendstoadd + 1;
			standing += 1;
		}
		standing += audience[i];
	}
	return friendstoadd;
	//cout << friendstoadd;
}
