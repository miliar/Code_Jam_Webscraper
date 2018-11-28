/* 
 * File:   main.cpp
 * Author: gokul
 *
 * Created on 7 April, 2016, 11:06 PM
 */

#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,num = 1;
    cin>>t;
    
    while(t--){
        char input[1010];
        cin>>input;
        int ans = 0;
        char cur = '-';
        for(int i=0;input[i]!='\0';i++){
            if(i==0){
                if(input[i] == '-'){
                    cur = '-';
                }else{
                    cur = '+';
                }
            }else{
                if(cur != input[i]){
                    ans++;
                    cur = input[i];
                }
                
            }
        }
        
            if(cur == '-'){
                ans++;
            }
        
        
        
        
        
        cout<<"Case #"<<num++<<": "<<ans;
        
        cout<<endl;
    }
    return 0;
}