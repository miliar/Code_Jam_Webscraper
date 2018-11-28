//
//  main.cpp
//  Round1B 2014
//
//  Created by Lincoln Grixti on 03/05/2014.
//  Copyright (c) 2014 Lincoln Grixti. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

static const string filename = "/Users/prophet/Dropbox/Development/Google Code Jam 2014/Round1B 2014/B-small-attempt0.in";


int evalPossibilities(unsigned int A, unsigned int B, unsigned int K)
{
    int result = 0;
    for( unsigned int tempA = 0; tempA < A; tempA++)
    {
        for( unsigned int tempB = 0; tempB < B; tempB++)
        {
            if ( (tempA&tempB) < K ){
                result++;
            }
        }
    }
    return result;

}
int main(int argc, const char * argv[])
{
    string line;
    ifstream ifs(filename);
    int cases = 0, caseNumber = 0;
    int options[3];
    int i = 0;
    if (ifs.is_open())
    {
        getline(ifs,line);
        stringstream myStream(line);
        myStream >> cases;
        while ( getline (ifs,line) )
        {
            ++caseNumber;
            i = 0;
            stringstream myStream(line);
            while (myStream.good() && i < 3){
                myStream >> options[i];
                ++i;
            }
            cout << "Case #" << caseNumber << ": " << evalPossibilities(options[0],options[1],options[2]) << endl;
        }
        ifs.close();
    }
    return 0;
}

