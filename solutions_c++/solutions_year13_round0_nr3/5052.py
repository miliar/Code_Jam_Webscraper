// fairsquare.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

#define ll unsigned long long

ifstream input;
ofstream output;

ll solve()
{
	ll result = 0;
	ll imin, imax;
	ll min, max;

	input >> imin >> imax;

	min = imin;
	max = imax;
	
	min = (ll)floor(sqrt((long double)min)) - 1;
	if(min < 0)
		min = 0;
	
	max = (ll)ceil(sqrt((long double)max)) + 1;

	ll lower = ((min == 0) ? 0 : (ll)(log((long double)min)/log(10.0)));
	ll upper = ((max == 0)? 1 : (ll)(log((long double)max)/log(10.0)));

	if(lower == 0)
		lower = 1;

	lower--;

	if(lower == 0)
		lower = 1;

	upper++;


	for(int count = lower; count <= upper; count++)
	{

		if(count % 2 == 0)
		{
			ll palindromtop = 1;
			for(int i = 0; i < count / 2; i++)
				palindromtop *= 10;

			ll palindrombot = palindromtop / 10;
			palindromtop -= 1;

			char buffer[20];
			for(ll n = palindrombot; n <= palindromtop; n++)
			{
				ltoa(n, buffer, 10);

				string left(buffer);
				string right(buffer);
				reverse(right.begin(), right.end());

				left.append(right);


				ll p = atol(left.c_str());
				cout << p << " = ";

				ll sq = p*p;
				cout << sq;
				ltoa(sq, buffer, 10);
				string strsq1(buffer);
				string strsq2(buffer);
				reverse(strsq2.begin(), strsq2.end());

				if(strsq1.compare(strsq2) == 0 && sq <= imax && sq >= imin)
				{
					result++;
					cout << "is success!";
				}
				cout << endl;
			}
		}
		else
		{
			if(count == 1)
			{
				if(1 <= imax && 1 >= imin)
					result++;
				if(4 <= imax && 4 >= imin)
					result++;
				if(9 <= imax && 9 >= imin)
					result++;
				continue;
			}

			ll palindromtop = 1;
			for(int i = 0; i <= count / 2; i++)
				palindromtop *= 10;

			ll palindrombot = palindromtop / 10;
			palindromtop -= 1;

			char buffer[20];
			for(ll n = palindrombot; n < palindromtop; n++)
			{
				ltoa(n, buffer, 10);

				string left(buffer);
				string right(buffer);
				right.pop_back();
				reverse(right.begin(), right.end());

				left.append(right);


				ll p = atol(left.c_str());
				cout << p << " = ";

				ll sq = p*p;
				cout << sq;
				ltoa(sq, buffer, 10);
				string strsq1(buffer);
				string strsq2(buffer);
				reverse(strsq2.begin(), strsq2.end());

				if(strsq1.compare(strsq2) == 0 && sq <= imax && sq >= imin)
				{
					result++;
					cout << "is success!";
				}
				cout << endl;
			}
		}
	}

	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	input.open("input.txt");
	output.open("output.txt");

	short t;
	input >> t;

	for(short i = 0; i < t; i++)
		output << "Case #" << i + 1 << ": " << solve() << endl;

	input.close();
	output.close();

	return 0;
}