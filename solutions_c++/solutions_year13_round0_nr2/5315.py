//
//  main.cpp
//  googlecodequalifying1
//
//  Created by Melody Pang on 13/04/2013.
//  Copyright (c) 2013 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[])
{
    
    ifstream infile("/Users/mellypang/Developer/googlecode/googlecodequalifying2/googlecodequalifying2/input.txt");
    
    if (!infile) {
        cout << "There was a problem opening file "
        << " for reading."
        << endl;
        return 0;
    }
    int nTests;
    int helper;
    infile >> nTests;
    ofstream myfile;
    myfile.open ("/Users/mellypang/Developer/googlecode/googlecodequalifying2/googlecodequalifying2/output.txt");
    for (int k = 0; k < nTests; ++k) 
    {
        int nrows = 0;
        int ncols = 0;
    
        infile >> nrows;
        infile >> ncols;
    
        //read in data
        vector<vector<int> > input;
        vector<int> heights;
        for (int i = 0; i < nrows; ++i)
        {
            input.push_back(vector<int>());
            for (int j = 0; j < ncols; ++j)
            {
                infile >> helper;
                input[i].push_back(helper);
                heights.push_back(helper);            
            }
        }
        
        // we have all the data - uniquify and sort
        sort( heights.begin(), heights.end() );
        heights.erase( unique( heights.begin(), heights.end() ), heights.end() );
        
        // go through each height and check if all its nearest neighbours are greater than it then it fails
        bool canBeCut = true;
        for (int i = 0; i < heights.size(); ++i)
        {
            for (int m = 0; m < nrows; ++m)
            {
                for (int n = 0; n < ncols; ++n)
                {
                    if (input[m][n] == heights[i])
                    {
                        vector<int> col;
                        for (int r = 0; r < nrows; ++r)
                        {
                            col.push_back(input[r][n]);
                        }
                        vector<int> row = input[m];
                        int max_row = *(max_element(row.begin(),row.end()));
                        int max_col = *(max_element(col.begin(),col.end()));
                        if ( max_row > heights[i] && max_col > heights[i])
                            canBeCut = false;
                    }
                }
            }            
        }
        string result = canBeCut ? "YES" : "NO";
        cout << result << endl;
        myfile << "Case #" << k+1 << ": " << result << endl;
             
    }
}

