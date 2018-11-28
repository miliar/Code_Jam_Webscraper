#include "string.h"
#include <cstring>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
#include <stack>
#include <list>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <limits.h>
#include <fstream>
using namespace std;


void countDigitals(vector<int>& digitals, long long n, int& count)
{
	while (n > 0){

		int d = n % 10;
		if (!digitals[d]){
			digitals[d] = 1;
			++count;
		}
		n = n / 10;
	}
}

int main()
{
	int t, n;
	ifstream istream;
	istream.open("input.in");
	istream >> t;
	ofstream ostream;
	ostream.open("output.in");
	int i = 0;
	while (t--)
	{
		i++;
		istream >> n;
		if (n == 0) {
			ostream << "Case #" << i << ": " <<"INSOMNIA" << endl;
			continue;
		}
		vector<int> digitals(10, 0);
		int count = 0;
		long long digital = 0;
		while (count < 10)
		{
			digital += n;
			countDigitals(digitals, digital, count);
		}
		ostream << "Case #" << i << ": " << digital << endl;
	}
	ostream.flush();
	ostream.close();
	return 0;
}