//
//  main.cpp
//  war
//
//  Created by Si Te Feng on 2014-04-12.
//  Copyright (c) 2014 Si Te Feng. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>

using namespace std;

bool compare(double a, double b)
{
    return a < b;
}


int main(int argc, const char * argv[])
{
    
    ifstream file("D-large.in", ios::in);
    string temp;
    
    ofstream fout("output.txt");
    
    if(file.is_open())
    {
        string Tstring;
        file >> Tstring;
        
        cout<< setprecision(4);
        
        int T = stoi(Tstring);
        
        for(int w=1; w<=T; w++)
        {
            string Nstring;
            file >> Nstring;
            int N = stoi(Nstring);
            
            double naomi[1001];
            double ken[1001];
            
            for(int i=0; i<N; i++)
            {
                file >> temp;
                naomi[i] = stod(temp);
            }
            for(int i=0; i<N; i++)
            {
                file >> temp;
                ken[i] = stod(temp);
            }
            
            ////////////////////////////////
            sort(naomi, naomi + N);
            sort(ken, ken + N);
            //////////////////////////////////
            
            double tempKen[1001];
            copy(ken, ken + N, tempKen);
            
            int numWarGameLostNaomi =0;
            
            for(int i=0; i< N; i++)//for naomi
            {
                for(int j=0; j<N; j++)//for ken
                {
                    if(tempKen[j]> naomi[i])
                    {
                        numWarGameLostNaomi++;
                        tempKen[j] = 0;
                        break;
                    }
                }
            }
            
            
            double tempNaomi[1001];
            copy(naomi, naomi + N, tempNaomi);
            
            int numDeceitWarWonNaomi = 0;
            
            for(int i=N-1; i>=0; i--)//for ken
            {
                for(int j=N-1; j>=0; j--)//for naomi
                {
                    if(tempNaomi[j]>ken[i])
                    {
                        numDeceitWarWonNaomi++;
                        tempNaomi[j]=0;
                        break;
                    }
                    
                }
            }
            
            fout << "Case #"<< w << ": ";
            
            fout << numDeceitWarWonNaomi << " " << N - numWarGameLostNaomi << endl;
            
            
        }
        
    }

    return 0;
    
}






