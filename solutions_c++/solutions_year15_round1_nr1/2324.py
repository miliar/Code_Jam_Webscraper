#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <iomanip>
using namespace std;

int N, *mushrooms;

long int method1(){
	long int output = 0;
	for(int i =1; i < N; i++){
		if( mushrooms[i] < mushrooms[i-1]){ output+= (mushrooms[i-1]-mushrooms[i]);}}
	return output;
}

long int method2(int k){ 
	cout << k << endl;
	if(N == 1){return 0;}
	else{
		long int answer = 0;
		for(int i = 0; i < N-1; i++){
			//if( mushrooms[i] > mushrooms[i-1] ){
						if(mushrooms[i] <= k){ 
								answer+= mushrooms[i];}
						else{answer+= k;}
			//..else{ answer += mushrooms[i]-k;}
		}
		return answer;
	}
}

int main() {
	int tcases;
	ifstream in("test");
	ofstream out("myanswer");
	in >> tcases;
	for(int i =1; i <= tcases;i++){
	    out<< "Case #" << i << ": ";
	    in >> N;
	    mushrooms = new int[N];
	    int k=0;
	    if(N >= 2){
	    	in>>mushrooms[0]; in>>mushrooms[1];
	    	int temp = mushrooms[1]-mushrooms[0];
	    	if(temp < k){ k = temp;}
	    	for(int i = 2;i < N; i++){ in>>mushrooms[i];
	    				temp = mushrooms[i]-mushrooms[i-1];
	    				if(temp < k){k = temp;}  }}
	    out << method1() << " " << method2(-1*k) << endl;
	  
	}
	return 0;
}

/*out << fixed;
	    out << setprecision(6); */
