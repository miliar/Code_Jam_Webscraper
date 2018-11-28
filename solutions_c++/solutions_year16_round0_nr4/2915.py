//
//  main.cpp
//  codejam
//
//  Created by Saurabh Goyal on 09/04/16.
//  Copyright © 2016 saurabhgoyal. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

unsigned long long pow(unsigned long long num, int power){
    unsigned long long value = 1;
    for (int i=0; i<power; i++) {
        value *= num;
    }
    return value;
}

unsigned long long index(int k, int c, int i, int j)
{
    unsigned long long num = pow((unsigned long long)(k), --c) * (i-1);
    while (c != 0) {
        num += pow((unsigned long long)(k), --c) * (j-1);
    }
    num++;
    return num;
}

int main(int argc, const char * argv[]) {
    // insert code here...

    string line;
    ifstream ifile ("D-small-attempt0.in.txt");
    ofstream ofile;
    ofile.open ("output.txt");

    if (ifile.is_open() && ofile.is_open())
    {
        getline (ifile,line);
        int totalCases = stoi(line);
        
        for(int i=1; getline (ifile,line) && i<=totalCases; i++)
        {
            int k=0, c=0, s=0;
            sscanf (line.c_str(),"%d %d %d", &k, &c, &s);
            
            if (s < (k+1)/2) {
                ofile << "Case #" << i <<": " << "IMPOSSIBLE" << endl;
            }else if(k==1){
                ofile << "Case #" << i <<": 1\n";
            }else if(c==1){
                if(s<k)
                    ofile << "Case #" << i <<": " << "IMPOSSIBLE" << endl;
                else{
                    ofile << "Case #" << i <<": ";
                    for (int j=1; j<=k; j++) {
                        if (j != 1) {
                            ofile << " ";
                        }
                        ofile << j;
                    }
                    ofile << endl;
                }
            }else{
                ofile << "Case #" << i <<": " ;

                for (int j=1; j<=k; j+=2) {
                    int l = j+1;
                    if (j==k)   l--;
                    unsigned long long temp = index(k, c, j, l);

                    if (j != 1) {
                        ofile << " ";
                    }
                    ofile << temp;
                }
                ofile << endl;
            }
            
        }
        ifile.close();
        ofile.close();
    }
    
    else cout << "Unable to open file";
    
    return 0;
}
