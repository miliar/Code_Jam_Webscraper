#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
using namespace std;

int main(){
 freopen("./b2.in.txt", "r", stdin);
 freopen("./b2.out.txt", "w", stdout);

    int N; 
    cin >> N;
   
 for(int i = 0; i < N; i++){
    string str; 
    cin >> str; 
    //process input 
    int len = str.length(); 
    string lastword = ""; 
    for(int i = 0; i < len; i++){
    	char temp = str.at(i); 
        if(lastword.length()>0){
            char frt = lastword[0]; 
            if(frt > temp){
            	//put to the back 
            	lastword += temp; 
            }else{
            	lastword = temp + lastword; 
            }
        }else{
        	lastword += temp; 
        }
    }

    //give output
    printf("Case #%d: ", i+1); 
    cout << lastword << endl; 
 }//for N 

}//main 
