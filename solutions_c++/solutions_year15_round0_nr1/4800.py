#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>

#define OUT out
#define GETC ;

#ifndef OUT
#define OUT cout
#endif

#ifndef GETC
#define GETC getchar();
#endif

using namespace std;

int main()
{
    ifstream in("files/file.in");
    ofstream out("files/file.out");

    int cases=0;
    string line;

    in >> cases;
    getline(in, line);

    for(int nc=1; nc<= cases; ++nc)
    {
        OUT << "Case #" << nc << ": ";
        getline(in, line);
        stringstream ss;

        ss << line;

		int maxsh=0;
		string str;

		ss >> maxsh >> str;
		long long numppl=0, reqval = 0;

		for(int i=0; i < maxsh + 1; ++i)
		{
			stringstream tmp;
			int tmp_n=0;
			tmp << str[i];
			tmp >> tmp_n;

			if(numppl < i) 
			{
					reqval += i - numppl;
					numppl += i - numppl;
			}
			numppl += tmp_n;
		}
		OUT << reqval;

        if(nc != cases) OUT << endl;
    }
    in.close();
    out.close();
    
    GETC
    return 0;
}
