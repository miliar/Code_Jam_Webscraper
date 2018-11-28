#include<iostream>
#include<fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
	ifstream ifile("A-large.in");
	ofstream ofile;
	ofile.open("A-large.out");
	long long t, cases = 0;
	string s;
	ifile>>t;
	while(t--)
	{
		ifile>>s;
		long long n = s.length();
		vector<int> res;
		vector<long long> hash(26,0);
		for(long long i = 0; i < n; ++i)
		{
			++hash[s[i] - 'A'];
		}
		n = hash['Z' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['Z' - 'A'];
			--hash['E' - 'A'];
			--hash['R' - 'A'];
			--hash['O' - 'A'];
			res.push_back(0);
		}
		n = hash['W' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['T' - 'A'];
			--hash['W' - 'A'];
			--hash['O' - 'A'];
			res.push_back(2);
		}
		n = hash['U' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['F' - 'A'];
			--hash['O' - 'A'];
			--hash['U' - 'A'];
			--hash['R' - 'A'];
			res.push_back(4);
		}
		n = hash['X' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['S' - 'A'];
			--hash['I' - 'A'];
			--hash['X' - 'A'];
			res.push_back(6);
		}
		n = hash['G' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['E' - 'A'];
			--hash['I' - 'A'];
			--hash['G' - 'A'];
			--hash['H' - 'A'];
			--hash['T' - 'A'];
			res.push_back(8);
		}
		n = hash['O' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['O' - 'A'];
			--hash['N' - 'A'];
			--hash['E' - 'A'];
			res.push_back(1);
		}
		n = hash['T' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['T' - 'A'];
			--hash['H' - 'A'];
			--hash['R' - 'A'];
			--hash['E' - 'A'];
			--hash['E' - 'A'];
			res.push_back(3);
		}
		n = hash['F' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['F' - 'A'];
			--hash['I' - 'A'];
			--hash['V' - 'A'];
			--hash['E' - 'A'];
			res.push_back(5);
		}
		n = hash['S' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['S' - 'A'];
			--hash['E' - 'A'];
			--hash['V' - 'A'];
			--hash['E' - 'A'];
			--hash['N' - 'A'];
			res.push_back(7);
		}
		n = hash['I' - 'A'];
		for(long long i = 0; i < n; ++i)
		{
			--hash['N' - 'A'];
			--hash['I' - 'A'];
			--hash['N' - 'A'];
			--hash['E' - 'A'];
			res.push_back(9);
		}
		sort(res.begin(), res.end());
		ofile<<"Case #"<<++cases<<": ";
		n = res.size();
		for(long long i = 0; i < n; ++i)
			ofile<<res[i];
		ofile<<"\n";
		res.clear();
    }
}


