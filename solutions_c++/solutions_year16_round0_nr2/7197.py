#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
#include <sstream>
using namespace std;

int main ()
{
        int T;
        string line;
        ifstream infile;
        ofstream outfile;
        infile.open ("B-large.in");
        outfile.open ("B-large.out");

//	infile >> T;
//	scanf ("%d\n", &T);
	getline (infile, line);
	istringstream ss(line);
	ss >> T;

        for (int t=1; t<=T; t++)
	{
		string s = "";
		getline (infile, s);
		int res = 0, len = s.length();

		if (len >= 1)
			if (s[0]=='-')
				res++;

		for (int i=1; i<len; i++)
		{
			if (s[i] != s[i-1] && s[i-1]=='+')
				res+=2;
		}

		outfile<<"Case #"<<t<<": "<<res;
		outfile<<endl;
	}
        infile.close();
        outfile.close();

        return 0;
}
