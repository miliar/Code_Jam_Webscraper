//
//  main.cpp
//  GoogleCodeJam2014CookieClickerAlpha
//
//  Created by Duong Alexandre on 12/04/2014.
//  Copyright (c) 2014 Duong Alexandre. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[])
{

    ifstream aInputFile("B-large.in.txt");
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
            double C,F,X = 0;
            double aResult = 0;
            
            // Getting C, F and X
            aInputFile >> C;
            aInputFile >> F;
            aInputFile >> X;
            cout<< "C= " << C << "  F= "<< F << "  X= "<< X <<endl;
            
            // Calculating the total amount of time needed to produce X cookie without farms
            double aPreviousTotalTime = X/2;
            
            // Calculating the total amount of time needed to produce X cookie with 1 farm
            int aNbOfFarms = 1;
            double aTotalTime = C/2 + X/((F*aNbOfFarms)+2);
            double aPreviousTimeToXWithFarms = X/((F*aNbOfFarms)+2);
            cout << "aPreviousTotalTime: "<<aPreviousTotalTime << " aTotalTime: "<<aTotalTime<<endl;
            if(aPreviousTotalTime > aTotalTime)
            {
                // While buying farms allow reducing the total of seconds keep calculating
                while(aPreviousTotalTime > aTotalTime)
                {
                    aPreviousTotalTime = aTotalTime;
                    aTotalTime = aPreviousTotalTime
                                + C/((F*aNbOfFarms)+2) + X/((F*(aNbOfFarms+1.0))+2)
                                - aPreviousTimeToXWithFarms;
                    aPreviousTimeToXWithFarms = X/((F*(aNbOfFarms+1))+2);
                    cout.precision(15);
                    cout << "aPreviousTotalTime:"<<aPreviousTotalTime << " aTotalTime: "<<aTotalTime<<endl;
                    aNbOfFarms ++;
                }
                aResult = aPreviousTotalTime;
            } else
            {
                aResult = aPreviousTotalTime;
            }
            
            aOutputFile.precision(9);
            
            // printing output
            aOutputFile<< "Case #"<< aIterator<< ": " << aResult << endl;
            cout<< "\n\n\n" << endl;
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

