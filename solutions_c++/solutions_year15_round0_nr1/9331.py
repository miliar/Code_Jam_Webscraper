#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main (){

ifstream in("input.txt");
ofstream out("output.txt");

int t;
int smax;
int *s;
char r_ch;

in >> t;
for ( int i = 0 ; i < t; ++i ){

	in >> smax;

	s = new int[ smax + 1 ];

	for ( int j = 0; j <= smax; ++j ){
		in >> r_ch;
		s[j] = r_ch - '0';
	}

	int invited = 0;
	int counted = 0;

	counted += s[0];

	for ( int j = 1; j <= smax ; ++j ){
		 if (  j > counted ){
		 	invited += j - counted;
		 	counted += j - counted;
		 }
		 counted += s[j];
	}

	out <<"Case #" << (i + 1) << ": "<< invited << endl;

	delete [] s;
	s = NULL;


}

in.close();
out.close();
return 0;
}