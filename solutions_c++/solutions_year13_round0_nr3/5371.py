#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
using namespace std;

bool isPalindrome(long long x)
{
	string s="";
	while(x!=0)
	{
		s += (char)(x%10+'0');
		x/=10;
	}
	for(long long i=0; i<(long long)s.length()/2; i++)
	{
		if(s[i]!=s[s.length()-1-i])
			return false;
	}
	return true;
}

int main()
{
	ifstream infile("C-small-attempt0.in");
	ofstream outfile("output.txt");
	int t;
	infile >> t;
	double a,b;
	long long x,y;
	for(int l=0; l<t; l++)
	{
		infile >> a >> b;
		x = (long long)sqrt(a);
		if((double)x != sqrt(a))
			x++;
		y = (long long)sqrt(b);

		unsigned int count=0;
		for(long long i=x; i<=y; i++)
		{
			if(isPalindrome(i) && isPalindrome(i*i))
				count++;
		}
		outfile << "Case #" << l+1 << ": " << count << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}