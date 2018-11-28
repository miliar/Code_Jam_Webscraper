#include <tchar.h> 
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/join.hpp>
using namespace std;


namespace String
{
	vector<string> Split(const string& str, const string& sep)
	{
		vector<string> ret;
		boost::split(ret, str, boost::is_any_of(sep));
		return ret;
	}
	vector<string> Split(const string& str, const char sep)
	{
		char separray[2] = {sep, '\0'};
		string sepators = separray;
		return Split(str, sepators);
	}

	string Unsplit(const vector<string>& vals, const string& sep)
	{
		string str = boost::algorithm::join(vals, sep);
		return str;
	}
	string Unsplit(const vector<string>& vals, const char sep)
	{
		char separray[2] = {sep, '\0'};
		string sepators(separray);
		return Unsplit(vals, sepators);
	}
}

template<class T>
void splitstr(const string& s, vector<T>& out)
{
	stringstream in(s);
	out.clear();
	copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

int str2int(const string& str) 
{
	stringstream ss(str);
	int num;
	if ((ss >> num).fail())
	{ 
		//ERROR 
	}
	return num;
}

vector<int> intToAnyBase(int x, int base) 
{
    assert(base >= 2);
    std::vector<int> v;
    while (x > 0)
	{
        v.push_back(x % base);
        x /= base;
    }
    std::reverse(v.begin(), v.end());
    return v;
}

bool isPalindrome(int i)
{
	vector<int> v = intToAnyBase(i, 10);
	vector<int> vr = v;
    std::reverse(vr.begin(), vr.end());
	return v == vr;
}

int TestCase(ifstream& input)
{
	string line;
	vector<int> v;
	getline(input, line);
	splitstr(line, v);
	int A = v[0];
	int B = v[1];
	//cout << A << "\t" << B << endl;
	int sqA = int(sqrt(double(A)));
	int sqB = int(sqrt(double(B)));

	int count = 0;
	for (int i=sqA; i<=sqB+1; i++)
	{
		int sqi = i*i;
		if (A<=sqi && sqi <=B && isPalindrome(i) && isPalindrome(sqi))
			count++;
	}

	return count;
}


int _tmain(int argc, _TCHAR* argv[])
{
	//ifstream input("A-large.in");
	ifstream input("C-small-attempt0.in");
	//ifstream input("test.in");

	ofstream myfile("result.txt");

	string line;
	getline(input, line);
	int T = str2int(line);
	cout << "number of cases : " << T << endl;

	for (int i = 0; i<T; i++)
	{
		int res = TestCase(input);
		cout << "Case #" << i+1 << ": "  << res << endl;
		myfile << "Case #" << i+1 << ": "  << res << endl;
	}
	myfile.close();

	return 0;
}
