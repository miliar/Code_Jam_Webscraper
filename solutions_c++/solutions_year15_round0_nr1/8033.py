#include <iostream>
#include <string>
#include <vector>
#include <fstream> 

using namespace std;

int main()
{
	ifstream reader("A-large.in");
	ofstream writer("output.txt");
	string word;
	string line;
	char character;
	int numtests;
	int numstanding;
	int numadded;
	int audiencesize;
	int numlevels;
	int numseated;
	vector <int> audience;



	reader >> numtests;
	for (int x = 0; x < numtests; x++)
	{
		
		//cout << "+++++++++++++++++++++++++++++++++" << endl;
		//cout << "+++starting case #" << x + 1 << "+++++" << endl;
		//cout << "+++++++++++++++++++++++++++++++++" << endl;
		
		audience.clear();
		numstanding = 0;
		numadded = 0;
		numlevels = 0;
		audiencesize = 0;

		reader >> numlevels;
		numlevels = numlevels + 1;
		//cout << "numlevels is " << numlevels << endl;

		reader >> word;
		//cout << "word is " << word << endl;
		for (int y = 0; y < numlevels; y++)
		{
			audience.push_back(word[y]-48);
		}
		//cout << "audience is " << endl;
		//for (auto& iterator : audience)
		//{
			//cout << iterator;
		//}
		//cout << endl;
		for (auto& iterator : audience)
		{
			audiencesize += iterator;
		}
		numseated = audiencesize;
		//cout << "audiencesize is " << audiencesize << endl;
		while (numstanding<audiencesize)
		{
			for (int j = 0; j < numlevels; j++)
			{
				//cout << "j is " << j << endl;
				//cout << "audience[j] is " << audience[j] << endl;
				if (audience[j]>0)
				{
					//cout << "j is >0" << endl;
					if (j <= numstanding)
					{
						//cout << "j is < numstanding" << endl;
						numstanding += audience[j];
						audience[j] = 0;
						//cout << "new audience j is " << audience[j] << endl;
					}
					else if (j>numstanding)
					{
						//cout << "j>numstanding" << endl;
						numadded += (j-numstanding);
						numstanding += (j-numstanding);
						numstanding += audience[j];
						audience[j] = 0;
					}
				}
			}
			//cout << "numstanding is " << numstanding << endl;
			//cout << "numadded is " << numadded << endl;
			//cout << "audience is " << endl;
			for (auto& iterator : audience)
			{
				//cout << iterator;
			}
			//cout << endl;
		}
		
		//print now
		writer << "Case #" << x + 1 << ": " << numadded << endl;
		//cout << "Case #" << x + 1 << ": " << numadded << endl;

		//cout << "+++++++++++++++++++++++++++++++++" << endl;
		//cout << "+++finished case #" << x + 1 << "+++++" << endl;
		//cout << "+++++++++++++++++++++++++++++++++" << endl;
	}

	reader.close();
	writer.close();
	return 1;

}