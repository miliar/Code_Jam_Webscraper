#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <stack>
#include <list>
#include <deque>
#include <map>
#include <bitset>
#include <string>
#include <sstream>
#include <algorithm>


using namespace std;

bool checkPali(string temp)
{
	long n = temp.length()/2;
	for(long i = 0; i < n; i++)
	{
		if (temp[i]!=temp[temp.length()-i-1])
			return false;
	}
	return true;
}

int main()
{
	long long n;
	ifstream in("C-large-1.in");
	ofstream out("output1.out");
	in >> n;

	vector<long long> fairsquare;

	for(long long i = 1; i <= 10000000; i++)
	{
		stringstream s,s1;
		long long temp = i * i;
		s << temp;
		s1 << i;
		if(checkPali(s.str()) && checkPali(s1.str()))
			fairsquare.push_back(temp);
	}

	for(long long cases = 1; cases <= n; cases++)
	{
		long long a, b; 
		in >> a >> b;
		long long countme=0;
		for(long long i=0;fairsquare[i]<=b;i++)
		{
			if(fairsquare[i]>=a)
				countme++;
		}
		out << "Case #" << cases << ": " << countme << endl;
	}
	system("pause");
	return 0;
}