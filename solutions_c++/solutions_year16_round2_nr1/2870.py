#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <iomanip>
#include <algorithm>
#include <list>
#include <set>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <limits>
#include <bitset>

#undef min
#undef max

#define ALL(x) begin(x), end(x)

using namespace std;

void doIt()
{
	string S;
	cin >> S;

	string Sprime = S;

	sort(ALL(S));

	vector<int> counts(10, 0);

	int cur = -1;
	while (true)
	{
		cur = S.find_first_of("ZWUXG", (size_t)(cur + 1));
		if (cur == string::npos)
			break;

		switch (S[cur])
		{
		case 'Z': ++counts[0]; break;
		case 'W': ++counts[2]; break;
		case 'U': ++counts[4]; break;
		case 'X': ++counts[6]; break;
		case 'G': ++counts[8]; break;
		}
	}

	size_t pos = S.find('O');
	if (pos != string::npos)
		S.erase(pos, counts[0] + counts[2] + counts[4]);
	pos = S.find('T');
	if (pos != string::npos)
		S.erase(pos, counts[2] + counts[8]);
	pos = S.find('F');
	if (pos != string::npos)
		S.erase(pos, counts[4]);
	pos = S.find('S');
	if (pos != string::npos)
		S.erase(pos, counts[6]);

	cur = -1;
	while (true)
	{
		cur = S.find_first_of("OTFS", (size_t)(cur + 1));
		if (cur == string::npos)
			break;

		switch (S[cur])
		{
		case 'O': ++counts[1]; break;
		case 'T': ++counts[3]; break;
		case 'F': ++counts[5]; break;
		case 'S': ++counts[7]; break;
		}
	}

	pos = S.find('N');
	if (pos != string::npos)
		S.erase(pos, counts[1] + counts[7]);

	cur = -1;
	while (true)
	{
		cur = S.find_first_of("N", (size_t)(cur + 1));
		if (cur == string::npos)
			break;

		switch (S[cur])
		{
		case 'N': ++counts[9]; break;
		}
	}

	if (counts[9] % 2 == 1)
		cerr << "wtf? " << counts[9] << S << endl;
	counts[9] /= 2;

	int length = 0;
	for (int i = 0; i < 10; ++i)
	{
		for (int j = 0; j < counts[i]; ++j)
			cout << i;
		switch (i)
		{
		case 0: length += 4; break;
		case 1: length += 3; break;
		case 2: length += 3; break;
		case 3: length += 5; break;
		case 4: length += 4; break;
		case 5: length += 4; break;
		case 6: length += 3; break;
		case 7: length += 5; break;
		case 8: length += 5; break;
		case 9: length += 4; break;
		}
	}

	if (length != Sprime.size())
		cerr << " " << length << " " << Sprime << endl;

	cout << endl;
}

int main(int, char* [])
{
	cout << setprecision(16);

	int nCases;
	cin >> nCases;
	for (int iCase = 0 ; iCase < nCases; iCase++)
	{
		cerr << "Case #" << (iCase + 1) << " \t";
		cout << "Case #" << (iCase + 1) << ": ";
		doIt();
	}

	cerr << endl << "Done" << endl;

	return 0;
}
