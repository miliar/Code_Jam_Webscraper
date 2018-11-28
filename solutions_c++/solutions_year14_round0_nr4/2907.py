#include <iostream>
#include<stdio.h>
#include <algorithm>
#include <stdlib.h> 

#include <math.h>
#include <string.h>
#include <utility>


#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <set>

#include<memory.h>

#include <sstream>
using namespace std;



bool ord(pair<double, bool> x, pair<double, bool> y ){
   
   return x.first > y.first;     
     
}
bool ord2(pair<double, bool> x, pair<double, bool> y ){
   
   return x.first < y.first;     
     
}



int main(){
    int T;
    cin >> T;
    
    for(int _T =1; _T <= T; _T++){
         int a,NG=0, NP=0;
        cin >> a;
         
         pair<double, bool> N[a+1],K[a+1], N2[a+1],k2[a+1];
         double x;
         //double N[a+1],K[a+1], N2[a+1],k2[a+1];
         
         for(int i =0; i<a; i++){
            cin >>x;
            N[i] = make_pair(x,true);
         }
            
        for(int i =0; i<a; i++){
            cin >>x;
            K[i] = make_pair(x,true);
         }
          
          //ordeno los 2
          sort(N, N+a, ord);
          sort(K, K+a, ord);
          
          
       /*
           for(int i =0; i<a; i++){
              pair<double, bool> s =N[i];      
            cout << s.first<< " ";
          }
          
          cout << endl;
          for(int i =0; i<a; i++){ 
            cout << K[i].first<< " ";
           
          }
          cout << endl;          
          
*/
          //Jugando sin trampas :P
          int j, i;
            for(i = 0; i<a; i++){
              for(j=0; j<a; j++)
                if(K[j].first> N[i].first && K[j].second ==true )
                    break;
              
                      
                      
               if(j != a){
                    K[j].second = false;
               } else if( j == a){
                      int z;
                      for(z = a-1; z>=0; z--)
                        if(K[z].second ==true){
                           K[z].second = false;
                           break;        
                        }
                        
                      if(z >= 0) NG++;
               }       
            }
            
              for(i = 0; i<a; i++)
                K[i].second =true;
            
            //Jugando con trampas :P
            
             sort(N, N+a, ord2);
            for(i = 0; i<a; i++){
              for(j=a-1; j>=0; j--)
                if(K[j].first < N[i].first && K[j].second ==true )
                    break;
              
                      
                      
               if(j >= 0){
                    K[j].second = false;
                    NP++;
               }
                
            }
            
            
            
            
              
              
              /*
              for(int i =0, j=a-1; i<a && j>=0; j--, i++ )
                if (N[j].first > K[i].first)
                  NP++;
              */
                   
        
          
          //cout << NP << " " << NG << endl;        
          printf("Case #%d: %d %d\n", _T, NP, NG);
    }
    
    
return 0;    
}
