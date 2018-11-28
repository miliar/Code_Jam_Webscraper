#include <fstream>
#include <set>

using namespace std;

ifstream fin("D:\\Input.txt");
ofstream fout("D:\\Output.txt");

int T;

int main(int argc, const char* argv[])
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		double N = 0, answer1 = 0, answer2 = 0;
		set<double> S1, S2, S1_a, S2_a;

		double a;
		fin >> N;
		for(int j = 0; j < N; j++)
			fin >> a, S1.insert(a);
		for(int j = 0; j < N; j++)
			fin >> a, S2.insert(a);
		S1_a = S1;
		S2_a = S2;
		for(int j = 0; j < N; j++)
		{
			double current = *(S1.rbegin());
			set<double>::iterator it = S2.lower_bound(current);
			if(*(S2.rbegin()) < current)
				S2.erase(S2.begin()), S1.erase(*(S1.rbegin())), answer2++;
			else
				S2.erase(it), S1.erase(*(S1.rbegin()));
		}
		for(int j = 0; j < N; j++)
		{
			double current = *(S1_a.rbegin());
			if(current < *(S2_a.rbegin()))
				S2_a.erase(*(S2_a.rbegin())), S1_a.erase(*(S1_a.begin()));
			else
				S2_a.erase(*(S2_a.rbegin())), S1_a.erase(*(S1_a.rbegin())), answer1++;
		}
		fout << "Case #" << i + 1 << ": " << answer1 << " " << answer2 << "\n";
	}
	return 0;
}