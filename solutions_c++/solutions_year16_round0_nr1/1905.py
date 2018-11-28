#include <iostream>
#include <sstream>
#include <cstdio>
#include <set>
using namespace std;

long long sheep( int input ){
	long long temp;
	int i;
	set<int> foo;

	for(i = 1; i<1000000; i++){
		temp = input * i;
		
		string result;
		ostringstream convert;
		convert << temp;
		result = convert.str();
		for( int i=0; i<result.size(); i++ ){
			foo.insert(result[i]);
		}
		if( foo.size() == 10 ) break;

	}
	if( foo.size() != 10 ) return -1;
	else return temp;
}


int main(){
	int cases, number;
	cin >> cases;
	for( int i=0; i<cases; i++ ){
		cin >> number;
		long long result = sheep(number);
		if( result == -1 ){
			printf("Case #%i: INSOMNIA\n", i+1);
		}
		else printf("Case #%i: %i\n", i+1, result);
	}
	
	return 0;	
}
