/* 
 * File:   main.cpp
 * Author: nitin
 *
 * Created on 13 November, 2012, 9:13 PM
 */

#include<iostream>
#include<vector>
#include<fstream>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main()
{
    int test,t,rows,columns,possible,one_check_count=0;
    string result;
    ifstream myfile ("example.txt");
    myfile>>t;
    test = t;
    while(t--)
    {
        one_check_count = 0;
        myfile>>rows>>columns;
        int garden[rows][columns];
        for(int i=0;i<rows;i++)
        {
            for(int j=0;j<columns;j++)
            {
                myfile>>garden[i][j];
            }
        }
        possible = 1;
        for(int i=0;i<rows&&possible;i++)
        {
            for(int j=0;j<columns&&possible;j++)
            {
                if(garden[i][j]==1)
                {
                    for(int jtemp=0;jtemp<columns;jtemp++)
                    {
                        if(garden[i][jtemp]!=1)
                        {
                            possible = 0;
                            break;
                        }
                    }
                    if(!possible)
                    {
                        possible=1;
                        for(int itemp = 0;itemp<rows;itemp++)
                        {
                            if(garden[itemp][j]!=1)
                            {
                                possible = 0;
                                break;
                            }
                        }
                    }
                }
            }
        }
        if(possible)
            result = "YES";
        else
            result = "NO";
        cout<<"Case #"<<test - t<<": "<<result<<"\n";
    }
}