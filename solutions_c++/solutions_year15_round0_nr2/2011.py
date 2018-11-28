#include <fstream>
#include <iostream>
#include <string>
#include <vector> 
#include <list>
#include <sstream>
#include <iterator>
#include <map> 
#include <iomanip>
#include <utility> 
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include <limits>
#include <queue>

using namespace std;


void printV(vector<int> myV){
	for(int i=0; i<myV.size(); i++){
		cout<<myV[i];
	}
	cout<<endl;
}

int decide(vector<int> myV){
	int MAX=0;
	int idx=0;
	for (int i=0; i<myV.size(); i++){
		int tmp = myV[i];
		if (tmp>MAX){
			MAX=tmp;
			idx=i;
		}		
	}
	return MAX;	
}

int NumSplit(int val, int guess){	
	return (val+(guess-1))/guess -1;
}


int main(){
	int test;
	cin >>test;		
	
	for (int i=0; i<test; i++){
		
		int numDiner;		
		vector<int> myV;
		cin >>numDiner;	

		for (int i=0; i<numDiner; i++){
			int tmp;
			cin>>tmp;
			myV.push_back(tmp);
		}		

		int myMax = decide(myV);		
		int min = 0;
		
		min = myMax;
		
		for (int guess=1; guess<myMax; guess++){			
			int cur_total = 0;
			for (int i=0; i<myV.size(); i++){
				cur_total += NumSplit(myV[i], guess);				
			}
			cur_total += guess;

			if (cur_total<min) min = cur_total;

		}
		
		cout<<"Case #"<<i+1<<": "<<min<<endl;

	}
}



