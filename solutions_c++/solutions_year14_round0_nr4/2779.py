#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	ifstream ifs("C:/yoshiko/programming/gcj/2014/QR/D/D-large.in");
	ofstream ofs("C:/yoshiko/programming/gcj/2014/QR/D/D-large.out");
	string line;

	getline(ifs, line);
	int nCases = 0;
	sscanf(line.c_str(), "%d", &nCases);

	cout << "cases:" << nCases << endl;

	for(int i=0; i<nCases; ++i)
	{
		getline(ifs, line);
		int nBlock = 0;
		sscanf(line.c_str(), "%d", &nBlock);

		getline(ifs, line);

		vector<double> vNaomi;
		size_t current = 0;
		size_t pos = line.find_first_of(" ", current);
		while(pos != string::npos)
		{
			istringstream iStream;
			iStream.str(line.substr(current, pos - current));
			double dBlock;
			iStream >> dBlock;
			vNaomi.push_back(dBlock);

			current = pos + 1;
			pos = line.find_first_of(" ", current);
		}

		istringstream iStreamN;
		iStreamN.str(line.substr(current));
		double dBlock;
		iStreamN >> dBlock;  
		vNaomi.push_back(dBlock);

		getline(ifs, line);

		vector<double> vKen;
		current = 0;
		pos = line.find_first_of(" ", current);
		while(pos != string::npos)
		{
			istringstream iStream;
			iStream.str(line.substr(current, pos - current));
			double dBlock;
			iStream >> dBlock;
			vKen.push_back(dBlock);

			current = pos + 1;
			pos = line.find_first_of(" ", current);
		}

		istringstream iStreamK;
		iStreamK.str(line.substr(current));
		dBlock;
		iStreamK >> dBlock;  
		vKen.push_back(dBlock);

		sort(vNaomi.begin(), vNaomi.end());
		sort(vKen.begin(), vKen.end());

		multiset<double> sKenForWar;
		multiset<double> sKenForDeceitfulWar;
		vector<double>::iterator it;
		bool isFound = false;
		for(it=vKen.begin(); it != vKen.end(); ++it)
		{
			sKenForWar.insert(*it);
			sKenForDeceitfulWar.insert(*it);
		}

		int nWonWar = 0;
		int nWonDeceitfulWar = 0;

		// War
		vector<double>::iterator itN;
		for(itN=vNaomi.begin(); itN != vNaomi.end(); ++itN)
		{
			bool isFound = false;
			vector<double>::iterator itK;
			for(itK=vKen.begin(); itK != vKen.end(); ++itK)
			{
				if(*itK > *itN)
				{
					multiset<double>::const_iterator pos = sKenForWar.find(*itK);
					if(pos != sKenForWar.end())
					{
						sKenForWar.erase(pos);
						isFound = true;
						break;
					}
				}
			}

			if(!isFound)
			{
				nWonWar++;

				for(itK=vKen.begin(); itK != vKen.end(); ++itK)
				{
					multiset<double>::const_iterator pos = sKenForWar.find(*itK);
					if(pos != sKenForWar.end())
					{
						sKenForWar.erase(pos);
						break;
					}
				}
			}

			isFound = false;
			vector<double>::reverse_iterator ritK;
			for(ritK=vKen.rbegin(); ritK != vKen.rend(); ++ritK)
			{
				if(*ritK < *itN)
				{
					multiset<double>::const_iterator pos = sKenForDeceitfulWar.find(*ritK);
					if(pos != sKenForDeceitfulWar.end())
					{
						sKenForDeceitfulWar.erase(pos);
						isFound = true;
						nWonDeceitfulWar++;
						break;
					}
				}
			}

			if(!isFound)
			{
				for(ritK=vKen.rbegin(); ritK != vKen.rend(); ++ritK)
				{
					multiset<double>::const_iterator pos = sKenForDeceitfulWar.find(*ritK);
					if(pos != sKenForDeceitfulWar.end())
					{
						sKenForDeceitfulWar.erase(pos);
						break;
					}
				}
			}
		}

		ofs << "Case #" << i+1 << ": " << nWonDeceitfulWar << " " << nWonWar << endl;
		cout << "Case #" << i+1 << ": " << nWonDeceitfulWar << " " << nWonWar << endl;
	}
}