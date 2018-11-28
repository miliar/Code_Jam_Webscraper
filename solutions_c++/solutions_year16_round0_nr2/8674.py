#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <set>
#include <sstream>
#include <iterator>

using namespace std;

int main()
{
    ifstream infile("large.in");
    ofstream outfile("large.txt");
    string line;
    int count;
    int flipnum;

    // read number of instances
    getline(infile,line);
    count = atoi(line.c_str());
    cout << "T = " << count << endl;

    for (int i=0; i<count; i++)
    {
        line.clear();
        flipnum = 0;
        //read buget for each case
        getline(infile, line);
        cout << endl << "new pile = " << line << endl;

        int leng = line.length();
        for (int j=0; j<leng-1; j++){
            if (line[j]!=line[j+1]){
                flipnum++;
            }
        }
        if (line[leng-1] == '-')
            flipnum++;

        outfile << "Case #" << i+1 <<": " << flipnum << endl;
        cout << "Case #" << i+1 <<": " << flipnum << endl;
    }

    infile.close();
    outfile.close();
    return 0;
}



