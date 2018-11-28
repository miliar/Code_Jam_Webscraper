/******************************************************************************
 * main.cpp
 *
 * Created on: May 19, 2011
 * Copyright Martin Wojtczyk <martin.wojtczyk@gmail.com>
 *
 * Implementation file for Google code jam 2011. Everything is contained in one
 * file now, since splitting up code into several files was too time consuming
 * during the qualification.
 ******************************************************************************/

#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <utility>
#include <string>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

typedef std::vector<int> vi;            // Vector of int
typedef std::vector<vi> vvi;            // Vector of vi
typedef std::pair<int, int> ii;         // pair of ints
#define sz(a) int((a).size())           // return size of container
#define pb push_back                    // pushback macro
#define all(c) (c).begin(), (c).end()   // short form for interval begin-to-end
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++) // Traverse container c with iterator it
#define present(c, x) ((c).find(x) != (c).end()) // Does container c contain element x? use for sorted containers set/map
#define cpresent(c, x) (find(all(c), x) != (c).end()) // Does container c contain element x? use for vector

class Problem
{
private:
	std::istream& in;

public:
	Problem(std::istream& instream):
		in(instream)
	{
	};

	virtual ~Problem()
	{
	};

	std::string processCase()
	{
		stringstream str("");

		int firstLine;
		in >> firstLine;
		int firstLineIndex = firstLine - 1;
		vvi firstCards;
		vi line;
		int card;
		int x;
		int y;
		for (y = 0; y < 4; y++)
		{
			line.clear();
			for (x = 0; x < 4; x++)
			{
				in >> card;
				line.pb(card);
			};
			firstCards.pb(line);
		};

		int secLine;
		in >> secLine;
		int secLineIndex = secLine - 1;
		vvi secCards;
		for (y = 0; y < 4; y++)
		{
			line.clear();
			for (x = 0; x < 4; x++)
			{
				in >> card;
				line.pb(card);
			};
			secCards.pb(line);
		};

		int found = 0;
		int foundCard = 0;
		for (x = 0; x < 4; x++)
		{
			if (find(all(secCards[secLineIndex]), firstCards[firstLineIndex][x]) != secCards[secLineIndex].end())
			{
				found++;
				foundCard = firstCards[firstLineIndex][x];
			};
		};

		if (found == 0)
		{
			str << "Volunteer cheated!";
		}
		else if (found == 1)
		{
			str << foundCard;
		}
		else
		{
			str << "Bad magician!";
		};

		return str.str();
	};

	// Read number of Test Cases and process them
	void process()
	{
		unsigned int t;

		in >> t;
		for (unsigned int i = 1; i <= t; i++)
		{
			std::string caseResult = processCase();
			cout << "Case #" << i << ": " << caseResult << endl;
		};
	};
};

// Open file and process it, or print command syntax
int main(int argc, char** argv)
{
	if (argc == 2)
	{
		fstream file;
		file.open(argv[1], fstream::in);

		Problem* problem = new Problem(file);
		problem->process();
		delete problem;

		file.close();
	}
	else
	{
		cout << "Please provide an input file name." << endl;
	};

	return 0;
};
