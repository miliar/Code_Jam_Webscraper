#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

void readfile(vector<string> &thestring);
string inttostring(int n);
string judgewinninglosing(int n, vector<string> somevector);

int main ()
{
	vector<string> thegames(1, "");
	readfile(thegames);
	int repeatingtimes = atoi (thegames[0].c_str());
	ofstream file("results.txt");
	for (int p = 0; p < repeatingtimes; p++)
		file << "Case #" << inttostring (p+1).c_str() << ": " << judgewinninglosing(5*p+1, thegames) << endl;
	return 0;
}

void readfile(vector<string> &thestring)
{
	int n = 0;
	ifstream file("data.txt");
	while (getline (file, thestring[n]))
	{
		n++;
		thestring.resize(thestring.size() + 1);
	}
	thestring.resize(thestring.size() - 1);
	file.close();
}

string judgewinninglosing(int n, vector<string> somevector)
{
	bool unfinished = 0;
	int winner = 0;
	string exportstring;
	vector<string> testinglines(10, "");
	for (int p = 0; p < 4; p++)
	{
		testinglines[p] = somevector[n + p];																//horizontal lines
		testinglines[p+4] += somevector[n][p];																//vertical lines
		testinglines[p+4] += somevector[n+1][p];
		testinglines[p+4] += somevector[n+2][p];
		testinglines[p+4] += somevector[n+3][p];		
		testinglines[8] += somevector[n+p][p];																//diagonal lines
		testinglines[9] += somevector[n+3-p][p];															
	}
	for (int p = 0; p < 10; p++)																			//testing the lines
	{
		if ((testinglines[p].find('.'))==(-1))
		{
			
			if ((testinglines[p].find('X')) == (-1))
				winner = 2;
			if ((testinglines[p].find('O')) == (-1))
				winner = 1;
		}
		else
			unfinished = 1;
	}
	if ((unfinished) && (winner == 0))
		winner = 3;

	switch (winner)
	{
		case 0: exportstring = "Draw"; break;
		case 1: exportstring = "X won"; break;
		case 2: exportstring = "O won"; break;
		case 3: exportstring = "Game has not completed"; break;
		default: exportstring = "Error"; break;
	}
	return exportstring;
}

string inttostring(int n)
{
	string numberindecform, reversednum;
	while (n > 0)
	{
		reversednum+=char(n%10 + '0');
		n/=10;
	}
	for (int p = reversednum.size()-1; p >= 0; p--)
		numberindecform += reversednum[p];
	return numberindecform;
}