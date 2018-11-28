/*
 * g11.cpp
 *
 *  Created on: ??þ/??þ/????
 *      Author: Toshiba
 */
# include <algorithm>
# include <iostream>
# include <stdio.h>
# include <stdlib.h>
# include <vector>
# include <string.h>
using namespace std;
int main(){
    int test ;
    scanf("%i",&test);
    for (int i = 0 ; i < test ; i++ ){
     	int in1 , l1 , l2 ;vector <int> temp ;
     	vector <int> line1; vector <int> line2;

     	scanf("%i",&l1);
     	  for (int y = 0 ; y < 4 ; y++){
     	  for (int z = 0 ; z < 4 ; z++) {
     		 scanf("%i",&in1);
     		 temp.push_back(in1);
     		 if(y+1==l1){
               line1.push_back(in1);
     		 }  } }

     	  scanf("%i",&l2);
     		 for (int y = 0 ; y < 4 ; y++){
         	  for (int z = 0 ; z < 4 ; z++) {
     		     	 scanf("%i",&in1);
     		         temp.push_back(in1);
     		         if(y+1==l2){
     		         line2.push_back(in1);
     		         }  } }

     		int count = 0;
     		int n = -1 ;
     		for (int j = 0 ;  j < 4 ; j++ ){
     		int f = find (line2.begin() , line2.end() , line1[j]) - line2.begin()  ;
     		if (f < 4 ){
     		count++ ;
     		n=f ; }
     		 }

     		 if (count == 1)
               printf ("Case #%i: %i\n",i+1,line2[n]);
     		 if (count >1 && count < 5)
     			 printf ("Case #%i: %s\n",i+1,"bad magician!");
     		 if (count == 0)
     			 printf ("Case #%i: %s\n",i+1,"Volunteer cheated!");
    }
	return 0;
}


