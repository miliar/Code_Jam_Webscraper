#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
    ofstream fout ("output.out");
    ifstream fin ("A-large.in");

    string numTests;
    getline(fin, numTests);
    int num;
    istringstream(numTests) >> num;

    for (int i = 0; i < num; ++i){
        string line;
        getline(fin, line);
        int max;
        string shyness;
        istringstream split(line);
        split >> max;
        split >> shyness;
        //cout << max << " " << shyness << endl;

        int count = 0, pos = 0;
        while (pos < max + 1) {
            //cout << shyness[pos] << endl;
            int posNum = shyness[pos] - '0';
            if(posNum == 0){
                ++count;
                ++pos;
            }
            else{
                //cout << posNum << endl;
                int toAdd = posNum;

                int j = pos + 1;
                int varyEnd = pos + toAdd;
                while (j < min(varyEnd, max + 1)){
                    int extraBetween = shyness[j] - '0';
                    toAdd += extraBetween;
                    varyEnd += extraBetween;
                    ++j;
                }

                pos += toAdd;
                //cout << "Adding: " << toAdd << endl;
            }
        }

        fout << "Case #" << (i+1) << ": " << count << "\n";
    }

    return 0;
}
