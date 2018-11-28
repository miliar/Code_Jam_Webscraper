#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#define BASE 10

using namespace std;

char digit_to_char(int n)
{
	char index[10] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
	return index[n];
}

string to_string(int num)
{
	vector<char> word_num;

	while(num>0)
	{
		int rem = num % BASE;
		word_num.insert(word_num.begin(),digit_to_char(rem));
		num = (num-rem)/BASE;
	}

	return string( word_num.begin(), word_num.end() );
}


bool is_fair(int n)
{
	string str = to_string(n);
	for(unsigned i=0;2*i<str.length();i++)
	{
		if(str[i] != str[str.length()-i-1])
		{
			return false;
		}
	}
	return true;
}

int main()
{
	ifstream fin("fair.in");
	int T;
	fin>>T;

	ofstream fout("fair.out");

	for(int i=0;i<T;i++)
	{
		int A,B;
		fin>>A>>B;
		int lower = ceil(sqrt((double)A)), upper = floor(sqrt((double)B));
		int cnt = 0;

		for(int k=lower;k<=upper;k++)
		{
			cout<<"TRYING: "<<k*k<<endl;
			cnt += (is_fair(k) && is_fair(k*k)) ? 1 : 0 ;
			if(is_fair(k) && is_fair(k*k))
			{
				cout<<"FOUND: "<<k*k<<endl;
			}
		}

		cout<<"Case #"<<(i+1)<<": "<<cnt<<endl;
		fout<<"Case #"<<(i+1)<<": "<<cnt<<endl;
	}

	return 1;
}
