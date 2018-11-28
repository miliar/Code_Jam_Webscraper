//
//  test.cpp
//  
//
//  Created by Jonathan Beltran on 4/8/16.
//
//

#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <fstream>
#include <functional>
#include <climits>
#include <vector>
#include <queue>
#include <list>
#include <algorithm>
#include <bitset>         // std::bitset


using namespace std;

typedef vector<int> vi;

int main(){
    
    int t;
    cin >> t;
     
    for(int i = 0; i < t; i++){
        int x, j;
        long z;
        j = 1;
  
        cin >> x;
   
        
        if(x == 0){
            cout << "CASE #" << i + 1<< ": INSOMNIA" << endl;
            continue;
        }
        
        bitset<10> check;
        while(!check.all()){
            
            z = x * j;
            //cout << "Z: " << z << endl;
            int k = 1;
            long p = 0;
            while(p != z){
                check.set((z%(k*10))/k);
                p = (z%(k*10))/k;
                //cout << "P " << p << endl;
                p = (z%(k*10));
                k = k * 10;
            }
            j++;
        }
        cout << "CASE #" << i + 1<< ": " << z << endl;
        
    }
    
    

}