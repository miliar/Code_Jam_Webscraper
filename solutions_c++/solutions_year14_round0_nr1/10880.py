#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>     /* atoi */
#include <stdio.h>
#include <sstream>
using namespace std;

int main ()
{
    string STRING, testcases,gramiA,gramiB,stringtest;
    ifstream infile;
    infile.open ("A-small-attempt3.in");
    int a,b,c,d;
    int apadisis=0;
    int dipli=0;
    string apadisi="";
    string apadisi2="";


    string previousLine="";
    getline(infile,testcases); // Saves the line in STRING.
    int testcases2,STRING2;
    stringstream(testcases)>>testcases2;
    //cout<<" exoume :"<<testcases2<<" \n"<<endl;  
    for(a=0;a<testcases2;a++){
      getline(infile,STRING);
      for(b=0;b<4;b++){
        stringstream(STRING)>>STRING2;
        if(b==STRING2-1){
          getline(infile,gramiA);
          //cout<<" H proti sira ine i   "<<gramiA<<endl;
        }
        else{
          getline(infile,stringtest);
        }
      }
      getline(infile,STRING);
      for(b=0;b<4;b++){
        stringstream(STRING)>>STRING2;
        if(b==STRING2-1){
          getline(infile,gramiB);
          //cout<<" H defteri sira ine i "<<gramiB<<endl;
        }
        else{
          getline(infile,stringtest);
        }
      }



      for(c=0;c<gramiA.length();c++){
        //if (gramiA.at(c)!=" "){
        if (isdigit(gramiA[c])){

          if(isdigit(gramiA[c+1])){

            c=c+1;
            //cout<<" To noumero pou elegxo einai to : "<<gramiA.at(c-1)<<gramiA.at(c)<<endl;

            for(d=0;d<gramiB.length();d++){


              if(isdigit(gramiB[d])){
                if(isdigit(gramiB[d+1])){
                  if (gramiA[c-1]==gramiB[d] && gramiA[c]==gramiB[d+1]){
                    apadisi=gramiA[c-1];
                    apadisi2=gramiA[c];

                    dipli=1;

                    apadisis=apadisis+1;
                  }
                }
              }


            }



          }
          else{

            //cout<<" To noumero pou elegxo einai to : "<<gramiA.at(c)<<endl;
            

            for(d=0;d<gramiB.length();d++){
              if(isdigit(gramiB[d])){
                if  (isdigit(gramiB[d+1])==false) {
                  if(isdigit(gramiB[d-1])==false){

                    if (gramiA[c]==gramiB[d]){
                      apadisi=gramiA.at(c);
                      apadisis=apadisis+1;
                    }

                  }


                }
              }

            }            

          }
          //cout<<gramiA[c]<<endl;
        
          
        }
      }
      if (apadisi==""){
        cout<<"Case #"<<a+1<<": Volunteer cheated!"<<endl; 
      }
      else{
        if(apadisis==1){
          if (dipli==0){
            cout<<"Case #"<<a+1<<": "+apadisi<<endl;
          } 
          else{
            cout<<"Case #"<<a+1<<": "+apadisi<<apadisi2<<endl;
          } 
        }
        else{
          cout<<"Case #"<<a+1<<": Bad magician!"<<endl;
           
        }
      }
      apadisi="";
      apadisi2="";
      gramiA="";
      gramiB="";
      STRING="";
      apadisis=0;
      dipli=0;
    }
    /*
    while(a<1) // To get you all the lines.
    {
        getline(infile,STRING); // Saves the line in STRING.
        if (STRING != previousLine)
        {
            previousLine=STRING;
            cout<<STRING<<endl; // Prints our STRING.
        }

    }
    */
    infile.close();
}