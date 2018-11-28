#include <iostream>
#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
 
using namespace std;

int main (void) {
	
	int T;
	int col = 9;
	char aux[col]; // maximum 8 letters + the \0 + \n, note: 10^6=1000000
	
	FILE * p1;
	
	// ############ INPUT FILE
	p1 = fopen ("A-large.in","r");
	char ** buffer;	
	if (p1!=NULL) { 		
		// get the lines T
		fgets ( aux, col, p1 );
		T = atoi (aux);	
		
		cout <<"T"<<T<<endl;
		
		//write all content of the input file to the buffer
		buffer = (char **) malloc( T * sizeof (char *));		
		for (int t = 0; t <T; t++) {
			buffer[t]=(char*)malloc(col*sizeof(char));
			fgets ( buffer[t], col, p1 );						
		}	
		
		for (int t = 0; t <T; t++) cout << "t="<<t<<"  string="<<buffer[t];
		fclose (p1);// close p1
	}			
	
	// ################### OUTPUT FILE
	p1 = fopen ("file.out","w");
	
	long long int N;
	char num[sizeof (long long int)];
	int c[10]= {0,0,0,0,0,0,0,0,0,0};
	
	if (p1!=NULL) { 	
			
		for (int t = 0; t <T; t++) { // choose the test case
			
			N = atoi(buffer[t]);
			
			for (int i=0;i<10;i++) 
				c[i]=0;
			
			if (N!=0) { // NOT INSOMNIA
						
				for (long long int i=1; 1;i++) { // iterate the number:  N, 2N, 3N, 
					 sprintf (num, "%lld",i*N);
					
					 for (long long int d=0;1;d++) { //... and count the digits
						if (num[d] == '\n' || num[d] == '\0' ||	(c[0]&&c[1]&&c[2]&&c[3]&&c[4]&&c[5]&&c[6]&&c[7]&&c[8]&&c[9])) {
							break;
						} else {
							sprintf(aux, "%c",num[d]);
							c[atoi(aux)]=1;
						}					
							
					 }
					 
					 if (c[0]&&c[1]&&c[2]&&c[3]&&c[4]&&c[5]&&c[6]&&c[7]&&c[8]&&c[9]) {
						// write the sleeping number  
						fprintf(p1,"Case #%i: %s\n",t+1,num);
						break;
					 } 
						
					
				}
			} else { // INSOMNIA
				fprintf(p1,"Case #%i: INSOMNIA\n",t+1);
			}
		}	
		
		fclose (p1);// close p1
	}
		
	
	return 0;
	
}
