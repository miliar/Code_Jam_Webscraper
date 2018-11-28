#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<vector>
#include<cmath>

using namespace std;


int main(int argc, char ** argv) {
    //read
    ifstream file(argv[1]);
//    ifstream file("input.txt");
    ofstream ofile("output.txt");
    int numT;
    file>>numT;

    for(int i=0; i<numT; i++) {
	long long r,t;
	file >> r >> t;

	long long n=1;

	while(2*n*n+(2*r-1)*n <= t) {
	    n++;
	}
	ofile<<"Case #"<<i+1<<": "<<n-1<<endl;
 
    }
    return 0;
}
