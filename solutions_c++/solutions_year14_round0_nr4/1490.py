#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream is(argv[1]);
	ofstream os("out");
	int T;
	is >> T;
	vector<double> naomi;
	vector<double> ken;
	int N;
	for(int t = 1; t <= T; t++)
	{
		naomi.clear();
		ken.clear();
		is >> N;
		naomi.resize(N);
		ken.resize(N);
		for(int i = 0; i < N; i++)
			is >> naomi[i];
		for(int i = 0; i < N; i++)
			is >> ken[i];
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int deceit = 0;
		int nondeceit = 0;
		int b = 0;
		int e = N - 1;
		for(int i = 0; i < N; i++)
		{
			if(naomi[i] < ken[b])
			{
				e--;
			}
			else
			{
				deceit++;
				b++;
			}
		}
		b = 0;
		e = N - 1;
		for(int i = 0; i < N; i++)
		{
			if(ken[i] > naomi[b])
			{
				b++;
			}
			else
			{
				nondeceit++;
				e--;
			}
		}
		os << "Case #" << t << ": " << deceit << " " << nondeceit << endl;
	}
}

