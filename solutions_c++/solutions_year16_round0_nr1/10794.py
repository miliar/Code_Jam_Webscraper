#include<bits/stdc++.h>
using namespace std;

bool debugEnabled = false;
int visited[10];

void debug (string str){
	if(debugEnabled){
		cout<<str<<endl;
	}
}

void resetVisitedArray(){
	visited[0] = visited[1] = visited[2] = visited[3] = visited[4] = visited[5] = visited[6] = visited[7] = visited[8] = visited[9] = 0;
}

bool visitedAll(){
	return (visited[0] * visited[1] * visited[2] * visited[3] * visited[4] * visited[5] * visited[6] * visited[7] * visited[8] * visited[9] );
}

void visitAllDigitsIn(long long int x){
    if(x >= 10)
       visitAllDigitsIn(x / 10);

    int digit = x % 10;

    visited[digit] = 1;
}

void printVisitedArray(){
	if(debugEnabled){
		cout<< visited[0] << visited[1] << visited[2] << visited[3] << visited[4] << visited[5] << visited[6] << visited[7] << visited[8] << visited[9] <<endl;		
	}
}

string toString(long long int i){
	stringstream sstm;
	sstm << i ;
	return sstm.str();
}

long long int getResult(long long int n){
			resetVisitedArray();

		if(n == 0){
			return 0;
		}
		int i = 1;
		visitAllDigitsIn(n*i);
		printVisitedArray();
		while ( ! visitedAll() ){
			debug("Still not visited all. n = " + toString(n*i) );
			i++;
			visitAllDigitsIn(n*i);
			printVisitedArray();

		}
		debug("Visited All, n = " + toString(n*i) );
		return n*i;
}

int main(){
	/*
	for (long long int i = 0; i < 1000000000; i++){
		cout<<"Fetching result for " + toString(i) << endl ;
		cout << toString(getResult(i)) << endl;
	}*/
	
	long long int t;
	cin>>t;
	for (long long int i = 0 ; i < t; i++){
		cout << "Case #" << i+1 << ": ";
		long long int n;
		cin>>n;
		long long int result = getResult(n);
		if(result == 0){
			cout << "INSOMNIA" << endl;
		} else {
			cout << result << endl;
		}
	}
	return 0;
}
