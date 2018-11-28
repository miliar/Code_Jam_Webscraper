// Copy all the content below to start a new file

#include <iostream>
#include <fstream>
#include <string>

#define INFILE "C:\\GCJ\\CodeJam\\input_output\\A-small-attempt0.in"
#define OUTFILE "C:\\GCJ\\CodeJam\\input_output\\A-small-attempt0.out"
using namespace std;

bool isVowel(char a)
{
	if(a == 'a'||
		a == 'e'||
		a == 'i'||
		a == 'o'||
		a == 'u')
	{
		return true;
	}
	return false;
}

int isComplex(const string &s, int n)
{
	// iterate the characters
	int count = 0;
	bool flag = true;
	int tcount = 0;
	for(int i =0; i<s.size(); i++)
	{
		if(!isVowel(s[i]))
		{	
			tcount++;
			if(tcount > count)
			{
				count = tcount;
			}
		}
		else
		{
			tcount = 0;
		}		
	}
	if (count >= n)
		return 1;
	else
		return 0;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open(INFILE);
	if(!fin.is_open())
	{
		cout<<"Failed to open input file. Press a key to exit...";
		cin.get();
		return 0;
	}
	fout.open(OUTFILE);
	if(!fin)
	{
		cout<<"Failed to open output file. Press a key to exit...";
		cin.get();
		return 0;
	}	
	// Actual code starts
	//===================
	int totalcases = 0;
	fin>>totalcases;
	
	cout<<"\nReading total cases: "<<totalcases;
	for( int c = 1; c <= totalcases; c++)
	{
		int nval = 0;
		string name;
		string subname;
		int n;
		getline(fin, name, ' ');
		fin>>n;
		for(int i = 1; i < name.size(); ++i)
		{
			for(int l = 1; l < name.size() - i +1; l++)
			{
				subname = name.substr(i,l);
				nval += isComplex(subname, n);
			}
		}
		fout<<"Case #"<<c<<": "<<nval<<endl;
	}		
	//===================
	// Actual code ends
	if(fin)
	{
		fin.close();
	}
	if(fout)
	{
		fout.close();
	}
	cout<<"\nExiting program. Press a key to exit...";
	cin.get();
	return 0;
}
