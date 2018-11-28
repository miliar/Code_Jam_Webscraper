#include <iostream>
#include <fstream>
#include <string>

int main(){	
	int T, needed = 0;
	std::ifstream inputfile("input.txt");
	std::ofstream outputfile("output.txt");
	inputfile >> T;	
	int intinput[T], intoutput[T];
	std::string stringinput[T];
	for(int i=0; i<T; i++){
		inputfile >> intinput[i];
		inputfile >> stringinput[i];
	}	
	for(int i=0; i < T; i++){		
		int count = 0;
		needed=0;
		for(int j=0; j<intinput[i]+1; j++){			
			while(count<j){	
				needed++;
				count++;
			}	
			count = count + (stringinput[i].at(j) - '0');
		}
		intoutput[i]=needed;
	}
	for(int i=0;i<T;i++){
		outputfile << "Case #" << i+1 << ": " << intoutput[i] << std::endl;
	}
}