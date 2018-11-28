
#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
#include<vector>

using namespace std;

string say(bool t);

int main(int agrc, char* agrv[])
{


	ifstream in("D-small-attempt2.in");
	ofstream out("D-small-attempt2.out");

	
	int testCase;
	in >> testCase;
	for (int t = 0; t < testCase; ++t)
	{
		int x, r, c;
		in >> x >> r >> c;
		int _max , _min;
		if (r > c)
		{
			_max = r;
			_min = c;
		}
		else
		{
			_max = c;
			_min = r;
		}
		if ( (_max * _min) % x != 0 )
		{
			//채우기 실패
			out << "Case #" << t+1 << ": " << say(false) << endl;
		}
		else
		{
			if (x > _max)
			{
				out << "Case #" << t + 1 << ": " << say(false) << endl;
			}
			else
			{
				int x_min = (int)floor((x + 1) / 2.0);
				if (x_min > _min )
				{
					out << "Case #" << t + 1 << ": " << say(false) << endl;
				}
				else
				{
					if (x < 4 || _min > x_min)
					{
						out << "Case #" << t + 1 << ": " << say(true) << endl;
					}
					else
					{
						out << "Case #" << t + 1 << ": " << say(false) << endl;
					}
				}
			}
		}

	}

	//in.close();
	//out.close();

	return 0;
}

string say(bool t)
{
	if (t) return "GABRIEL";
	else return "RICHARD";
}