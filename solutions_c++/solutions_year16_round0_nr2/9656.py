/* 
 * File:   main.cpp
 * Author: doganay
 *
 * Created on 09 Nisan 2016 Cumartesi, 20:43
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
   int caseCnt=0,num=0;
   getline(infile,line);
   int caseT = 1;
   string ln="";
   int operationCounter = 0;
   istringstream(line)>>caseCnt;
   int similarity = 0;

   for(int j=0;j<caseCnt;j++){
        
       getline(infile,line);
       vector<string> sayi;

       istringstream(line)>>num;  
       
       for(int i=0;i<line.length();i++){
                sayi.insert(sayi.end(),line.substr(i,1));  
       }
       
       int i = sayi.size()-1;
       while(true){
           string SonVall ="";
           string firstVal ="";
           string similarityLast ="";
           
           bool con = false;
           if(sayi[i]=="-" && sayi[0]=="-"){
               con = true;
           }else if(i==1 && sayi[i]=="-" && sayi[0]=="+"){
               con = true;
               sayi.at(0)="-";
               operationCounter++;
           }else if(sayi[i]=="-" && sayi[0]=="+"){
               
               for(int m = 1;m<line.length();m++){
                   
                   if(sayi[0]==sayi[m]){
                       similarity++;
                   }
                   else{

                       i=similarity;
                       con=true;

                       similarityLast =sayi[m]; 
                       break;
                   }
                   
                 
               }
               
               
               
           }
           
           
           if(con){
               int c = 0;
               string convert[sayi.size()];
               for(int k=sayi.size()-1;k>=0;k--){
                   
                   string a = "-";
                   if(k<=i){
                        if(sayi[k]=="+")
                        {
                            convert[c]="-";
                            c++;
                        }
                        else{
                        convert[c]="+";
                        c++;
                        }
                   
                   }else{
                    
                       convert[k]=sayi[k];
                   }
                   
               }
               if(similarity>=1){
                 
                   similarity=0;
               }
               /*for(int k=0;k<sayi.size();k++){
                   cout<<"Convert :"<<convert[k]<<endl;
               }*/ 
               for(int k=0;k<sayi.size();k++){
                    
                   sayi.at(k)=convert[k];
               }
               
                 i=sayi.size();
               operationCounter++;
           }
           int plustCounter=0;
           for(int k=sayi.size()-1;k>=0;k--){
               
               if(sayi[k]=="+") plustCounter++;
            }
           
           if(plustCounter==sayi.size())break;
           i--;
           
       } 
       sayi.clear();
        cout<<"Case #"<<caseT<<": "<<operationCounter<<endl;
        operationCounter = 0;
       
        caseT++;  
    }
   infile.close();

    return 0;
}


