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

		int m;
		string s;
		int t;
		in>>t;
		for (int i=1; i<=t;i++)
		{
			int sum =0;
			int c=0;

			in>> m>>s;
			for (int j =0;j<(m+1); j++)
			{
				if (sum <j && s[j] > '0')
				{
					c+= j- sum;
					sum += j-sum;
				}
				sum += int(s[j] -48) ;

			}
			out<<"Case #"<<i<<": "<<c<<endl;
					}

	}

	return 0;
		}
