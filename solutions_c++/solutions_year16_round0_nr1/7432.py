#include <iostream>
#include <fstream>
#include <math.h>
#include <set>
#include <string>

using namespace std;

void main()
{
	ifstream ifs("Resources/input.in", std::ifstream::in);
	unsigned int samples;
	ofstream ofs("Resources/output.txt", std::ofstream::out);
	
	ifs>>samples;
	for(int i=1;i<=samples;i++)
	{
		std::set<int> goal;
		unsigned long int N;
		ifs>>N;

		if(!N)
		{
			ofs<<"Case #"<<i<<": INSOMNIA"<<"\r\n";
		}
		else
		{
			unsigned long stopped_at;
			unsigned int step = 1;
			while(goal.size() < 10)
			{
				unsigned long temp=N*step;
				stopped_at = temp;
				while(temp)
				{
					unsigned int ldigit;
					ldigit = temp%10;
					goal.insert(ldigit);
					temp = (unsigned long int)temp/10;
				}

				step++;
			}
			ofs<<"Case #"<<i<<": "<<stopped_at<<"\r\n";
		}
	}
}