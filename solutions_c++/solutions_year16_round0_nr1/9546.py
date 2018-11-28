/* 
 * File:   main.cpp
 * Author: doganay
 *
 * Created on 09 Nisan 2016 Cumartesi, 08:37
 */

#include <cstdlib>

#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <math.h>
#include <cmath>
#include <sstream>
#include <string>
#include <string.h>


using namespace std;


std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, elems);
    return elems;
}
/*
 * 
 */
int main(int argc, char** argv) {
       string line="";
   
   ifstream infile;
   infile.open ("/home/doganay/Masaüstü/practise.in");
   freopen("/home/doganay/Masaüstü/output.txt","w,",stdout);
   int caseCnt=0;
   getline(infile,line);
   int count = 1,num=0;
   int counter = 0,caseT = 1;
   int tempNum = 0;
   string ln="";
   istringstream(line)>>caseCnt;
   string words [] ={"1","2","3","4","5","6","7","8","9","0"};
   int opposites [] = {0,0,0,0,0,0,0,0,0,0};
   string writeTotxt ="INSOMNIA";
   int valsay = 0;
   for(int j=0;j<caseCnt;j++){
        
       getline(infile,line);
       vector<string> sayi;

       istringstream(line)>>num;
       
       while(true){
             tempNum = num*count;
             
             stringstream ss;
             ss << tempNum;
             line = ss.str();
             
           for(int i=0;i<line.size();i++){
                sayi.insert(sayi.end(),line.substr(i,1));  
           } 
            
           for(int i=0;i<sayi.size();i++){
             
               int length = sizeof(words)/sizeof(words[0]);
               for(int k=0;k<length;k++){
                   
                   if(sayi[i]==words[k] && opposites[k]==0){
                       valsay++;
                       opposites[k]=1;
                       break;
                   }
                   //else if(sayi[i]==words[k] && opposites[k]==1) break;
                  
                  
               }
                if(valsay==10)break;
               
           }
           sayi.clear();
           if(count>=1000000)break; 
            if(valsay==10) break;
         
            count++;
            
           
       }
      // cout<<"Count Number :"<<countNumber<<endl;
       fill(opposites,opposites+10,0);
       if(count>=1000000 && valsay!=10)
       cout<<"Case #"<<caseT<<": "<<"INSOMNIA"<<endl;
       else 
        cout<<"Case #"<<caseT<<": "<<count*num<<endl;
       count =1;
       valsay=0;
       caseT++;   
    }
   infile.close();

    return 0;
}

