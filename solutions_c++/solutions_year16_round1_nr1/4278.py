#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <math.h>
#include <limits.h>
#include <deque>

using namespace std;

int T; //test cases

int line_size = 1002;
typedef vector<string> vs;


vs read_file () {
    
    
    char aux[line_size];
    FILE * p1;      
    vs vaux;
    
    
    // ############ INPUT FILE
    p1 = fopen ("data.in","r");
    
    
    if (p1!=NULL) { 		
        
        T = atoi( fgets( aux, line_size, p1 ) ); // get T
        vaux.clear();
        // write all content of the input file to the vvi
        for (int t = 0; t <T; t++) {
                      
            vaux.push_back ( fgets( aux, line_size, p1 ) ); // get n
             
            }
        }	
        
        
       /* for (vs::iterator it=vaux.begin();it!=vaux.end();it++ ) {
                
           cout << *it<<endl;
        }
        */
        
        fclose (p1);// close p1
    
    
    return vaux;   
}

int main () {
	   
    vs v = read_file (); 
    
    deque<char> d; 
    
    
    for (int t = 0; t<T; t++) {
		cout << "Case #"<<t+1<<": ";
		
		int y=0;
		
		d.clear();
		
		d.push_back(v[t][y++]);
		
		
		while (v[t][y] != '\n' ) {
			 if ( v[t][y] < *d.begin() ) 
				d.push_back(v[t][y++]) ; 
			 else 
				d.push_front(v[t][y++]);				
			 
		} 
		
		
		for (  deque<char>::iterator it=d.begin(); it!=d.end(); it++ ) cout << *it;
		cout <<endl;
	}
    return 0;
}
