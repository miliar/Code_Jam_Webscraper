#include <iostream>
#include <fstream>

using namespace std;

int main(){
	
	int N;
	
	int x;
	int needed=0;
	int standing=0;
	ifstream fin("ok.in");
	ofstream fout("output.txt");
	
	fin >> N;
	
	int size;
	int n=1;
	
	while(N>0){
		N--;
		needed=0;
		standing=0;
	
	fin>> size;

	size++;
	

	int array[size];
	
	fin >> x;
	
	for(int i=0; i<size; i++){
		array[size-i-1]= x%10;
		x=x/10;
	}
	
/*	for(int i=0; i<size; i++){
		cout << array[i];
	}
	cout << endl;
*/	
	
//110011
	standing = array[0];
	
	for(int i=1; i<size; i++){
	//cout << i << " " << standing;
		if(array[i]!=0){
		
		if(standing<i){ // if friends required
			x = i - standing;
			needed += x;
			standing += needed;
			standing += array[i];
		}
		else{
			standing += array[i];	
		}
	}
	
//	cout << " " << needed << endl;
	
	
	}
	
	fout << "Case #" << n++<<": " << needed << endl;
}
	
	
	
	
}
