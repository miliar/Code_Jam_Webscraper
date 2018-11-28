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

int Method1 (vector<int> myV){
	int sum=0;
	for (int i=1; i<myV.size(); i++){
		if (myV[i]<myV[i-1]){
			sum += myV[i-1] - myV[i];
		}
	}
	return sum;
}

int Method2 (vector<int> myV){
	int sum = 0;
	int rate = INT_MAX;
	int size = myV.size();
	
	for (int i=1; i<myV.size(); i++){
		int diff = myV[i] - myV[i-1];		
		if (diff< rate && diff<0) rate = diff;
	}
	if (rate == INT_MAX) rate=0;
	else rate = abs(rate);

	for (int i=0; i<myV.size()-1; i++){
		// cout<<"curV:"<<myV[i]<<endl;
		if (myV[i] >= rate) sum += rate;
		else sum += myV[i];
	}

	return sum;
}


int main(){
	int numCase;
	cin >>numCase;		
	
	for (int i=0; i<numCase; i++){
		
		int numDiner;		
		vector<int> myV;
		int Num;
		cin >>Num;	

		for (int i=0; i<Num; i++){
			int tmp;
			cin>>tmp;
			myV.push_back(tmp);
		}		

		// cout << Method1(myV)<<endl;
		// cout << "rate: " << Method2(myV)<<endl;
		
		cout<<"Case #"<<i+1<<": "<<Method1(myV)<<" "<<Method2(myV)<<endl;

	}
}



