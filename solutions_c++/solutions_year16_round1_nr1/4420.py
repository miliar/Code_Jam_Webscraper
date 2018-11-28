#include <iostream>
#include <fstream>

using namespace std;

string defaultInName("in.in");
string defaultOutName("out.out");

void file2File(string inName, string outName);
void runTestCase(char * inStr);

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
		outName.assign(defaultOutName);
	
	//runToNum(10000000);
	file2File(inName, outName);
	
	return 0;
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
		}
		else
		{
			cout << "successfully loaded '" << inName << "'\n";
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
		char inStr[3000];
		inFile >> inStr;
		cout << "Case #" << i+1 << ", input: " << inStr;
		runTestCase(inStr);
		outFile << "Case #" << i+1 << ": " << inStr << "\n";
		cout << ", output: " << inStr << "\n";
	}
	
	inFile.close();
	outFile.close();
	
	cout << "\nall cases saved, program done\n";
}

void runTestCase(char * in)
{
	char c[3000];
	int p[3000];
	
	int lng;
	
	lng=0;
	
	while (in[lng])
	{
		c[lng]=in[lng];
		p[lng]=lng;
		
		//do a quick insertion sort
		int j=lng;
		while (j>0 && (c[j]>c[j-1] || (c[j]==c[j-1] && p[j]>p[j-1])))
		{
			char cTmp=c[j];
			c[j]=c[j-1];
			c[j-1]=cTmp;
			
			int pTmp=p[j];
			p[j]=p[j-1];
			p[j-1]=pTmp;
			
			--j;
		}
		
		++lng;
	}
	
	cout << ", sorted: " << c;
	
	int w=lng;
	
	int j=1;
	
	while (j<w)
	{
		if (p[j]>p[j-1])
		{
			--w;
			
			char cTmp=c[j];
			int pTmp=p[j];
			
			for (int k=j; k<w; ++k)
			{
				c[k]=c[k+1];
				p[k]=p[k+1];
			}
			
			c[w]=cTmp;
			p[w]=pTmp;
			
			int k=w;
			
			while (k<lng-1 && p[k]>p[k+1])
			{
				char cTmp=c[k];
				c[k]=c[k+1];
				c[k+1]=cTmp;
				
				int pTmp=p[k];
				p[k]=p[k+1];
				p[k+1]=pTmp;
				
				++k;
			}
		}
		else
			++j;
	}
	
	cout << ", w=" << w;
	
	/*char l0[3000], l1[3000];
	int s0=0, s1=0, h=lng;
	
	for (int j=0; j<lng; ++j)
	{
		if (s0==0 || l0[s0-1]==c[j] || p[j]<h)
		{
			l0[s0]=c[j];
			h=p[j];
			++s0;
		}
		else
		{
			l1[s1]=c[j];
			++s1;
		}
	}*/
	
	for (int j=0; j<lng; ++j)
	{
		in[j]=c[j];
	}
	
	in[lng]=0;
}


