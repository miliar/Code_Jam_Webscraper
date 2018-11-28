#include<fstream>
#include<iomanip>
using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

int T;
double C, F, X, cookies=2, sec;
int main()
{
	fin >> T;
	int tmp = T;
	while (T--)
	{
		fin >> C >> F >> X;
		bool finished = 0;
		sec = 0;
		cookies = 2;
		while (!finished)
		{
			if (X / cookies <= C / cookies + X / (cookies + F))
			{
				finished = true;
				sec += X / cookies;
			}
			else
			{
				sec += C / cookies;
				cookies += F;
			}
		}
		fout << "Case #" << tmp - T << ": "<<fixed<<setprecision(7)<<sec<<'\n';
	}
	return 0;
}