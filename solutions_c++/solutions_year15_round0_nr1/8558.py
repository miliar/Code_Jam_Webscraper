#include <stdio.h>
#include <string.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<string>
#include<cstdio>
#include<sstream>
#include<map>
#include<list>
#include<queue>
#include<set>
#include<numeric>
#include<functional>
#include <bitset>
using namespace std;


int main (){


   int  t , cnt = 0 ;     cin >> t ;
   while (t--){
	     int  s;
	     int x [1500]  ;
	     string temp   ;
	     cin >> s >> temp ;
	     for (int i = 0 ; i <  temp.size() ; i ++ )
	    	 x[i]  = temp[i] - '0';

	     for (int i = 1 ; i < temp.size();i ++)  x[i] += x[i-1] ;

	     int  counter = 0 ;

	     for (int i = 1 ;i < temp.size() ; i ++){
	    	 if ( i  > (x[i -1 ] + counter  ) )  counter += i - (x[i -1 ] + counter  ) ;
	     }

	   cout <<"Case #" <<++cnt<<": "<< counter << endl ;
   }


	return 0 ;
}
