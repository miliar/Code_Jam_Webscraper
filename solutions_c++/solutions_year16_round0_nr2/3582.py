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

int countJump(string& str){
    int count = 0;
    unsigned long length = str.length();

    for (int i=1; i<length; i++) {
        if (str[i] != str[i-1])
            count++;
    }
    return count;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    string line;
    ifstream ifile ("B-large.in.txt");
    ofstream ofile;
    ofile.open ("output.txt");

    if (ifile.is_open() && ofile.is_open())
    {
        getline (ifile,line);
        int totalCases = stoi(line);
        
        for(int i=1; getline (ifile,line) && i<=totalCases; i++)
        {
            int count = countJump(line);
            if(line[line.length()-1] == '-')
                count++;
            
            ofile << "Case #" << i <<": " << count << endl;
            
        }
        ifile.close();
        ofile.close();
    }
    
    else cout << "Unable to open file";
    
    return 0;
}
