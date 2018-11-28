//
//  main.cpp
//  Google_jam
//
//  Created by Nader on 07/03/2016.
//  Copyright (c) 2016 Nader. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

int main(int argc, const char * argv[]) {
    
    //Problem A
    std::ofstream myAnswer;
    myAnswer.open ("A-small-test.out");
    
    
    std::fstream myfile("A-small-test.in", std::ios_base::in);
    int t_cases;
    int N;
    int count;
 
    int sum_digits = 0;
    int last_digit = 0;
    float t1;
    
    myfile >> t1;
    int digits[10];
    t_cases = (int) t1;
    std::cout << "Cases = " << t_cases << std::endl;
    int max_N = 8;  //expontial of 10^6
    int M  = 1;
    int mod_val = 10;
    int digit_temp;
    int i = 1; //N multiplier
    int flag = 0;
    int MAXITER = 1000000;
    for(int j  =1; j <= t_cases; j++){
        //
        
        myfile >> N;
        
        
        //Clean digit array
        for(int kk=0; kk < 10; kk++){
            digits[kk] = 0;
        }
        std::cout << "N = "<< N << std::endl;
        i = 1;
        
        flag  =0;
        sum_digits = 0;
        last_digit = 0;
        
        while ( M < 1000001 && flag == 0 && i < MAXITER){
            ////                    //Check digits
            mod_val = 1;
            M = i*N;
            
            for(int k = 1; k < max_N; k++){
                
                digit_temp = ((M /(mod_val)))% 10;
                digits[digit_temp] = 1;
                
                mod_val *= 10;
                if(mod_val > M){
                    
                    break;
                }
                
                
            }
            
            
            i = i+1;
            sum_digits = 0;
            for(int k = 0; k< 10; k++){
                sum_digits += digits[k];
            }
            
            if( sum_digits == 10){
                flag = 1;
                
            }
            last_digit = M;
            
            
            
        }
        
        
        if(flag == 0){
            myAnswer << "Case #"<< j<< ": INSOMNIA" << std::endl;
            std::cout << "Case #"<< j<< ": INSOMNIA" << std::endl;
        }else{
            myAnswer << "Case #"<< j<< ": " << last_digit << std::endl;
            std::cout << "Case #"<< j<< ": " << last_digit << std::endl;
        }
        
        
    }

    
    myfile.close();
    myAnswer.close();
    return 0;
}

