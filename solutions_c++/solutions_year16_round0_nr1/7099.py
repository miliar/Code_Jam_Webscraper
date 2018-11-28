#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
#include <set>
using namespace std;

int main ()
{
        int T;
        string line, line2;
        ifstream infile;
        ofstream outfile;
        infile.open ("A-large.in");
        outfile.open ("A-large.out");

	infile>>T;

        for (int t=1; t<=T; t++)
	{
		int N;
		set<int> s;
		infile>>N;

		if (N==0)
		{
			outfile<<"Case #"<<t<<": INSOMNIA"<<endl;
			continue;
		}

		long mult = 1, num, num1;

		while (s.size() < 10)
		{
			num = N*mult;
			num1 = num;
			while (num)
			{
				s.insert (num%10);
				num = num/10;
			}
			mult++;
		}

		outfile<<"Case #"<<t<<": "<<num1;
		outfile<<endl;
	}
        infile.close();
        outfile.close();

        return 0;
}
