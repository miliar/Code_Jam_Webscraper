/*
 * CountingSheep.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: ramshad
 */

#include "CountingSheep.h"
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <windows.h>

using namespace std;

string matched;




bool match(string Number){

	sort(Number.begin(), Number.end());
	Number.erase(unique(Number.begin(), Number.end()), Number.end());
    //cout << "Number: " << Number << endl;

	matched=matched + Number;

	//cout << "matched: " << matched << endl;

	sort(matched.begin(), matched.end());
	matched.erase(unique(matched.begin(), matched.end()), matched.end());
	//cout << "Unique: " << matched << endl;

	if(matched.length()==10){
		return true;
	}
	else{
        return false;
	}
}

void Counting() {
	// TODO Auto-generated constructor stub

	 string line;
	 fstream infile("C:\\Users\\ramshad\\workspace\\CodeJam2016\\CountingSheeps\\A-large.in");
	 fstream outfile;
	 stringstream ss;
 	 int T, N;
 	 string result;
 	 int tmp;

 	 outfile.open("C:\\Users\\ramshad\\workspace\\CodeJam2016\\CountingSheeps\\output.txt");
 	 //outfile << "Writing this to a file.\n";

 	 while (getline(infile, line)){
 		 cout << line << endl;
	     stringstream ss (line);
	     ss >> T;
	     cout << "Number of Test cases: " << T <<endl;
	     if (1<=T && T<=100){
	    	 for (int i=1; i<=T ; i++){
	    		 getline(infile, line);
	    	     stringstream ss (line);
	    	     ss >> N;
	    	     if (0<=N && N<= 10000000){
	    	    	 if(N==0){
	    	    		 result="INSOMNIA";
	    	    	 }
	    	    	 else {
	    	    		 //cout << "Searching  "<< "N: "<< N <<  endl;
	    	    		 //tmp=line;
	    	    		 int j=2;
	    	    		 matched="";

	    	    		 while(!match(line)){

	    	    			 tmp=N*j;
	    	    			 ss.str("");
	    	    			 ss.clear();
	    	    			 ss << tmp;
	    	    			 //cout << ss.str() << endl;
	    	    			 line=ss.str();
	    	    			 j++;
	    	    			 //cout << "Here I am  "<< "N: "<< N << " j: " << j << endl;
	    	    			 //Sleep(1000);
	    	    		 }
	    	    		 result=line;
	    	    	 }
	    	    	 cout << "Case #"<< i <<": "<< result << endl;
	    	    	 outfile << "Case #"<< i <<": "<< result << endl;
	    	     }
	    	 }
	     }
 	 }
 	 outfile.close();
 	 infile.close();

}


int main() {
	Counting();
	return 0;
}




