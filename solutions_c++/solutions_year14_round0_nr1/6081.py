/* 
 * File:   main.cpp
 * Author: perfectmak
 *
 * Created on April 12, 2014, 2:16 AM
 */

#include <iostream>
#include <fstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) 
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    
    int t, ansA, ansB;
    int cA[4][4], cB[4][4];
    
    in >> t;
    
    for (int i = 0; i < t; i++) 
    {
        int counter = 0;
        int result = -1;
        in >> ansA;
        
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                in >> cA[j][k];
            }
        }
        
        in >> ansB;
        
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                in >> cB[j][k];
            }
        }
        
        //solving the problem
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                if(cA[ansA-1][j] == cB[ansB-1][k])
                {
                    counter++;
                    result = cA[ansA-1][j];
                }
            }
        }
        
        if(counter == 1)
        {
            out << "Case #" <<i+1 << ": " << result << endl;
        }
        else if(counter == 0)
        {
            out << "Case #" <<i+1 << ": Volunteer cheated!" << endl;
        }
        else
        {
            out << "Case #" <<i+1 << ": Bad magician!" << endl;
        }
    }
    
    in.close();
    out.close();
    
    return 0;
}

