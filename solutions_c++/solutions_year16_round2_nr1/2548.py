#include <iostream>
#include <fstream>

using namespace std;

string defaultInName("a.in");
string defaultOutName("out.out");

const char * nums[10];

string setOutName(string inName);
void file2File(string inName, string outName);

void init()
{
	int i=0;
	nums[i]="ZERO"; ++i;
	nums[i]="ONE"; ++i;
	nums[i]="TWO"; ++i;
	nums[i]="THREE"; ++i;
	nums[i]="FOUR"; ++i;
	nums[i]="FIVE"; ++i;
	nums[i]="SIX"; ++i;
	nums[i]="SEVEN"; ++i;
	nums[i]="EIGHT"; ++i;
	nums[i]="NINE";
}

void removeDigit(int dig, char chr, int * tally, int * numi)
{
	int iters=tally[chr-'A'];
	numi[dig]+=iters;
	for (int j=0; j<iters; ++j)
	{
		for (int i=0; nums[dig][i]; ++i)
		{
			--tally[nums[dig][i]-'A'];
		}
	}
}

string runTestCase(string in)
{
	int numi[10];
	int tally[26];
	
	{
	for (int i=0; i<10; ++i)
		numi[i]=0;
	
	for (int i=0; i<26; ++i)
		tally[i]=0;
	
	for (int i=0; i<(int)in.length(); i++)
		++tally[in[i]-'A'];
	}
	
	removeDigit(0, 'Z', tally, numi);
	removeDigit(2, 'W', tally, numi);
	removeDigit(4, 'U', tally, numi);
	removeDigit(5, 'F', tally, numi);
	removeDigit(6, 'X', tally, numi);
	removeDigit(7, 'V', tally, numi);
	removeDigit(8, 'G', tally, numi);
	removeDigit(1, 'O', tally, numi);
	removeDigit(3, 'T', tally, numi);
	removeDigit(9, 'I', tally, numi);
	
	string out;
	for (int i=0; i<10; ++i)
	{
		for (int j=0; j<numi[i]; ++j)
		{
			out+=(char)(i+'0');
		}
	}
	
	return out;
}

int main(int argc, char * * args)
{
	string inName, outName;
	
	init();
	
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
		string inStr;
		inFile >> inStr;
		string out=runTestCase(inStr);
		cout << "Case #" << i+1 << ", input: " << inStr << ", output: " << out << "\n";;
		runTestCase(inStr);
		outFile << "Case #" << i+1 << ": " << out << "\n";
	}
	
	inFile.close();
	outFile.close();
	
	cout << "\nall cases saved, program done\n";
}



