#include <iostream>
#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include <vector>
 
using namespace std;

// this function flips in the reversed order all of its elements
void flip_range (vector<char> & v) {
	vector<char> x;
	x.clear();
	
	for (vector<char>::reverse_iterator it=v.rbegin(); it!= v.rend(); it++) { //reverse the order
		x.push_back(((*it=='+')? '-':'+'));	// reverse the sign	
	}
		
	v.swap(x);
	
}
// this fuction negates the beginning pancake range with + sign (to - sign)
void negate_range(vector<char> & v) {		
	
	for (vector<char>::iterator it = v.begin(); it!= v.end(); it++) {
		
		if ( *it == '-' ) { 
			break; 
		} else {
			*it = '-';
		}
	}		
}

int main (void) {
	
	int T;
	int col = 102;
	char aux[col]; // maximum 100 letters + the \0 + \n
	
	FILE * p1;
	
	// ############ INPUT FILE
	p1 = fopen ("B-large.in","r");
	char ** buffer;	
	if (p1!=NULL) { 		
		// get the lines T
		fgets ( aux, col, p1 );
		T = atoi (aux);		
		
		//write all content of the input file to the buffer
		buffer = (char **) malloc( T * sizeof (char *));		
		for (int t = 0; t <T; t++) {
			buffer[t]=(char*)malloc(col*sizeof(char));
			fgets ( buffer[t], col, p1 );						
		}			
		
		fclose (p1);// close p1
	}			
	
	// ################### OUTPUT FILE
	p1 = fopen ("file.out","w");	
	vector<char>v;
	if (p1!=NULL) { 	
			
		for (int t = 0; t < T; t++) { // choose the test case
			
			// copy test case to vector v	
			int i=0;
			v.clear();
			int op=0;
			do {
				v.push_back(buffer[t][i++]);										
			} while (buffer[t][i]!='\n' && buffer[t][i]!='\0');			
			
			do {  
				
				if (*v.rbegin()=='+') { 					
					v.pop_back(); //remove bottom + pancake (do not count as op)
					
				} else if (*v.begin()=='+') {					
					negate_range(v); 
					op++;	
							
				} else if (*v.begin()=='-') {					
					flip_range (v);
					op++;
					
				}
				
				
			} while(!v.empty()); 
			
			fprintf(p1,"Case #%i: %i\n",t+1,op);			
		}
		
		fclose (p1);// close p1
	}
	
	free(buffer);
	
	return 0;
	
}
