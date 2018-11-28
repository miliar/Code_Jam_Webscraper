#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <list>

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
	ifstream in("file.in");
	ofstream out("file.out");

	int cases=0;
	string line;

	in >> cases;
	getline(in, line);

	for(int nc=1; nc<= cases; ++nc)
	{


		OUT << "Case #" << nc << ": ";
		getline(in, line);
		int len = line.length();
		list<char> ph;
		for(int i=0; i<len; ++i)
			ph.push_back(line[i]);

		string retval="";

		list<char>::iterator it;

		it = find(ph.begin(), ph.end(), 'Z');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'E');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'R');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'O');
			ph.erase(it);

			retval += "0";
			it = find(ph.begin(), ph.end(), 'Z');
		}

		it = find(ph.begin(), ph.end(), 'W');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'T');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'O');
			ph.erase(it);

			retval += "2";
			it = find(ph.begin(), ph.end(), 'W');
		}

		it = find(ph.begin(), ph.end(), 'U');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'F');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'O');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'R');
			ph.erase(it);

			retval += "4";
			it = find(ph.begin(), ph.end(), 'U');
		}

		it = find(ph.begin(), ph.end(), 'X');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'S');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'I');
			ph.erase(it);

			retval += "6";
			it = find(ph.begin(), ph.end(), 'X');
		}

		it = find(ph.begin(), ph.end(), 'R');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'T');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'H');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'E');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'E');
			ph.erase(it);

			retval += "3";
			it = find(ph.begin(), ph.end(), 'R');
		}

		it = find(ph.begin(), ph.end(), 'O');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'N');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'E');
			ph.erase(it);

			retval += "1";
			it = find(ph.begin(), ph.end(), 'O');
		}

		it = find(ph.begin(), ph.end(), 'F');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'I');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'V');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'E');
			ph.erase(it);

			retval += "5";
			it = find(ph.begin(), ph.end(), 'F');
		}

		it = find(ph.begin(), ph.end(), 'S');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'E');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'V');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'E');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'N');
			ph.erase(it);

			retval += "7";
			it = find(ph.begin(), ph.end(), 'S');
		}

		it = find(ph.begin(), ph.end(), 'G');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'E');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'I');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'H');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'T');
			ph.erase(it);

			retval += "8";
			it = find(ph.begin(), ph.end(), 'G');
		}

		it = find(ph.begin(), ph.end(), 'N');
		while(it!=ph.end())
		{
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'I');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'N');
			ph.erase(it);
			it = find(ph.begin(), ph.end(), 'E');
			ph.erase(it);

			retval += "9";
			it = find(ph.begin(), ph.end(), 'N');
		}

		sort(retval.begin(), retval.end());
		OUT << retval;

		if(nc != cases) OUT << endl;
	}
	in.close();
	out.close();

	GETC
		return 0;
}
