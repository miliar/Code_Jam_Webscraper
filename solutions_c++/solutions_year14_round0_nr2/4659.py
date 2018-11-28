//
//  main.cpp
//  cookieClicker
//
//  Created by Si Te Feng on 2014-04-11.
//  Copyright (c) 2014 Si Te Feng. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>

using namespace std;

void inputArray(int rowValues[], ifstream& infile);

int main(int argc, const char * argv[])
{
    
    ifstream file("B-small-attempt0.in", ios::in);
    
    ofstream fout("time.txt");
    
    if(file.is_open())
    {
        
        string Tstring;
        file >> Tstring;
        int T = stoi(Tstring, NULL, 10);
        
        fout << setprecision(15);
        
        for(int w=0; w<T; w++)
        {
            double c,f,x;
            
            string cs,fs,xs;
            
            file >> cs;
            c = stod(cs);
            
            file >> fs;
            f = stod(fs);
            
            file >> xs;
            x = stod(xs);
            
            double T1 = x/2;
            double Tnext = c/2 + x/(2+f);
            
            int n=1;
            
            while (Tnext < T1)
            {
                T1 = Tnext;
                n++;
                
                Tnext = c/2;
                
                for(int i=1; i<=n; i++)
                {
                    if(i==n)
                    {
                        Tnext += x/(2+i*f);
                    }
                    else
                    {
                        Tnext += c/(2+i*f);
                    }
                }
            }
            
            fout<< "Case #" << (w+1) << ": " ;
            fout << T1 << endl;
        }
    }
   


    cin.get();
 
    return 0;
    
}
