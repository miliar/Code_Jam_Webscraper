#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

bool isPalindrome(long long n);

int main(int argc, char** argv){
    ifstream fIn;
    ofstream fOut;
    
    int N;
    long long A;
    long long B;

    long long rMin;
    long long rMax;
    
    int fs;

    fIn.open("input.dat", ifstream::in);
    fOut.open("output.dat", ofstream::out);

    if(fIn.is_open() && fOut.is_open()){
	fIn >> N;

	for(int i=0; i<N; i++){
	    fIn >> A >> B;

	    rMin = ceil(sqrt(A));
	    rMax = floor(sqrt(B));
	    
	    fs = 0;
	    for(long long j=rMin; j<=rMax; j++){
		if(isPalindrome(j*j) && isPalindrome(j))fs++;
	    }
	      
	    fOut << "Case #" << i+1 << ": " << fs << "\n";	    
	}

	fIn.close();
	fOut.close();
    }
}


bool isPalindrome(long long n){
    stringstream converter;
    string str;
    
    converter << n;
    converter >> str;

    for(int i=0; i<str.size()/2; i++){
	if(str[i] != str[str.size()-1-i]){ 
	    return false;
	}    
    }

    return true;
}
