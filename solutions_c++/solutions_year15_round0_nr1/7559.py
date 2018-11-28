#include <iostream>
#include <fstream>
#include <string>

using namespace std;


struct Record
{
	int size;
	string word;
};


int main()
{
	ifstream file("A-large.in");
	ofstream file2("output.txt");

	int totalSize;
	file >> totalSize;

	Record *r = new Record[totalSize];
	
	for ( int i = 0 ; i < totalSize ; i++)
	{
		file >> r[i].size;
		file >> r[i].word;
		
		int count = 0;
		int required = 0;
		for ( int j = 0 ; j <= r[i].size ; j++)
		{
			if ( count < j )
			{
				required += (j - count);
				count += (j-count);
			}

			count += (r[i].word[j]-48);
			
		}
		
		file2 << "Case #" << (i+1) << ": " << required << endl;
	}

	return 0;
}