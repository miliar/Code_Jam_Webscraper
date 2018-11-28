#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int isPalin(int num) {
    int len=1, div=10, left, right;
    while(num/div) {
        len++; div*=10;
    }
    left=(int)pow((double)10, (double)(len-1)); right=10;
    while(left >= right) {
        if(num/left == num%right) {
            left=left/10; right=right*10;
        }
        else
            return 0;
    }
    return 1;
}

int main() {
	ifstream inFile;
	inFile.open("C-small-attempt0.in");
	int c=1, T, lower, upper, curr, csqrt, count;
	inFile >> T;
	while(T--) {
		inFile >> lower >> upper;
        count=0;
        for(curr=lower;curr<=upper;curr++) {
            if(isPalin(curr)){
                if(sqrt(curr) - floor(sqrt(curr))< 0.0001){
                    csqrt = (int)sqrt(curr);
                    if(isPalin(csqrt))
                        count++;
                }
            }
        }
		cout<<"Case #"<<c<<": "<<count<<endl; c++;
	}
	inFile.close();
	return 0;
}

