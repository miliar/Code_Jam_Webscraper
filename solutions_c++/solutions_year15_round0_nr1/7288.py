
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int main (){
    ifstream fin("./Downloads/A-large.in", ios::in);
    ofstream fout("./Desktop/answer-large.out", ios::out);

    int T;
    fin >> T;

    for (int i = 1; i <= T; i++){
        /* declarations */
        int count, max, acc, ind;

        string lis;
        /* input */
        fin >> max >> lis;

        /* Processing */
        ind = 0;
        count = 0;
        acc = 0;

        for (int j = 0; j <= max; j++)
        {
            if (j > acc){
                count+= j - acc;
                acc+= j - acc;
            }
            acc += lis[j] - '0';
        }

        /* output */
        fout << "Case #" << i << ": " << count << "\n";
    }

    return 0;

}