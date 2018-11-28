#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

bool first_half(const string& s)
{
	if(s[0] != '1') return false;
	for(int i = 1; i < (int)floor((float)s.size() / 2); ++i)
		if(s[i] != '0') return false;

	return true;
}

bool second_half0(const string& s)
{
	if(s.size() == 1) return false;
	for(int i = s.size() / 2; i < s.size(); ++i)
		if(s[i] != '0') return false;

	return true;
}

int main()
{
	cout << "Hello" << endl;
	ifstream file("A-small-attempt5.in");
	ofstream ofile("res.out");
	int tests;
	file >> tests;

	for(int i =0; i < tests; ++i)
	{
		long long j;
		long long nb_coup = 1;

		file >> j;
		while(j > 1)
		{ 
			auto s = to_string(j);
			if(second_half0(s))
			{
				j--;
				nb_coup++;
				continue;
			}
			
			int size = s.size();
			if(size == 1)
			{
				nb_coup += j -1;
				j = 1;
				break;
			}
			if(!first_half(s))
			{
				string half = s.substr(ceil(((float)s.size())/2),s.size());
				long long j3 = atoi(half.c_str());
				
				reverse(s.begin(),s.end());
				for(int l = 0; l < (int)floor((float)s.size() / 2); ++l)
					s[l] = '0';
				s[0] = '1';
				j = atoi(s.c_str());
				nb_coup += j3;
			}
			else
			{
				string s2(s.size(),'0'); 
				s2[0] = '1';
				long long res = atoi(s2.c_str());
				nb_coup += j - res + 1;
				j = res - 1;
			}
		}


		ofile << "Case #" << i + 1 << ": " << nb_coup << endl;
	}



	return 0;
}
