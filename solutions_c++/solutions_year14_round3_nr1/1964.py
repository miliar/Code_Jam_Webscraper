#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream in("A-small-attempt1.in");
ofstream out("out.txt");
int CASES = 1;
string line;
string buffer;
char a[100];
long long FRACPOINT = 0; 
long long P, Q;
long long Two[40];


void TwoPowers()
{
	long long MULTIPLY = 1;
	for (int i = 0; i < 40; i++)
	{
		MULTIPLY *= 2;
		Two[i] = MULTIPLY;
	}
}

void debug()
{
	// Print Stuffs
	out << P << " " << Q << endl;
}

void Factor()
{
	for (int i = 2; i <= P; i++)
	{
		if (P % i == 0 && Q % i == 0)
		{
			P /= i;
			Q /= i;
		}
	}
}



int SearchString()
{
	for (int i = 1; i < line.length(); i++)
	{
		if (line[i] == '/')
			return i;
	} 
	return 0;
}

int main()
{

	TwoPowers();
	in >> CASES;
	getline(in, line);
	char *b;
	for (int i = 1; i <= CASES; i++)
	{
		bool possible = false;
		out << "Case #" << i << ": ";
		getline(in, line);
		FRACPOINT = SearchString();
		buffer = line.substr(0, FRACPOINT);
		memcpy(a, buffer.c_str(), buffer.size());
		a[buffer.size()] = 0;
		P = _atoi64(a);
		buffer = line.substr(FRACPOINT + 1);
		memcpy(a, buffer.c_str(), buffer.size());
		a[buffer.size()] = 0;
		Q = _atoi64(a);
		Factor();

		for (int j = 0; j < 40; j++)
		{
			if (Q == Two[j])
			{
				possible = true; 
				break;
			}
		}

		if (possible)
		{

			while (P > 1)
			{
				P /= 2;
				Q /= 2;
			}
			
			for (int j = 0; j < 40; j++)
			{
				if (Q == Two[j])
				{
					out << (j + 1) << endl;
					break;
				}
				
			}
		}
		else
			out << "impossible\n";
	}
	out.close();

}