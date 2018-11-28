#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <bitset>
#include <cmath>
//#include "gmpxx.h"

using namespace std;

int main()
{
    string problemLetter = "A";

    //string testFile = problemLetter+"-input";
    string testFile = problemLetter+"-small-attempt0";
    //string testFile = problemLetter+"-large";

    cout << "Runnig problem " + problemLetter << " on " << testFile << ".in" << endl;

    string infile = testFile + ".in";
    string outfile = testFile + "-output.out";
    ifstream fin( infile.c_str() );
    ofstream fout( outfile.c_str() );

    if (!fin.is_open()) cout << infile + " open fail" << endl;
    if (!fout.is_open()) cout << outfile + " open fail" << endl;

    int numCase;
    fin >> numCase;

    int answer;
    for (int caseIt = 0; caseIt < numCase; caseIt++)
    {
        string str;
        fin >> str;

        const char * p = str.c_str();
        char s[1000] ;
        int begin = 0;
        int end = 1;

        s[0] = p[0];
        for (int i = 1 ; i <= str.length() ; i++) {
            if (s[begin] <= p[i]  ) {
                begin--;
                if (begin < 0) {
                    begin += 1000;
                }
                s[begin] = p[i];

            } else {
                end++;
                s[end-1] = p[i];
            }
        }
        s[end] = '\0';

        if (begin < end) {
            cout << "Case #" << (caseIt + 1) << ": " << s << endl;
            fout << "Case #" << (caseIt + 1) << ": " << s << endl;
        } else {
            string left = string(&(s[begin]), 1000 - begin);
            string right = string(s, end - 1);
            cout << "Case #" << (caseIt + 1) << ": " << left + right << endl;
            fout << "Case #" << (caseIt + 1) << ": " << left + right << endl;
        }

    }

    fin.close();
    fout.close();
    return 0;
}
