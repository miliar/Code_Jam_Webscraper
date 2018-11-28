#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void main()
{
	ifstream in;
	in.open("D-small-attempt0.in");
	ofstream out;
	out.open("out2.txt");

	int T;
	int N;
	int deceitful;
	int war;
	double maxN, maxK, minN, minK;
	vector<double> Naomi;
	vector<double> Ken;
	vector<double> NWar;
	vector<double> KWar;
	
	in >> T;
	for (int i = 0; i < T; i++)
	{
		Naomi.clear();
		Ken.clear();
		NWar.clear();
		KWar.clear();
		deceitful = 0;
		war = 0;
		in >> N;
		double input;
		for (int j = 0; j < N; j++)
		{
			in >> input;
			Naomi.push_back(input);
			NWar.push_back(input);
		}
		for (int k = 0; k < N; k++) {
			in >> input;
			Ken.push_back(input);
			KWar.push_back(input);
		}
		if (N == 1)
		{
			if (Naomi[0] > Ken[0]) 
			{
				deceitful = 1;
				war = 1;
			}
			else
			{
				deceitful = 0;
				war = 0;
			}
		}
		else
		{
			while (Ken.size() > 0) {
				maxN = *max_element(Naomi.begin(), Naomi.end());
				minN = *min_element(Naomi.begin(), Naomi.end());
				maxK = *max_element(Ken.begin(), Ken.end());
				minK = *min_element(Ken.begin(), Ken.end());
				
				if (minN < maxK) {
					if (minN > minK) {
						deceitful++;
						Naomi.erase(min_element(Naomi.begin(), Naomi.end()));
						Ken.erase(min_element(Ken.begin(), Ken.end()));
					}
					else {
						Naomi.erase(min_element(Naomi.begin(), Naomi.end()));
						Ken.erase(max_element(Ken.begin(), Ken.end()));
					}
				}
				else {
					deceitful++;
					Naomi.erase(min_element(Naomi.begin(), Naomi.end()));
					Ken.erase(max_element(Ken.begin(), Ken.end()));
				}
			}
			while(KWar.size() > 0) {
				maxN = *max_element(NWar.begin(), NWar.end());
				minN = *min_element(NWar.begin(), NWar.end());
				maxK = *max_element(KWar.begin(), KWar.end());
				minK = *min_element(KWar.begin(), KWar.end());
				if (maxN > minK) {
					if (maxN > maxK){
						war++;
						KWar.erase(min_element(KWar.begin(), KWar.end()));
					}
					else
						KWar.erase(max_element(KWar.begin(), KWar.end()));
					NWar.erase(max_element(NWar.begin(), NWar.end()));
				}
				else {
					KWar.erase(min_element(KWar.begin(), KWar.end()));
					NWar.erase(max_element(NWar.begin(), NWar.end()));
				}
			}
		}
		out << "Case #" << i+1 << ": " << deceitful << " " << war << endl;
	}
	in.close();
	out.close();
}