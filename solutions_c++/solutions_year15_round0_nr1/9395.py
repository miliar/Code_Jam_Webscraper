#include <stdio.h>
#include <iostream>   // For '<<' and '>>', cin, cout and cerr (for errors).
#include <fstream>    // To read in and write out files, and includes istream.getline(char* s, streamsize n, char delim).
#include <stdlib.h>   // Includes the "atoi" function.
#include <string>     // May want for "getline(isteam& is,string& out,char delim='\n')".
using namespace std;
int main()
{
    ifstream in ("A-large.in");         // The file we want to read in.
    ofstream out("A-large.out");        // The file we want to output to.
    if (!in.is_open() || in.eof())               // Error checking just slows us down.
    {
        cerr << "ERROR: invalid input file" << endl;
        return (-1);
    }
    if(!out.is_open())                            // So for code jam you shouldn't bother with these!
    {
        cerr << "ERROR: couldn't create ouput file" << endl;
        return (-1);
    }
    int T,smax,standing,total,totalInvite,caseCount,i,k,j;
    char smaxString[1000];
    string line;                        // |-- If we want to call "getline" continually we need some type of string
    getline(in, line, '\n');            // |   then need to read in each line, and then have the great
    T = atoi(line.c_str());
    k = 0;
    j = 1;
    while(T--){
        if(in.eof())  { return (-1); }
        in >> smax;                            // |-- The >> operator is far easier than getline
        in >> smaxString;                            // |   and checking "in.eof()" for each variable.

        total = 0;
        totalInvite = 0;
        standing = 0;
        i = 0;
        for (int i=0; i<smax + 1; i++)
        {
            total = total + (int)smaxString[i] - '0';
        }
        k = 0;
        bool repeat = false;
        while(standing != total){
            int currentValue = (int)smaxString[k] - '0';
            if(currentValue > 0){
                if(k <= 0){
                    standing += currentValue;
                }else{
                    if(standing >= k){
                        standing += currentValue;
                        repeat = false;
                    }else{
                        int partialInvite = k - standing;
                        total += partialInvite;
                        standing += partialInvite + currentValue;
                        totalInvite += partialInvite;
                    }
                }
            }
            k++;
        }
            out <<  "Case #" << j << ": " << totalInvite << "\n";
        //cout << "" << j << "\n";
        j++;
    }
    in.close();       // |-- If we want to be proper we'd also want to close our files
    out.close();      // |   (yet more lines of code).
    return 0;
}
