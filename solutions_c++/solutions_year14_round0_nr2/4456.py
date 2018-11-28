#include <iostream>
#include <vector>
#include <cstdio>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>


using namespace std;



//  Google codejam small -  B



int main() {

	int t ;
	cin >> t;

	for ( int    l = 0; l < t; l ++ ){

		double c,f,x  ;
		cin >> c >> f>>  x;
		double sec = x /  2 ;
        double cnt = 0 ;
        double cok = 2 ;
        int tt = 0 ;
     while (1 ){
    	 cnt +=  c / cok  ;
    	 cok += f ;
    	 if (cnt + ((double)x /(double) cok) < (double)sec)
    		 sec = cnt + ((double)x /(double) cok) ;
    	 else
    		 break ;
     }

 	cout << "Case #"<<l + 1 << ": " ;
 	printf("%.7f\n", sec);
	}

	return 0;
}
