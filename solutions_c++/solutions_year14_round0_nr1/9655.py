// 1111.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>
using namespace std;

string getValue(string s1, string s2){
     string s;
     int array[17] = {0,};
     int l1 = s1.length();
     int l2 = s2.length();
     int tmp = 0;
     int result = 0;
     int count = 0;
	// cout<<s1<<" and "<<s2<<endl;

     for (int i = 0; i < l1; i++){
         if (s1[i] != ' '){
              tmp = s1[i] - 48 + tmp*10;     

		 }
		 if(i == l1 - 1){
			  array[tmp] = 1;

			  tmp = 0;
		 }
		 if(s1[i] == ' '){
              array[tmp] = 1; 

              tmp = 0;
         }
     }
     for (int i = 0; i < l2; i++){
         if (s2[i] != ' '){
              tmp = s2[i] - 48 + tmp*10;     
		 } 
		if (i == l2 -1){
			if(array[tmp] == 1){
				   count++; 

                    result = tmp;
                            
               }
              tmp = 0;
		 }
		if (s2[i] == ' '){
               if(array[tmp] == 1){
				   count++; 
                    result = tmp;         
               }
              tmp = 0;
         }
     }
     if (count == 0){
		//cout<<"cheat"<<endl;
        return "Volunteer cheated!";
     }
     if (count == 1){
        stringstream ss;
        ss << result;
		//cout<<ss.str()<<endl;
        return ss.str();
     }

		 //cout<<"bad"<<endl;
     return "Bad magician!";

}

int main()
{
    std::ifstream infile("A-small-attempt1.in");
    std::string line;
    string num;
    std::getline(infile, num);
    //cout<<num<<endl;
    int nums = atoi(num.c_str());
    ofstream outfile;
    outfile.open("output.txt");
    int counter = 0;
    int i = 0;
    int row1 = 0;
    int row2 = 0;
    string s1;
    string s2;
    while (std::getline(infile, line)){
          
          if (i == 10){
             i = 0;
             counter ++;
		     string output = getValue(s1, s2);
             cout<<"Case #"<<counter<<": "<<output<<endl;
			 outfile<<"Case #"<<counter<<": "<<output<<endl;
          }
          if (i < 10){
                if (i == 0){
                    row1 = line[0] - 48;  
                }else if (i == 5){
                    row2 = line[0] - 48 + 5; 
                }else if (i == row1){
                      s1 = line;      
                }else if (i == row2){
                      s2 = line;     
                }
                i++;
          }
    }
   if (i == 10){
          counter ++;
		  string output = getValue(s1, s2);
          cout<<"Case #"<<counter<<": "<<output<<endl;
		  outfile<<"Case #"<<counter<<": "<<output<<endl;
    }
    
    system("pause");
   // return 0;
}


