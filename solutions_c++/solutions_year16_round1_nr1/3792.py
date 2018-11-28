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
        infile.open ("A-large.in");
        outfile.open ("A-large.out");

//	infile >> T;
//	scanf ("%d\n", &T);
	getline (infile, line);
	istringstream ss(line);
	ss >> T;

        for (int t=1; t<=T; t++)
	{
		string s = "";
		getline (infile, s);

		string res = "";
		if (s.length()>=1) res+=s[0];
		for (int i=1; i<s.length(); i++)
		{
			if (s[i]>=res[0])
				res = s[i]+res;
			else
				res = res+s[i];
		}

		outfile<<"Case #"<<t<<": "<<res;
		outfile<<endl;
	}
        infile.close();
        outfile.close();

        return 0;
}
