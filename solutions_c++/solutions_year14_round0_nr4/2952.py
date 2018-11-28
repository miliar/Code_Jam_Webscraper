#include <cstdlib>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cassert>

using namespace std;

bool _max(double a, double b){
     return a>b;     
}
bool _min(double a, double b){
     return a<b;     
}
int main(int argc, char *argv[])
{
    //ifstream fcin("C:\\Users\\zdb\\Downloads\\B-large.in");
    ifstream fcin("C:\\Users\\zdb\\Downloads\\D-large.in");
    //ifstream fcin("file.txt");
    ofstream fcout("ans3.txt");
    int T; fcin >> T;
    for(int i = 1; i <= T; i++){
         double A[1001], B[1001];
         bool exist[1001];
         int N; fcin >> N;
         for(int j = 0; j < N; j++){
                 fcin >> A[j];
         }
         for(int j = 0; j < N; j++){
                 fcin >> B[j];
                 exist[j] = true;
         }
         sort(A,A+N,_min);
         sort(B,B+N,_min);
         int X = 0;
         int Y = 0; 
         for(int j = 0; j < N; j++){
                 for(int k = 0; k < N; k++){
                         if(exist[k]){
                                      if(A[j]>B[k]) {
                                                    X++;
                                                    exist[k] = false;
                                      }
                                      else{
                                           for(int t = N-1; t>=0; t--)
                                           if(exist[t]){ exist[t]=false;
                                           break;}
                                      }
                                      break;
                         }
                 }        
         }
         //sort(B,B+N,_min);
         
         for(int j = 0; j < N; j++) exist[j] = true; 
         for(int j = 0; j < N; j++){
                 bool win = true;
                 for(int k = 0; k < N; k++){
                         if(exist[k] && B[k]>A[j]){
                              exist[k] = false;  
                              win = false;
                              break;                 
                         }       
                 }
                 if(win){
                 Y++;
                 
                      for(int k = 0; k < N; k++){
                              if(exist[k]){
                                           exist[k] = false;
                                           break;
                              }
                      }
                 }        
         }
         assert(X>=Y);
         fcout << "Case #" << i << ": ";   
         fcout << X << " " << Y << endl; 
    }    
    system("PAUSE");
    return EXIT_SUCCESS;
}
