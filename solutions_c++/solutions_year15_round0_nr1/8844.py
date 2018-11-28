#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void main()
{
	int count,shylevel,memberCount,sum;
	char audience;
	ifstream reader;
	ofstream writer;
	reader.open("C:\\Users\\Hussein\\Documents\\ABC.txt", ios::in||ios::out);
	writer.open("C:\\Users\\Hussein\\Documents\\Output.txt", ios::out);
	if (reader.is_open())
	{
		reader >> count;
		for (int i = 0; i < count; i++)
		{
			memberCount = sum = 0;
			reader >> shylevel >> audience;
			for (int j = 1; j <= shylevel; j++)
			{
				sum = sum + audience - '0';
				reader >> audience;
				if (sum < j)
				{
					++memberCount;
					++sum;
				}
			}
			writer << "Case #" << i+1 << ": " << memberCount << endl;
		}
	}
	else
		cout << "Unable to open file";
	reader.close();
	writer.close();

}