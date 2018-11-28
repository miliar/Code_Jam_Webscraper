#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int simulate(int myMote, vector<int> &others, int count);

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A_large.out");

	int cases;
	fin >> cases;

	for (int c=0; c<cases; ++c)
	{
		int myMote, numOther;
		fin >> myMote >> numOther;

		vector<int> others(numOther);
		for (int i=0; i<numOther; ++i)
			fin >> others[i];

		sort(others.begin(), others.end());

		int changes = simulate(myMote, others, 0);

		fout << "Case #" << c+1 << ": " << changes << endl;
	}

	return 0;
}

int simulate(int myMote, vector<int> &others, int count)
{
	int changes = 0;

	while (myMote > others[count] && count < others.size())
		myMote += others[count++];

	if (count == others.size())
		return changes;

	if (myMote == 1)
		return others.size() - count;

	while (myMote <= others[count])
	{
		++changes;
		myMote += myMote - 1;
	}

	int addMotes = simulate(myMote, others, count);
	return changes + addMotes < others.size() - count ? changes + addMotes : others.size() - count;
}