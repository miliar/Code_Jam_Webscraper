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

int Table(int first, int second){
	if (abs(first)==1) return (first>0)? second:-second;
	else if (abs(second)==1) return (second>0)? first:-first;
	
	// else if (first == second) return (first==1)? 1:-1;
	
	else if (abs(first) == abs(second)){
		if (abs(first)==1) return (first==1)? second:-second;
		else if (first*second >0) return -1;		
		else return 1;
	}
	
	else if (abs(first) == 2 && abs(second) == 3 ) {
		return (first*second>0)? 4:-4;
	}
	else if (abs(first) == 2 && abs(second) == 4 ) {
		return (first*second>0)? -3:3;
	}
	else if (abs(first) == 3 && abs(second) == 2 ) {
		return (first*second>0)? -4:4;
	}
	else if (abs(first) == 3 && abs(second) == 4 ) {
		return (first*second>0)? 2:-2;
	}
	else if (abs(first) == 4 && abs(second) == 2 ) {
		return (first*second>0)? 3:-3;
	}
	else if (abs(first) == 4 && abs(second) == 3 ) {
		return (first*second>0)? -2:2;
	}
	return 2000;
}
int char2int(char mychar){
	switch(mychar){
		case 'i':
			return 2;
		case 'j':
			return 3;
		case 'k':
			return 4;
		default:
			return 1000;
	}
	
}
void printV(vector<char> myV){
	for(int i=0; i<myV.size(); i++){
		cout<<myV[i];
	}
	cout<<endl;
}
void printV(vector<int> myV){
	for(int i=0; i<myV.size(); i++){
		cout<<myV[i]<<" ";
	}
	cout<<endl;
}
int multiply(vector<int> resultV){
	int val=1;
	for(int i=0; i<resultV.size(); i++){
		val=val*resultV[i];
	}
	return val;
}
 bool homogeneous(vector<char> myV){
 	char mychar=myV[0];
 	for (int i = 1; i<myV.size(); i++){
 		if (mychar!=myV[i]) return false;
 	}
 	return true;
 }

 int allYouCanEat(int start, int end, vector<char> myV){
 	int result = 1;
	for (int i =start; i<end; i++){
		result = Table( result, char2int(myV[i]) );			
	}
	return result;
 }

int main(){
	int test;
	cin >>test;		
	// cout<<"Num of test: "<<test<<endl;
	
	for (int i=0; i<test; i++){
		int num_letter, num_repeat;
		string myS, tmpS;
		vector<char> myV; vector<char> tmpV;
		cin>>num_letter>>num_repeat;
		// cout<<num_letter<<" "<<num_repeat<<endl;
		
		for (int j=0; j<num_letter; j++){
			char tmp;cin>>tmp;
			myV.push_back(tmp);
		}
		tmpV=myV;		
		for(int j =1; j<num_repeat; j++){			
			myV.insert(myV.end(), tmpV.begin(), tmpV.end());
		}		
		// printV(myV);
		/*
		Below is about finding the index
		*/
		int result=1;
		for (int k=2; k<myV.size()&&result!=-1; k++){
			result=1;
			int valAfterK = allYouCanEat(k,myV.size(),myV);
			// cout<<"K: "<<k<<" valAfterK: "<<valAfterK<<endl;
			if (valAfterK==4){
				int val2K = allYouCanEat(0,k,myV);				
				result = Table(val2K, valAfterK);					
				// cout<<"val2K: "<<val2K<<" valAfterK: "<<valAfterK<<endl;
				// cout<<"result: "<<result<<endl;
			}
		}
		string decision = (result==-1 && !homogeneous(myV))? "YES":"NO";
		// cout<<"result: "<<result<<endl;
		cout<<"Case #"<<i+1<<": "<<decision<<endl;

	}

}


// int result = 1;
// 		for (int i =0; i<myV.size(); i++){
// 			result = Table( result, char2int(myV[i]) );			
// 		}
// 		string decision = (result==-1 && !homogeneous(myV))? "YES":"NO";
// 		// cout<<"result: "<<result<<endl;
// 		cout<<"Case #"<<i+1<<": "<<decision<<endl;


// int result=1;
// 		int idx1=0;
// 		vector <int> resultV;
// 		while (abs(result)!=2 && idx1<myV.size()){			
// 			result = Table( result, char2int(myV[idx1]) );
// 			idx1++;			
// 			cout<<"result: "<<result<<" idx: "<<idx1-1<<" ";
// 		}
// 		resultV.push_back(result);result=1;
// 		cout<<endl;

// 		while (abs(result)!=3 && idx1<myV.size()){			
// 			result = Table( result, char2int(myV[idx1]) );
// 			idx1++;			
// 			cout<<"result: "<<result<<" idx: "<<idx1-1<<" ";
// 		}
// 		resultV.push_back(result);result=1;
// 		cout<<endl;
// 		while (idx1<myV.size()){			
// 			result = Table( result, char2int(myV[idx1]) );
// 			idx1++;			
// 			cout<<"result: "<<result<<" idx: "<<idx1-1<<" ";
// 		}
// 		resultV.push_back(result);
// 		cout<<endl;
// 		cout<<"resultV: "; printV(resultV);




// int result=1;
// 		int idx1=0;
// 		int allMUL=1;
// 		vector <int> resultV, i_idxV, j_idxV, k_idxV;
// 		vector<int> i_valV, j_valV, k_valV;
// 		for(int i=0; i<myV.size()&&allMUL!=24;i++){
// 			result = Table( result, char2int(myV[i]) );
// 			int tmpResultI = result;
// 			if (abs(result)==2){
// 				// cout<<"Fit i: "<<i<<endl;
// 				resultV.push_back(result);
// 				result = 1;
// 				for(int j=i+1; j<myV.size()&&allMUL!=24; j++){
// 					result = Table( result, char2int(myV[j]) );
// 					int tmpResultJ = result;
// 					if (abs(result)==3){
// 						// cout<<"Fit j: "<<j<<endl;
// 						resultV.push_back(result);
// 						result = 1;
// 						int k = j+1;
// 						while(k<myV.size()){
// 							result = Table( result, char2int(myV[k]) );
// 							k++;
// 						}
// 						allMUL = multiply(resultV)*result;						
// 						// cout<<"curV: "; printV(resultV);
// 						// cout<<"Done Loop: "	<<result<<endl;
// 						if (allMUL!=24) {allMUL=1;result=1;}
// 						// Do something for resultV?
// 						resultV.pop_back();
// 					}
// 					result = tmpResultJ;
					
// 				}	
// 				// Do something for resultV?
// 				resultV.pop_back();
// 			}
// 			result = tmpResultI;
			
// 		}

// 		string decision = (allMUL==24)? "YES":"NO";
// 		cout<<"Case #"<<i+1<<": "<<decision<<endl;




// int result=1;
// 		for(int i = 0; i<myV.size(); i++){
// 			result = Table( result, char2int(myV[i]) );
// 			cout<<"not_idx: "<<i<<" result: "<<result<<endl;
// 			if (abs(result)==2){
// 				cout<<"idx: "<<i<<" result: "<<result<<endl;
// 			}
// 		}