#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

void main()
{
	ifstream ifs("Resources/input.in", std::ifstream::in);
	unsigned int samples, N, J;
	ofstream ofs("Resources/output.txt", std::ofstream::out);
	ifs>>samples;
	
	for(int j=1; j<=samples; j++)
	{
		char word[1001];
		ifs>>word;
		
		char output[1001];
		output[0] = word[0];
		output[1] = '\0';

		for(int i=1; i<strlen(word); i++)
		{
			if(word[i] >= output[0])
			{
				char temp[1001];
				strcpy(temp, output);
				output[0] = word[i];
				output[1] = '\0';
				strcat(output, temp);
			}
			else
			{
				int pos = strlen(output);
				output[pos] = word[i];
				output[pos+1] = '\0';
			}
		}

		ofs<<"Case #"<<j<<": "<<output<<endl;
	}
}