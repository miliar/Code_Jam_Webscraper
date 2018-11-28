#include <string>
#include <fstream>
#include <iostream>


unsigned int solve(unsigned max, std::string aud){
	unsigned int active = 0;
	unsigned int needed = 0;
	//std::cout << aud << "->";
	for(unsigned i = 0; i<aud.length(); i++){
		unsigned int t = aud[i] - 48;
		//std::cout << t;
		if(active < i and i != 0){
			needed ++;
			active ++;
		}
		active += t;
	}
	//std::cout << "\n";
	return needed;
}



int main (int argn, char** args){
	std::string in = args[1];
	std::string out = args[2];

	std::fstream input(in, std::ios_base::in);
	std::fstream output(out, std::ios_base::out);
	
	unsigned int cases;
	input >> cases;
	for(unsigned i=0; i<cases; i++){
		unsigned int max;
		std::string aud;
		input >> max >> aud;
		
		
		
		output << "Case #" << (i+1) << ": " << solve(max, aud) << "\n";
	}


	return 0;
}