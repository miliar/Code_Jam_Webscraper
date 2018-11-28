//
//  main.cpp
//  Google codejam 2014 qualification round cookie
//
//  Created by David Yang on 4/12/14.
//  Copyright (c) 2014 David Yang. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;


ifstream fin("B-large.in");
ofstream fout("B-large.out");



void Calculator(long double FarmPrice, long double FarmSpeed, long double FinalGoal){
    
    
    long double CurrentTime = 0;
    
    long double CurrentSpeed = 2;
    
    while (true){
    
        if (FinalGoal/CurrentSpeed <=  (FarmPrice/CurrentSpeed + FinalGoal/(CurrentSpeed + FarmSpeed)) ){
            //std::cout << std::fixed << "num = " << std::setprecision(2) << num << std::endl;

            fout << fixed << setprecision(7) << CurrentTime + FinalGoal/CurrentSpeed << endl;
            return;
            
        }
        
        else{
            
            CurrentTime = CurrentTime + FarmPrice/CurrentSpeed;
            CurrentSpeed = CurrentSpeed + FarmSpeed;
            
            
            
            
        }
        
    }
    
    
    
    
    
    
    
}



int main(int argc, const char * argv[])
{
    
    int TestCases;
    long double FarmPrice;
    long double FarmSpeed;
    long double FinalGoal;
    
    
    
    fin >> TestCases;
    
    
    
    
    for (int i=0; i<TestCases; i++){
        
    
        fin >> FarmPrice;
        fin >> FarmSpeed;
        fin >> FinalGoal;
        
        fout << "Case #" << i+1 << ": ";
        
        Calculator(FarmPrice, FarmSpeed, FinalGoal);
    
    
        
        
        
        
        
        
    }
    
    
    return 0;
}

