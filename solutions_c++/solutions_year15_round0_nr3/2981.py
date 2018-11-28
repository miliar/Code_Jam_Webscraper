#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

int main()
{
	ifstream in("C-small-attempt2.in");
	ofstream out("C-small-attempt2.out");

	//ifstream in("C-large.in");
	//ofstream out("C-large.out");

	int iTasks;
	in >> iTasks;
	map<string, pair<char, bool>> mpRules;
	mpRules["11"] = make_pair('1', false);
	mpRules["1i"] = make_pair('i', false);
	mpRules["1j"] = make_pair('j', false);
	mpRules["1k"] = make_pair('k', false);

	mpRules["i1"] = make_pair('i', false);
	mpRules["ii"] = make_pair('1', true);
	mpRules["ij"] = make_pair('k', false);
	mpRules["ik"] = make_pair('j', true);

	mpRules["j1"] = make_pair('j', false);
	mpRules["ji"] = make_pair('k', true);
	mpRules["jj"] = make_pair('1', true);
	mpRules["jk"] = make_pair('i', false);

	mpRules["k1"] = make_pair('k', false);
	mpRules["ki"] = make_pair('j', false);
	mpRules["kj"] = make_pair('i', true);
	mpRules["kk"] = make_pair('1', true);

	string sNeeded = "ijk";

	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{		
		int nLetters;
		in >> nLetters;
		int nRepeats;
		in >> nRepeats;
		string sTemplate;
		in >> sTemplate;
		
		char result = '\0';
		bool sign = false;
		int nIndex = 0;

		for (int i = 0; i < nRepeats; i++)
		{
			for (size_t j = 0; j < sTemplate.size(); j++)
			{
				if (result == '\0')
				{
					result = sTemplate[j];
					if (result == sNeeded[nIndex])
					{
						if (nIndex < sNeeded.size() - 1)
						{
							nIndex++;
							result = '\0';
						}
					}
					continue;
				}
				
				string s;
				s.append(1, result);
				s.append(1, sTemplate[j]);
				result = mpRules[s].first;
				sign ^= mpRules[s].second;
				if (result == sNeeded[nIndex])// && !sign)
				{
					if (nIndex < sNeeded.size() - 1)
					{
						nIndex++;
						result = '\0';
					}
				}
			}
		}
		
		string sAnswer = "NO";
		if (result == sNeeded[nIndex] && !sign)
		{
			sAnswer = "YES";
		}	

		out << "Case #" << iCount << ": " << sAnswer << endl;
	}
	return 0;
}
