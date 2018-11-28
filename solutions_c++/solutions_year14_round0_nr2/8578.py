//
//  main.cpp
//  Jam
//
//  Created by Beibin Li on 14-4-11.
//  Copyright (c) 2014年 Beibin. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <cstdlib>
#include<iomanip> //decimal precision


using namespace std;

double time(int x, double C, double F, double X)
// x is the # farm to buy
{
    double time = 0;
    for(int i=0; i<x; i++){
        time += C/(i*F + 2);
    }

    time += X/(x*F+2);

    return time;
}

void one_case(int caseNum)
{

    double C, F, X;
    cin >> C >> F >> X;

    double minTime = X/2;

    int numFarm = 0;

    for(int i=0; i>-1; i++){
        double newTime = time(i, C, F, X);
        if(minTime >= newTime){
            minTime = newTime;
            numFarm = i;
        }else{
            break;
        }
    }



    cout<< "Case #" << caseNum+1 <<": "<<minTime<<endl;

}


int main(int argc, const char * argv[])
{

    cout << std::setprecision(7); //Always show 2 decimal places
    cout << std::fixed; //Disable scientific notation for large numbers
    //these two lines should be quoted out. Used for Xcode
//    ifstream arq(getenv("try"));
//    cin.rdbuf(arq.rdbuf());

    int numCase = 0;
    cin >> numCase;
    
    for(int i=0; i<numCase; i++){
        one_case(i);
    }
    
    
    return 0;
}

