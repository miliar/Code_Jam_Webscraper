//
//  main.cpp
//  codejam
//
//  Created by Saurabh Goyal on 09/04/16.
//  Copyright © 2016 saurabhgoyal. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

bool allTrue(bool* flags){
    if (flags[0] && flags[1] && flags[2] && flags[3] && flags[4] && flags[5] && flags[6] && flags[7] && flags[8] && flags[9])
        return true;
    return false;
}

long getLastNumber(long number) {
    if(number == 0)
        return -1;

    bool flag[10] = {false};
    long ithNumber = number;
    for (int i=1; !allTrue(flag); i++) {
        ithNumber = number * i;
        long temp = ithNumber;
        while (temp != 0) {
            flag[temp%10] = true;
            temp = temp/10;
        }
    }
    return ithNumber;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    string line;
    ifstream ifile ("A-large.in.txt");
    ofstream ofile;
    ofile.open ("output.txt");

    if (ifile.is_open() && ofile.is_open())
    {
        getline (ifile,line);
        int totalCases = stoi(line);
        
        for(int i=1; getline (ifile,line) && i<=totalCases; i++)
        {
            long number = stol(line);
            long lastNumber = getLastNumber(number);
            
            ofile << "Case #" << i <<": ";
            
            if (lastNumber != -1) {
                ofile << lastNumber << endl;
            }else{
                ofile << "INSOMNIA" << endl;
            }
        }
        ifile.close();
        ofile.close();
    }
    
    else cout << "Unable to open file";
    
    return 0;
}
