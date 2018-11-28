#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <bitset>

using namespace std;

string changeToBase10(long long n)
{
	string s = "";
	
	while(n!=0)
	{
		s += to_string(n%2);
		n /= 2;
	}

	reverse(s.begin(), s.end());
	return s;
}

int alternatingSum(long long n)
{
	int sum = 0;
	int sign = 1;

	while(n != 0)
	{
		sum += sign * n%2;
		n /= 2;
		sign *= -1;
	}

	return sum;
}

int main()
{
    ifstream in("small-practice.in");
    //ifstream in("large-practice.in");
    ofstream out("output.out");

    unsigned int T, N, J;
    in >> T >> N >> J;
	out << "Case #1:" << endl;

	long long n = (long long)(pow(2,N-1)+1);
	int found = 0;

    while( found < J )
    {
		if (alternatingSum(n) == 0)
		{
			found++;
			out << changeToBase10(n);
			for(int i = 2; i<=10; i++)
			{
				out << " " << i+1;
			}
			out << endl;
		}

		n += 2;
    }

    return 0;
}
