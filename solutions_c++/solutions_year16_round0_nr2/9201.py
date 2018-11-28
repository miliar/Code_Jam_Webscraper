#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int no_of_cases, t, i, times;
    int num, remainder, answer,temp_num;
    string string;
    int * digit = new int [100];
    int * temp_digit = new int [100];
    
    int k ,j;
    int finish = 0;
    
    int size; 
    int temp_size;
	int flip_begin, flip_end;
	
	cin >> no_of_cases;
    
    
	for (t = 1; t <= no_of_cases; t++) {
		
        cin >> string ;
        size = string.size();
        
        answer = 0;
        //+ = 1
    	//- = 0
    	for (i = 0; i < size; i++)
    		if (string[i]=='+')
				digit[i] = 1;
			else digit[i] = 0;
			
		for (i = 0; i < size; i++)

		temp_size = size;
				
		while (temp_size > 0) {

		if (temp_size ==1){
			if (digit[0]==0) { //'-'
			answer ++;
			}
			temp_size--;
			
		}
		
		else { // size > 1 

		
		while  ((temp_size >= 1) & (digit[temp_size-1] == 1) 
		
		) {  //find '-'
			temp_size --;					
		}
		
		if (temp_size!=0) //not all are + 
		{ 

		if (digit[0]==0) //need to flip '-'
		{
		
			if (temp_size>1) { 
			
					
					for (j = temp_size-1; j >= 0 ; j--){
						
					if ((digit[temp_size-1-j]) == 0 ) {
						temp_digit[j] = 1 ;
					}
						
					else {
					temp_digit[j]  = 0 ;
					}
					
				}
				for (j = 0; j < temp_size ; j++) {
					digit[j] = temp_digit[j];
					
				}
					
				answer ++;	
			}
			else {
			 digit[0] = 1;
			 answer++;
			 }
			 
			 
 		}
 		
 		else {// flip all beginning '+' first 
 			k = 0;
 			
 			while ((k < temp_size) & (digit[k] == 1))
 			k++;
 			for (j = 0; j < k ; j++){
 				digit[j]=0;
			 }
			 
			 answer ++; 	

		 }
		 
		 } 
		 
        
        } // size > 1
        
        } 


        cout << "Case #" << t << ": " << answer << endl;

    }
    
    return 0;
}

