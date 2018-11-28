#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>


using namespace std;

int main(int argc, char* argv[])
{
	ifstream input("B-small-attempt0.in");
	//ifstream input("test.data");
    ofstream output("output.out");

    
	int cases;
	
	input >> cases;

	for(int i=1;i<=cases;i++){
		output << "Case #"<<i<<": ";
		int A,B,K;
		input >> A;
		input >> B;
		input >> K;
		int wincount = 0;
  		for(int j=0;j<A;j++){
  			for(int k=0;k<B;k++){
  				if((j&k)< K){
  					wincount += 1;
  				}
  			}
  		}
  		output << wincount << endl;
  	}
  	input.close();
  	output.close();
  	return 0;
}



