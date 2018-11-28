#include <map>
#include <fstream>
#include <math.h>
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	ifstream fin("cookie.in");
	ofstream fout("cookie.out");
	int N;
	fin >> N;
	for (int cases = 0; cases < N; cases++)
	{
		int r = cases + 1;
		fout << "Case #" << r << ": ";
		double C, F, X;
		fin >> C >> F >> X;
		int i = 1;
		double answer = (X / 2);
		double time = 0;
		do
		{
			double temp;
			time += C / (2 + F*(i-1));
			/*for (int rate = 0; rate < i; rate++)
			{
				time += C / (2 + F*rate);
			}*/
			temp = time + X /(2 + F*i);
			if (temp>=answer) break;
			else
			{
				answer=temp;
				i++;
			}
		} while (true);
		int digits = floor(log(answer));
		cout << cases << endl;
		fout << setprecision(7+digits) << answer << endl;
	}
}