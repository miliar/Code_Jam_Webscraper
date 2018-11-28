/* 
 * File:   fair.cpp
 * Author: Ragesh
 *
 * Created on April 13, 2013, 9:05 PM
 */

#include <iostream>

using namespace std;

/*
 * 
 */
int main() {

    int t,a,b,out,i,j;
    int test[5]={1,4,9,121,484};
    
    cin>>t;
    for(i=1;i<=t;i++){
        out=0;
        cin>>a>>b;
        
        for(j=0;j<5;j++){
            if(test[j]>=a && test[j]<=b){
                out++;
            }
        }
        
        cout<<"\nCase #"<<i<<": "<<out;
    }
    
    return 0;
}

