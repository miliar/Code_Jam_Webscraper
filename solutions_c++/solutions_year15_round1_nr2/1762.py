#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <fstream>
#include <list>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <cmath>

#include <numeric>

using namespace std;


#define MUSHROOM 0
#define HAIRCUT 1
#define LOGGING 0



#if HAIRCUT

int gcd(int a, int b)
{
	for (;;)
	{
		if (a == 0) return b;
		b %= a;
		if (b == 0) return a;
		a %= b;
	}
}

int lcm(int a, int b)
{
	int temp = gcd(a, b);

	return temp ? (a / temp * b) : 0;
}

int main()
{
	ifstream in("input.in");
	ofstream out("out.txt");


	int ncase; in >> ncase;
	for (int icase = 0; icase < ncase; icase++)
	{
		int nbarbs; in >> nbarbs;
		int pos; in >> pos;

		vector<int> times(nbarbs);
		for (int i = 0; i < nbarbs; i++)
		{
			in >> times[i];
		}

		int LCM = times[0];
		int GCD = times[0];
		for (int i = 1; i < times.size(); i++)
		{
			LCM = lcm(LCM, times[i]);
			GCD = gcd(GCD, times[i]);
		}
		vector<int> status(nbarbs, 0);
		int cur_time = 0;
		int served = 0;

		while (cur_time < LCM)
		{
			//fill up
			for (int i = 0; i < nbarbs && pos > 0; i++)
			{
				if (status[i] == 0)
				{
					served++;
					status[i] = times[i];
				}
			}
			for (int i = 0; i < status.size(); i++)
			{
				status[i]-=GCD;
			}
			cur_time += GCD;
		}
		/*
		int skip_ahead = pos / LCM;
		if (served != 0)
		pos %= served;
		*/


		pos = (pos-1) % served ;

		int answer = -1;
		status=vector<int>(nbarbs, 0);

		if (pos == 0)
		{
			out << "Case #" << icase + 1 << ": ";
			out << 1 << endl;
			continue;
		}
		pos++;
		while (true)
		{
			//fill up
			for (int i = 0; i < nbarbs && pos > 0; i++)
			{
				if (status[i] == 0)
				{
					pos--;
					status[i] = times[i];
					if (pos == 0)
					{
						answer = i;
						break;
					}
				}
			}
			if (pos == 0)
			{
				break;
			}
			for (int i = 0; i < status.size(); i++)
			{
				status[i] -= GCD;
			}
		}
		

		//simulate

		out<< "Case #" << icase + 1 << ": ";
		out << answer+1 << endl;
	}

}


#endif