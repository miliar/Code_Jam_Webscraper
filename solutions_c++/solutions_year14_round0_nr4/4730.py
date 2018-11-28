#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

typedef long double ld;
typedef long long lli;

int main()
{
	ifstream fin("deceitfulwar.in");
	int T;
	fin>>T;

	ofstream fout("deceitfulwar.out");

	for(int i=0;i<T;i++)
	{
		fout<<"Case #"<<(i+1)<<": ";
		lli N;
		fin>>N;
		vector<ld> naomi;
		vector<ld> ken;
		lli deceit=0,fair=0;
		for(int k=0;k<N;k++)
		{
			ld inp;
			fin>>inp;
			naomi.push_back(inp);
		}
		sort(naomi.begin(), naomi.end());

		for(int k=0;k<N;k++)
		{
			ld inp;
			fin>>inp;
			ken.push_back(inp);
		}
		sort(ken.begin(), ken.end());

		vector<ld> k2(ken);


		for(int k=0;k<N;k++)
		{
			if(k2[k2.size()-1] < naomi[k])
			{
				fair++;
				k2.erase(k2.begin());
			}
			else
			{
				k2.erase(lower_bound(k2.begin(),k2.end(),naomi[k]));
			}
		}


		for(int k=0;k<N;k++)
		{
			if(naomi[0] < ken[0])
			{
				naomi.erase(naomi.begin());
				ken.erase(--ken.end());
			}
			else
			{
				naomi.erase(naomi.begin());
				ken.erase(ken.begin());
				deceit++;
			}
		}

		fout<<deceit<<" "<<fair<<endl;
	}

	return 0;
}
