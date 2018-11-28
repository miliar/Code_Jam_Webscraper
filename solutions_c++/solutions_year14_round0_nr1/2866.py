/* 
 * File:   main.cpp
 * Author: Parnami
 * Created on April 12, 2014, 4:43 AM
 * Description : Google Code Jam 2014 Qualification Round. Question 1
 */

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    int t,i,lineNumber,j,arr[4][4],arr2[17],count,answer,l;
    string fileName = "in.txt";
    ifstream input_data("A-small-attempt0.in");
    ofstream outputFile("out.txt");
    //input_data.open;
    input_data>>t;
    for(l=0;l<t;l++)
    {
        count = 0;
        for(i=0;i<17;i++)
        {
            arr2[i]=0;
        }
        input_data>>lineNumber;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                input_data>>arr[i][j];
            }
        }
        for(i=0;i<4;i++)
        {
            arr2[arr[lineNumber-1][i]]++;
        }
        input_data>>lineNumber;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                input_data>>arr[i][j];
            }
        }
        for(i=0;i<4;i++)
        {
            arr2[arr[lineNumber-1][i]]++;
        }
        for(i=1;i<17;i++)
        {
            if(arr2[i]==2)
            {
                count++;
                answer=i;
            }
        }
        outputFile<<"Case #"<<l+1<<": ";
        if(count==0)
            outputFile<<"Volunteer cheated!"<<endl;
        else if(count==1)
            outputFile<<answer<<endl;
        else
            outputFile<<"Bad magician!"<<endl;
    }
    return 0;
}

