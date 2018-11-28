/*
 * Compilation:
 * gcc <file>.cpp
 *
 * Usage:
 * ./a.out <input file> <output file>
 */

#include <stdint.h>
#include <algorithm>
#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <assert.h>
#include <stdio.h>


using namespace std;


int main(int argc, char *argv[])
{
	assert(argc == 3);

	/* open and read file passed as first command-line argument */
    ifstream fin (argv[1], fstream::in);

    /* open output file */
    ostringstream sout;
    sout << argv[2] << ".tmp";
    ofstream fout(sout.str().c_str(), fstream::out);

    /* read number of cases */
    int T;
    fin >> T;

    for (int c = 1; c <= T; c++) {
        /* read case */
        int R, C, W;
        fin >> R >> C >> W;
        
        /* First hit: */
        int a = C / W;
        if (C % W == 0 && W > 1)
            a--;
        cerr << "first hit " << a << endl;

        /* In every row: */
        a = a * R;
        cerr << "every row " << a << endl;

        /* Finish him: */
        a += W - 1;
        /* He will make me miss at least once: */
        if (W > 1)
            a ++;
        //a += C % W;
        cerr << "finished " << a << endl;

        /* solve case */
        ostringstream answer;
        answer << a;

        /* store solution */
        fout << "Case #"<< c << ": " << answer.str() << endl;
    }

    fout.close();
    rename(sout.str().c_str(), argv[2]);

	return 0;
}

