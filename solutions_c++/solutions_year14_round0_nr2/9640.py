//
//  main.cpp
//  LFS
//
//  Created by Moko on 2/23/14.
//  Copyright (c) 2014 Moko Tech. All rights reserved.
//



#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

//ifstream fin;
//    fin.open("/Development/OS Assigment/1_13030020_13030022/A-small-attempt3.in");
//    fin >> totalCases;
//   // cout << totalCases;
//    ofstream fout;
//    fout.open("/Development/OS Assigment/1_13030020_13030022/outfile.txt");

//fout <<"Case #"<<caseNumber<<": ";
//if (commanCount == 1) {
//    fout << matrix1[input1][commonCol];
//}else if (commanCount == 0)
//{
//    fout << "Volunteer cheated!";
//}else
//{
//    fout << "Bad magician!";
//}
//fout << endl;

float timeForNewRate(float C, float F, float X, float farmCount)
{
    float totalTime = C / 2;
    
    totalTime = 0;
    for (int i = 0; i < farmCount; i++) {
        totalTime += C / (F*i + 2);
    }
    totalTime += X/(F*farmCount + 2);
  //  cout << totalTime << endl << endl;
    return totalTime;
}

int main(int argc, const char * argv[])
{
    int totalCases;
    ifstream fin;
    fin.open("/Development/OS Assigment/1_13030020_13030022/B-small-attempt1.in");
    fin >> totalCases;
    
    double C,F,X;
    
    ofstream fout,fout1;
    fout.open("/Development/OS Assigment/1_13030020_13030022/outfile.txt");
    fout1.open("/Development/OS Assigment/1_13030020_13030022/outfile1.txt");

    for (int caseNumber = 1; caseNumber <= totalCases; caseNumber++) {

    //cout << endl << endl << currentFarmtTime;
    fin >>std::setprecision(10)>> std::dec>> C >> F >> X;
        fout1 << C << " " << F << " "<< X <<"\n" ;
    float current = timeForNewRate(C, F, X, 0);
    float next = timeForNewRate(C, F, X, 1);
    int i = 1;
    while(current > next)
    {
        current = next;
        next = timeForNewRate(C, F, X,++i);
    }
        
        
        fout <<"Case #"<<caseNumber<<": "<<std::setprecision(10)<<current<<"\n";
        cout <<"Case #"<<caseNumber<<": "<<std::setprecision(10)<<current<<"\n";
    }
    
    
    

    
    return 0;
}




