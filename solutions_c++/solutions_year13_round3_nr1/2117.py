//============================================================================
// Name        : round1.cpp
// Author      : rodrijuana
// Date	(D/M/Y): 12/05/2013
//============================================================================
#include <fstream>
#include <string>
#include <math.h>
//#include <iostream>

using namespace std;

int main() {

//ifstream input("inputA-small.in");
ifstream input("A-small-attempt0.in");
ofstream output("A-small-attempt0.out");

int cnt, CNT;
int n ;
int nv ;
string name;

string::iterator it_1;
string::iterator it_2;

input >> CNT;

for (cnt = 1; cnt <= CNT; cnt++)
{   //get case
	input >> name;
	input >> n;

	nv = 0;

	it_1= name.begin();

	while ( it_1 != name.end())
	{

		it_2 = it_1;

		while (it_2 != name.end())
		{
			int aux = 0;
			while (*it_2 != 'a' && *it_2 != 'e' && *it_2 != 'i' &&
					*it_2 != 'o' && *it_2 != 'u' && aux != n && it_2!= name.end())
			{
				aux++;
				it_2++;
			}

			if (aux == n) {
				nv++;
				while (it_2 != name.end()) {
					nv++;
					it_2++;
				};
			}
			else
				if ( it_2 != name.end() )
				it_2++;
		}

		it_1++;

	}//while

	output << "Case #" << cnt << ": " << nv << '\n';
}


}


