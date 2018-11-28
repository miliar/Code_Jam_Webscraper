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
        int N;
        fin >> N;
        vector<int> m(N);
        for (int i = 0; i < N; i++)
            fin >> m[i];

        /* solve case */
        ostringstream answer("");

        /* first method */
        int mnum1 = 0;
        for (int i = 1; i < N; i++) {
            if (m[i] < m[i-1]) {
                mnum1 += m[i-1] - m[i];
            }
        }
        answer << mnum1 << " ";

        /* second method */
        int v = 0;
        for (int i = 1; i < N; i++) {
            if (m[i] < m[i-1]) {
                v = max(v, m[i-1] - m[i]);
            }
        }
        int mnum2 = 0;
        for (int i = 0; i < N-1; i++) {
            mnum2 += min(v, m[i]);
        }
        assert(mnum2 >= 0);
        answer << mnum2;

        /* store solution */
        fout << "Case #"<< c << ": " << answer.str() << endl;
    }

    fout.close();
    rename(sout.str().c_str(), argv[2]);

	return 0;
}

