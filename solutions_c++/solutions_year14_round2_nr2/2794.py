#include <iostream>
#include<stdio.h>
#include <algorithm>
#include <stdlib.h> 
#include <bitset>

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
#define MAX 100100
using namespace std;


int main(){
    
    int c;
    cin >> c;
 
    long long int a, b, k, ab;
    for(int _c =1; _c<=c; _c++){
     cin >> a >> b >> k;
     
    long long int cont  = 0;
    for(int i = 0; i<= a; i++ ){
            for(int j =0; j<= b; j++){
                     ab = i&j;
                    
                if(i<a && j<b && ab < k){
                    cont++;   
                }
                
                    
            }
    
    }
     
     
     
     cout << "Case #"<<_c<<": "<< cont << endl;
        
         
    } 
    
return 0;    
}
