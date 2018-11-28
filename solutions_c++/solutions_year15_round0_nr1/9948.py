#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main(int argc, char* argv[])
{
	ifstream input("A-small-attempt2.in");
	//ifstream input("test.data");
    	ofstream output("output.out");

    
	int cases;
	
	input >> cases;
	
	

	for(int i=1;i<=cases;i++){

		int Smax;
		int Ssum = 0;
		int answer = 0;

		input >> Smax;

		output << "Case #"<<i<<": ";
		
		int num;
		int S[Smax+1];	
	
		input >> num;

		for(int cs=Smax;cs>=0;cs--){
			S[cs] = num % 10;
			num = num / 10;
		}

		for(int k=0;k<=Smax;k++){
			if(S[k] == 0 && Ssum <= k){
				answer++;
				Ssum++;
			}
			Ssum += S[k];
		}
		
		output << answer;
		output << endl;
	}

	input.close();
	output.close();


	return 0;
}

