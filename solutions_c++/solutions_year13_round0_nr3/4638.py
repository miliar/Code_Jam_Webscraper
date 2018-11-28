#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

bool isPalindrome (double num)
{
	stringstream st;
	string s;
	string::iterator istr, iend;

	st << num;
	s = st.str ();

	istr = s.begin ();
	iend = s.end () - 1;

	for (double i = 0; i < (s.size()/2); ++i)
	{
		if (*(istr + i) != *(iend - i))
		{
			cout << "num:" << num << " " << *istr << " " << *iend << " false" << endl;
			return false;
		}
	}
	cout << "num:" << num << " " << *istr << " " << *iend << " true" << endl;
	return true;
}

double cfairnsqr (double start, double end)
{
	double count = 0;

	for (double i = ceil(sqrt (start))
		 ; i * i <= end
		 ; ++i)
	{
		if (isPalindrome (i*i) && isPalindrome (i))
			++count;
	}
	return count;
}

int main ()
{
	double tn, str, end;
	ifstream fin("testcase.txt");
	ofstream fout("result.txt");

	fin >> tn;

	for (double i = 0; i < tn; ++i)
	{
		fin >> str;
		fin >> end;
		fout << "Case #" << i+1 << ": " << cfairnsqr (str,end) << endl;
		cout << "t1" << endl;
	}

	fin.close();
	fout.close();
	getchar();
	return 0;
}
