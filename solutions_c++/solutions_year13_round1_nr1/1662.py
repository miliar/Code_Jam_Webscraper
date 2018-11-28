#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <math.h>
#define REP(i,n) for (int i=0; i<n; i++)
typedef long long ll;
using namespace std;

static const double PI = 6*asin( 0.5 );

int main(int argc, char *argv[]){
	int testcase=0;	//Nth test
	int X;	//testcase
	cout << "input file: " << argv[1] << endl;
	ifstream inputfile(argv[1]);
	ofstream outputfile("output.txt");
	
	inputfile >> X;
	
	REP(i,X){
		int count=0;
		testcase++;
		ll r, t, radius=0;
		ll sn=0;
		inputfile >> r;
		inputfile >> t;
		radius += r+1;
		
		while(t>=sn){
			sn = 2 * radius -1;
			if(t >= sn){
				t -= sn;
				count++;
			}
			radius += 2;
		}
	
		cout << "Case #" << testcase << ": " << count << endl;
		outputfile << "Case #" << testcase << ": " << count << endl;
	}
	
	
	return 0;
}