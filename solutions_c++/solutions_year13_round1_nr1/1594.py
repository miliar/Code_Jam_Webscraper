#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<string>

//#define USE_STDIN

using namespace std;

int main()
{

#ifdef USE_STDIN
	istream& in = cin;
#else
	ifstream infile;
	infile.open ("A-small-attempt0.in", ifstream::in);
	istream& in = infile;
#endif

	ofstream outfile;
	outfile.open("A-small-attempt0.out", ofstream::out);

    int T;
	in >> T;

	for( int i=0; i<T; i++ ){
		
		int r;
		int t;

		in >> r;
		in >> t;

		int init = (r << 1) + 1;
		int used = init;

		t -= used;


		int count = 0;

		while( t >= 0 ){
			count++;
			used += 4;
			t -= used;
		}

		outfile << "Case #" << i+1 << ": ";
		outfile << count;
		outfile << endl;
	}
	
#ifdef USE_STDIN

#else
	infile.close();
#endif
	outfile.close();
}