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

void printV(vector<int> V){
	for(int i=0; i<V.size(); i++){
		cout<<V[i];
	}
	cout<<endl;
}

int decide(string mystring, int S){
	int accuSum=0;
	int Need=0;

	for(int i=0; i<S+1; i++){
		// cout<<"i: "<< i <<" accuSum: "<<accuSum<<endl;
		if (i <= accuSum){
			int curVal= mystring[i]-'0';
			accuSum += curVal;			
			Need +=0;
		}		
		else{
			int curVal= mystring[i]-'0';			
			int curNeed = i - accuSum;			
			Need += curNeed;
			// cout<<"i:"<<i<<endl;
			// cout<<accuSum<<" "<<curNeed<<" "<<curVal<<endl;
			accuSum += curNeed + curVal;
			// cout<<"i: "<<i<<" curNeed: "<<curNeed<<endl;
			// cout<<"accuSum: "<<accuSum<<endl;
		}
	}
	return Need;
	// cout<<"Need: "<<Need<<endl;
}

int main(){
	int test;
	cin >>test;		
	
	for (int i=0; i<test; i++){
		int S;
		string mystring;
		vector<int> myV;
		cin >>S>>mystring;	
		cout<<"Case #"<<i+1<<": "<<decide(mystring, S)<<endl;
		
	}
}