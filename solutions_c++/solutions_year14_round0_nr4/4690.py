#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T = 0, N = 0;
	ifstream fi("D-large.in");
	//ifstream fi("Input.txt");
	ofstream fo("Output.txt");
	fi>>T;
	for (int t = 1; t <= T; ++t)
	{
		fi>>N;
		vector<double> Naomi(N,0);
		vector<double> Ken(N,0);
		for (int i = 0; i < N; ++i)
		{
			fi>>Naomi[i];
		}
		for (int i = 0; i < N; ++i)
		{
			fi>>Ken[i];
		}
		sort(Naomi.begin(),Naomi.end());
		sort(Ken.begin(),Ken.end());
		int Deceitful = 0;
		int War = 0;
		int n = 0;
		int m = 0;
		int i = 0;
		int j = 0;
		while (i < Naomi.size() && j < Ken.size())
		{
			if (Naomi[i] > Ken[j])
			{
				++Deceitful;
				++i;++j;
			}
			else
			{
				while (i < Naomi.size() && Naomi[i] < Ken[j])
					++i;
			}
		}
		while (!Naomi.empty() && !Ken.empty())
		{
			int i = Naomi.size() - 1;
			int j = Ken.size() - 1;
			if (Naomi[i] > Ken[j])
			{
				++War;
				Naomi.erase(Naomi.end() - 1);
				Ken.erase(Ken.begin());
			}
			else
			{
				while (j > 0 && Naomi[i] < Ken[j - 1])
				{
					--j;
				}
				Naomi.erase(Naomi.end() - 1);
				Ken.erase(Ken.begin() + j);
			}
		}
		fo<<"Case #"<<t<<": "<<Deceitful<<" "<<War;
		if (t != T) fo<<endl;
	}
	fo.close();
	fi.close();
	return 0;
}