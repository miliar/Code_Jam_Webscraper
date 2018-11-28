#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{	
	ifstream read;
	read.open("B-large.in");

	ofstream write;
	write.open("output.txt");

	int T;
	read >> T;
	
	for(int i = 0; i < T; i++)
	{
		write << "Case #" <<i+1 <<": ";
		
		string pan;
		read >> pan;
		bool *panA = new bool[pan.size()];
		int count = 0;

		for(int j = 0; j < pan.size(); j++)
		{
			if(pan[j] == '+')
				panA[j] = true;
			else panA[j] = false;
		}

		for(int j = 0; j < pan.size() - 1; j++)
		{
			if(panA[j] != panA[j+1])
			{
				for(int k = 0; k < j + 1; k++)
				{
					panA[k] = panA[j+1];
				}
				count++;
			}
		}
		if(panA[0] == false)
			count++;

		delete panA;
		write << count << endl;
	}
	return 0;
}
