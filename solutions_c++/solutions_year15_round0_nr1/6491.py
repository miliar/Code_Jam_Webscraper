#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int totalUp (string a, int index){
	
	int sum = 0;
	
	for (int i = 0; i<index-1; i++){
		int ab = a[i] - '0';
		sum += ab;
	}
	return sum;	
}

int zero(string a, int size){
	
	int count = 0;
		
	for (int i=1; i<size; i++){
			
		if ( i > totalUp(a,i+1)){
		
			while (i != totalUp(a,i+1)){
				
				int ab = a[i-1] - '0' + 1;
				a[i-1] = ab + '0';
				count++;
			
			}
		}
	}
		
	return count;
	
}

int main(){

	ifstream file("test.in");
	ofstream outfile("test.out");

	int iterations;
	int smax;

	file >> iterations;
	
	for (int i = 0 ; i < iterations; i++){
		
		file >> smax;
		string a;
		
		file >> a;
			
		outfile << "Case #" << i+1 << ": " << zero(a,smax+1) << endl ;
		
	}
}
