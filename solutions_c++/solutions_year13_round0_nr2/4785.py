#include<iostream>
#include<fstream>
#include<string>

//#define USE_STDIN

using namespace std;

#include "Lawn.h"

int main()
{

#ifdef USE_STDIN
	istream& in = cin;
#else
	ifstream infile;
	infile.open ("B-large.in", ifstream::in);
	istream& in = infile;
#endif

	ofstream outfile;
	outfile.open("B-large.out", ofstream::out);


    int T;
	in >> T;


	for( int i=0; i<T; i++ ){
		int N, M;
		in >> N;
		in >> M;
		
		Lawn lawn = Lawn(N, M);

		int max = 0;
		for( int row=0; row<N; row++ ){
			for( int col=0; col<M; col++ ){
				
				int iGrassHeight;
				in >> iGrassHeight;

				lawn.board[row][col] = iGrassHeight;
				lawn.solved[row][col] = false;
				lawn.sequence.push_back( iGrassHeight );
				lawn.aCountBox[ iGrassHeight ]++;
			}
		}

		outfile << "Case #" << i+1 << ": ";
		outfile << ((lawn.hasSolution())? "YES" : "NO");
		outfile << endl;
	}
	
#ifdef USE_STDIN

#else
	infile.close();
#endif
	outfile.close();
}