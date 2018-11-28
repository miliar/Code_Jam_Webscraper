#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("yayz.out");
	long long a; fin >> a; int l=1;
	for (int g=0; g<a; g++)
	{
		double rate=2;
		double time=0;
		double money=0;
		double C,F,X; fin >> C >> F >> X; // cost of farm, rate farm adds, number of cookies needed to win
		long long farms= floor(X/C);
		for (int y=1; y<=farms; y++)
		{
			money=C*y;
			if (double(double((X-C*y))/double(rate))>double(X/double((rate+F))))
			{
				time+=(double)(double(C)/double(rate));
				rate+=F;
				money=0;
				y=0;
				continue;
			}
			else
			{
				time+=(double)(double(C)/double(rate));
			}
		}
		double legit= X-C*farms;
		double all= rate;
		double awesome= (double(legit)/double(all));
		time=time+awesome;
		fout << std::fixed;
		fout << "Case #" << l << ": ";
		fout << setprecision(7) << (double)time;
		fout << endl;
		l+=1;

	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
