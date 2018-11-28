#include<iostream>
#include<vector>
#include <algorithm>
#include <fstream>
#include <math.h>
#include <iomanip>      
using namespace std;
int main(){
    int T;
    long double C, F, X, current, sec, addition, temp;
    ifstream File;
    File.open("B-large.in");
    ofstream File2;
    File2.open("B-large.out");
    File>>T;
    for(int t = 1; t <= T; t++){
       File>>C>>F>>X;
       sec = 0.0;
       addition = 2.0; 
       while(true){
          if ( X/(addition+F) < (X-C)/addition ){
             sec += C/addition;
             addition += F;
          }
          else{
             sec += X/(addition);
             break;
          }
       }
       File2 <<"Case #"<<t<<": "<<std::fixed<<std::setprecision(7)<<sec<<endl;
    }
system("pause");
return 0;    
}
