#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <sstream>

using namespace std;

#define ERROR 0.00000001

bool IsSquare(int x){
    double tmp1 = sqrt(x);
    int tmp2 = tmp1;
    if(abs(tmp2-tmp1) < ERROR)
	return true;
    else
	return false;
}

bool IsFair(int x){
    stringstream ss;
    ss << x;
    string str = ss.str();
    int len = str.length();
    for(int i = 0; i < len/2; i++){
	if(str[i]!=str[len-1-i])
	    return false;
    }
    return true;
}

int main(int argc, char **argv){
    string inputFileName(argv[1]);
    string outputFileName(argv[2]);

    ifstream input(inputFileName.c_str());
    ofstream output(outputFileName.c_str());

    int T;
    input >> T;

    int A,B;

    for(int t = 0; t < T; t++){
	/* Input*/
	input >> A;
	input >> B;
	//////////////////////////////////////////
	/*Process*/
	int C = sqrt(A);
	int D = sqrt(B);
	if(C*C<A)
	    C++;
	int counter = 0;
	for(int i = C; i <= D; i++){
	    if(IsFair(i) && IsFair(i*i)){
		cout << i*i <<endl;
		counter++;
	    }
	}
	
	/* Output*/
	output << "Case #" << t+1 <<": " << counter;

	output <<endl;
    }
    
    return 0;
}
