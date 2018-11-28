//
//  main.cpp
//  FairSquare
//
//  Created by Akanksha Verma on 4/13/13.
//  Copyright (c) 2013 Akanksha Verma. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{

    ifstream input;
    int numbers=0;
    input.open("Numbers.txt");
    int range[2];
   
    int CaseCount=0;
    
    
    while(!input.eof()){
        if(numbers == 0)
            input>>numbers;
        
        for(int i=0;i<2;i++){
            input>>range[i];
            //cout<<range[i]<<" ";
        }
        
        int howmany=0;
        
        
        
        int r=0;
        double square = range[0];
        double num = sqrt(square);
        
        while(square<=range[1]){
        
           
            bool isPalindromic = false;
            bool isAlsoPalindromic =false;
            
            
            int sq = num;
            int an = square;
            
            string Palindrome_Checker = to_string(an);
            string base = to_string(sq);

//if both the number and its square are single digit numbers
            if(base.length() == 1 && Palindrome_Checker.length() == 1 && (sq*sq == an)){
                isAlsoPalindromic=isPalindromic = true;
            }
//if only the number is single digits
            if(base.length() == 1 && Palindrome_Checker.length()>1 && (sq*sq == an)){
               
                int p = static_cast<int>(Palindrome_Checker.length()-1);
                for(int k=0;k<Palindrome_Checker.length()-1;k++){
                    if (Palindrome_Checker[k]== Palindrome_Checker[p]) {
                        isPalindromic = true;
                    }
                }
            }
            
//if both number and its square are more than 1 digit
            
            if(base.length()>1 && Palindrome_Checker.length()>1 && (sq*sq == an)){
            int p = static_cast<int>(Palindrome_Checker.length()-1);
            for(int k=0;k<Palindrome_Checker.length()-1;k++,p--){
                if (Palindrome_Checker[k]== Palindrome_Checker[p]) {
                    isPalindromic = true;
                }
                else{
                    isPalindromic=false;
                    break;
                }
            }
            
            int q = static_cast<int>(base.length()-1);
            for(int k=0;k<base.length()-1;k++,q--){
                if (base[k]== base[q]) {
                    isAlsoPalindromic = true;
                }
                else{
                    isPalindromic=false;
                    break;
                }
            
            }
      }
            
            if(isPalindromic && isAlsoPalindromic ){
                howmany++;
             //cout<<"\n"<<square<<"-->"<<num<<endl;
            }
            
            square++;
            num = sqrt(square);
            
        }
        
        if(CaseCount<numbers){
        cout<<"Case #"<<CaseCount+1<<": "<<howmany<<endl;
        CaseCount++;
        
        }
        
        
        
    }
}

