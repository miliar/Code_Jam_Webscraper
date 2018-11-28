#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

void Tokenize(vector<string> & tokens, string line)
{
	string token="";
	string oneCharString = " ";
	for (int i=0; i< line.size(); i++)
		if (line[i]==' ')
		{
			tokens.push_back(token);
			token="";
		}
		else
		{
			oneCharString[0] = line[i];
			token += oneCharString;
		}
	if (token!= "")
		tokens.push_back(token);
}

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
		vector<string> tokens;
		Tokenize( tokens, line);
		int K = atoi(tokens[0].c_str());
		outf << "Case #" << i+1 <<": ";
		for (int j=0; j<K; j++)
			outf << j+1 << " ";
		outf << endl;
	}	

	outf.close();
	inf.close();
}
