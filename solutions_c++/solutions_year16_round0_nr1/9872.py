//
//  main.cpp
//  GoogleJamSheep
//
//  Created by Will Suhrbur on 4/9/16.
//  Copyright (c) 2016 Will Suhrbur. All rights reserved.
//

#include <iostream>
using namespace std;
#include <fstream>
#include <vector>



bool checkArr (int [] );

int main()
{
    ifstream myInput;
    ofstream myOutput;
    char inputFileName [] = "/Users/WillSuhrbur/Desktop/GoogleJamProjects/GoogleJam/GoogleJamSheep/GoogleJamSheep/A-large.in.txt";
    char outputFileName [] = "/Users/WillSuhrbur/Desktop/GoogleJamProjects/GoogleJam/GoogleJamSheep/GoogleJamSheep/A-largeoutput.txt";
    
    myInput.open(inputFileName, ios::in );
    myOutput.open(outputFileName, ios::out );
    
    int N = 0;
    myInput >> N;
    
    for ( int j = 1; j <= N; j++ )
    {
        
        int dope;
        myInput >> dope;
        
        
        
        if ( dope == 0 )
        {
            cout << "Case #" << j << ": " << "INSOMNIA" << endl;
            
        } // end if
        else
        {
            const int arraySize = 10;
            int array[ arraySize ] = { 0 };
            int maximumValue = 0;
            int counter = 1;
            vector< int > digits;
            
            while ( checkArr ( array ) == false )
            {
                int N = dope * counter;
                int temp = N;
                
                
                while (N)
                {
                    
                    
                    digits.push_back(N % 10);
                    N /= 10;
                } // end while
                
                for ( unsigned i = 0; i < digits.size(); i++ )
                {
                    
                    int current = digits[ i ];
                    array[ current ]++;
                } // end inner for
                
                maximumValue = temp;
                counter++;
            } // end while
            cout << "Case #" << j << ": " << maximumValue << endl;
            
        } // end else
        
        
        
    } // end outer for
    
    
    
    
    return 0;
}


bool checkArr ( int dis[] )
{
    for ( int i = 0; i < 10; i++ )
    {
        if ( dis[ i ] == 0 )
            return false;
    } // end for
    return true;
} // end function checkArr