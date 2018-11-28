#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <cmath>
#include <stack>
#include <queue>
#include <fstream>
#include <set>

using namespace std;

typedef map < int, int>::iterator itr  ;
typedef set<int>::iterator ITR;

ifstream in;
ofstream out;

int main() {

	in.open("file.txt");
	out.open("output.txt");

	while (!in.eof()){

		int t, x, r, c;
		in >>t;
		for (int i=1; i<=t; i++)
		{
			in >>x>>r>>c;
			out<<"Case #"<<i<<": ";
			bool f = false;
			if (r*c ==1 && x==1)
			{
				out<<"GABRIEL"<<endl;
				f = true;
			}
			if (r*c ==2 && (x==1 || x==2))
			{
				out<<"GABRIEL"<<endl;
				f = true;
			}
			if (r*c ==3 && x==1)
			{
				out<<"GABRIEL"<<endl;
				f = true;
			}
			if (r*c ==4 && (x==1 || x==2))
			{
				out<<"GABRIEL"<<endl;
				f = true;
			}
			if (r*c ==6 && (x==1 || x==2 || x==3))
			{
				out<<"GABRIEL"<<endl;
				f = true;
			}
			if (r*c ==8 && (x==1 || x==2 ))
			{
				out<<"GABRIEL"<<endl;
				f = true;
			}
			if (r*c ==9 && (x==1 || x==3))
			{
				out<<"GABRIEL"<<endl;
				f = true;
			}
			if (r*c ==12 && (x==1 || x==2 || x==3 || x==4))
			{
				out<<"GABRIEL"<<endl;
				f = true;
			}
			if (r*c ==16 && (x==1 || x==2 || x==4))
			{
				out<<"GABRIEL"<<endl;
				f = true;
			}

			if (!f)
				out<<"RICHARD"<<endl;


		}

	}

	return 0;
		}
