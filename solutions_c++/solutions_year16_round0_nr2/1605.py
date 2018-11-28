#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
	if (argc!=4)
	{
		cout << "Params: 0 inputFilePath outputFilePath \n"; 
	}

	ifstream inf;
	inf.open(argv[2]);
	ofstream outf;
	outf.open(argv[3]);

	int n=0;
	string line;
	getline(inf,line);
	n = atoi(line.c_str());
	
	for (int i=0; i<n; i++)
	{
		getline(inf,line);
		char lastChar = line[0];
		int counter = 1; 
		for (int j=1; j<line.size(); j++)
			if (line[j]!=lastChar)
			{
				counter++;
				lastChar = line[j];
			}
		if (lastChar == '+')
			counter--;

		outf << "Case #" << i+1 <<": " << counter << endl; 
	}	

	outf.close();
	inf.close();
}
