#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <string>
using namespace std;

long long mi, ma;
string NumberToString(long long Number)
{
	ostringstream ss;
	ss << Number;
	return ss.str();
}

bool pal(long long test)
{
	string s = NumberToString(test);
	for(int p = 0; p < s.length()/2; p++)
		if(s[p] != s[s.length()-p-1])
			return 0;
	return 1;
}

bool sq(long long test)
{
	long double s = sqrt((long double)test);
	long long t = (long long)s;
	return (t < s + 0.0001) && (t > s - 0.0001);
}


int main()
{
	int tests;
	int count;
	long long temp;
	ifstream in("data.in", ifstream::in);
	in >> tests;
	for(int i = 0; i < tests; i++)
	{
		count = 0;
		in >> mi;
		in >> ma;
		for(int k = mi; k < ma + 1; k++)
		{
			temp = (long long)sqrt((long double)k);
			if(pal(k) && sq(k) && pal(temp))
				count++;
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	return 0;
}
