//
//  main.cpp
//  GoogleCodeJam2014MagicTrick
//
//  Created by Duong Alexandre on 12/04/2014.
//  Copyright (c) 2014 Duong Alexandre. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[])
{

    ifstream aInputFile("A-small-attempt3.in");
    ofstream aOutputFile("output.txt");
    
    if(aInputFile.is_open())
    {
        // Getting the number of cases
        int aNbOfCase = 0;
        aInputFile>> aNbOfCase;
        int aIterator=1;
        // Looping throught all the cases
        while(aIterator != (aNbOfCase+1))
        {
            // Re-initializing the variables in each iteration
            int aResponse1 = 0;
            int aResponse2 = 0;
            int aArrangement1 [5][5];
            int aArrangement2 [5][5];
            
            // Getting the first response
            aInputFile>> aResponse1;
            
            // Getting the first arrangement
            for(int i=1; i<=4; i++)
            {
                for(int j=1; j<=4; j++)
                {
                    aInputFile >> aArrangement1[i][j];
                }
            }
            
            // Getting the second response
            aInputFile>> aResponse2;
            
            // Getting the second arrangement
            for(int i=1; i<=4; i++)
            {
                for(int j=1; j<=4; j++)
                {
                    aInputFile >> aArrangement2[i][j];
                }
            }
            
            // count the number of that are the same from arrangement1 in line response1
            // and arrangement2 in line response2
            int aCount = 0;
            int aGoodCardNb = 0;
        
            for(int j=1; j<=4; j++)
            {
                if((aArrangement2[aResponse2][j] == aArrangement1[aResponse1][1])
                   || (aArrangement2[aResponse2][j] == aArrangement1[aResponse1][2])
                   || (aArrangement2[aResponse2][j] == aArrangement1[aResponse1][3])
                   || (aArrangement2[aResponse2][j] == aArrangement1[aResponse1][4]))
                {
                    aCount ++;
                    aGoodCardNb = aArrangement2[aResponse2][j];
                }
            }
            
            // Printing the result
            if(aCount == 0)
            {
                aOutputFile<< "Case #"<< aIterator<< ": Volunteer cheated!" << endl;
            } else if(aCount == 1)
            {
                aOutputFile<< "Case #"<< aIterator<< ": "<< aGoodCardNb<< endl;
            } else
            {
                aOutputFile<< "Case #"<< aIterator<< ": Bad magician!"<<endl;
            }
            
            aIterator = aIterator + 1;
        }
    } else
    {
        cout<<"Couldn't read file"<<endl;
    }
    
    aInputFile.close();
    aOutputFile.close();
    
    return 0;
}

