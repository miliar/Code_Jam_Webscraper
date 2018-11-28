#include <iostream>
#include <fstream>

using namespace std;

string defaultInName("exmpl.in");
string defaultOutName("out.out");

string setOutName(string inName);
void file2File(string inName, string outName);

string runTestCase(int N, int * data)
{
	string out="";
	
	while (1)
	{
		int mv0=0, mi0=0;
		int mv1=0, mi1=0;
		int c=0;
		
		for (int i=0; i<N; ++i)
		{
			c+=data[i];
			if (data[i]>mv0)
			{
				mv1=mv0;
				mi1=mi0;
				mi0=i;
				mv0=data[i];
			}
			else if (data[i]>mv1)
			{
				mi1=i;
				mv1=data[i];
			}
		}
		
		if (c%2)
		{
			out+=(char)(mi0+'A');
			out+=' ';
			--data[mi0];
		}
		else if (mv0>0)
		{
			out+=(char)(mi0+'A');
			out+=(char)(mi1+'A');
			out+=' ';
			--data[mi0];
			--data[mi1];
		}
		else
		{
			break;
		}
	}
	
	return out;
}

int main(int argc, char * * args)
{
	string inName, outName;
	
	if (argc>=2)
		inName.assign(args[1]);
	else
		inName.assign(defaultInName);
	
	if (argc>=3)
		outName.assign(args[2]);
	else
		outName=setOutName(inName);
	
	file2File(inName, outName);
	
	return 0;
}

string setOutName(string inName)
{
	string outName;
	unsigned int index=inName.find_first_of(".in");
	if (index>inName.length())
		index=inName.length();
	outName.assign(inName.substr(0, index)+".out");
	return outName;
}

void file2File(string inName, string outName)
{
	ifstream inFile;
	
	while (1)
	{
		if (!inName.compare("quit") || !inName.compare("exit") || !inName.compare("q"))
		{
			cout << "quiting without doing anything\n";
			return;
		}
		
		inFile.open(inName);
		
		if (!inFile.good())
		{
			cout << "failed to open '" << inName << "', type in filename or type 'quit' to exit:\n> ";
			cin >> inName;
			outName=setOutName(inName);
		}
		else
		{
			cout << "successfully loaded '" << inName << "'\n";
			cout << "saving to '" << outName << "'\n";
			break;
		}
	}
	
	ofstream outFile;
	
	outFile.open(outName);
	
	if (!outFile.good())
	{
		cout << "issue with output file, quitting\n";
		return;
	}
	
	int iters;
	
	inFile >> iters;
	
	cout << "\nrunning through cases:\n";
	
	for (int i=0; i<iters; ++i)
	{
		int nums[26];
		int N;
		inFile >> N;
		for (int j=0; j<N; ++j)
		{
			inFile >> nums[j];
		}
		string out=runTestCase(N, nums);
		cout << "Case #" << i+1 << ", input: " << N << ", output: " << out << "\n";
		outFile << "Case #" << i+1 << ": " << out << "\n";
	}
	
	inFile.close();
	outFile.close();
	
	cout << "\nall cases saved, program done\n";
}



