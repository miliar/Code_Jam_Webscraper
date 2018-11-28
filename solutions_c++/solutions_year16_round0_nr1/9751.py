#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;


int main() {
	int N; 
    cin >> N; 
    int number;
    for(int i = 0; i < N; i++){
	      cin >> number;
	      if(number == 0){
	        printf ("Case #%d: INSOMNIA\n",i+1);
	      //	cout << "Case #%d<<"INSOMNIA"<< endl; 
	      }else{
	         bool myArray[10] = {false}; 
	      	 int count = 0; 
	         bool allAppear = false; 
	         int multiple = number; 
	      while(!allAppear){
	      	count++; 
	      	multiple = number*count; 
	      int copy = multiple;  
	      while(copy > 0 && !allAppear){
	         int p = fmod(copy, 10); 
	         myArray[p]=true; 
	         copy = copy/10; 
             if(myArray[0] && myArray[1]&&myArray[2] && myArray[3]&&myArray[4] && myArray[5]&&myArray[6] && myArray[7]&&myArray[8] && myArray[9]){
                 allAppear = true; 
             }
           }//while copy > 9 and not allAppear
	      }//while not all appear
	        printf ("Case #%d: %d\n",i+1, multiple);
	     // cout << multiple << endl; 
	  }//else 
    }//for
    return 0;
}

