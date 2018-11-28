#include <iostream> 
#include <fstream>
#include <string>
#include <vector>
#include <algorithm> 
#include <iomanip>
#include <limits>
#include <utility>
#include <cmath>
#include <boost/algorithm/string.hpp>


int best_war(std::vector<double> &n, std::vector<double> &k) {
	if(n.front() < k.front()) { 
		// Naomi is going to lose this block but lets make it the least bad loss we can 
		if(n.size() == 1 ) { 
			//std::cout << "Naomi plays: " << n.front() << std::endl; 
			n.erase(n.begin());
			//std::cout << "Ken plays: " << k.front() << std::endl; 
			k.erase(k.begin());
			return 0; // no point is scored :-( 
		}
		int i; 
		for(i=0; i < n.size()-1; i++) { 
			if( n[i+1] < k[1] ) {
				break;
			}
		}
		//std::cout << "Naomi plays: " << *(n.begin()+i) << std::endl;  
		n.erase(n.begin()+i);
		//std::cout << "Ken plays: " << k.front() << std::endl;  
		k.erase(k.begin());
		return 0 ; // We set it up so we should be scoring a point later
	} else { 
		//std::cout << "Naomi plays: " <<n.front() << std::endl;  
		n.erase(n.begin());
		//std::cout << "Ken plays: " <<k.back() << std::endl;  
		k.pop_back();
		return 1; // We score a point
	}
	return 0; 
}

int deceptful_war(std::vector<double> &n, std::vector<double> &k) {
	// If I have any weight heavier then the lightest in kens desck I can win 
	std::vector<double> can_i ;
	std::copy_if(n.begin(),n.end(),std::back_inserter(can_i),[&](const double &a) { 
			return a > k.back();
	});
	if( ! can_i.empty() ) { 
		for(int i = n.size()-1; i >= 0 ; i--) { 
			if(n[i] > k.back()) { 				
				n.erase(n.begin()+i); 
				k.pop_back();
				return 1;
			}
		}
		// hmmmm
	} else { 
		// He is going to remove his heavest and I will remove my lightest
		n.pop_back();
		k.erase(k.begin());
		return 0 ;
	}
	return 0;	
}

int main(int argc, char **argv) { 
	std::shared_ptr<std::istream> in;
	std::ifstream infile; 
	if( argc > 1 ) { 
		in.reset(new std::ifstream(argv[1])); 
	} else { 
		in.reset(&(std::cin),[](...){});
	}
	int rounds,score,lieing; 
	std::string line;
	std::vector<std::string> placeholder;
	std::vector<double> naomi,ken; 
	std::getline(*in,line); 
	rounds = std::stoi(line); 
	//std::cout << "There will be " << rounds << " rounds " << std::endl;
	for(int i=0; i< rounds; i++) {
		score = 0;
		lieing = 0;
		naomi.clear();
		ken.clear();
		placeholder.clear();

		std::getline(*in,line); // this is the number of elements we drop this 
		//std::cout << "This round has " << line << " blocks " << std::endl; 
		// Get Naomi's line
		std::getline(*in,line); 
		boost::split(placeholder,line, boost::is_any_of(" "));
		std::transform(placeholder.begin(),placeholder.end(),std::back_inserter(naomi), [](const std::string& s) { return std::stod(s); } );

		// Get Kens line
		placeholder.clear();
		std::getline(*in,line); 
		boost::split(placeholder,line, boost::is_any_of(" "));
		std::transform(placeholder.begin(),placeholder.end(),std::back_inserter(ken), [](const std::string& s) { return std::stod(s); } );
		std::sort(naomi.begin(),naomi.end(),[](const double& a, const double& b) {return b < a; });
		std::sort(ken.begin(),ken.end(),[](const double& a, const double& b) {return b < a; });

		std::vector<double> n(naomi),k(ken);
		while( ! n.empty() ) {
			score += best_war(n,k);
		}

		std::vector<double> n1(naomi),k1(ken);
		while( ! n1.empty() ) {
			lieing += deceptful_war(n1,k1); 
		}
		// Normal War 
		// Play the block I have that is closest to Naomi's block without going over
		// If I have no block heavy enough play my lightest block 
		// Naomi Stragity. Play the lightest block I have that is heavier then his heaviest block 

		// If I have the heaviest block then play it. If not then 
		// Knowing his weights I want to play my lightest block and tell him it is heavier then all but his heaviest block 


		std::cout << "Case #" << i+1 << ": "  << lieing << " " << score << std::endl; 
	}

	//std::cout << "Leftover: \n" << in->rdbuf();

	return 0; 
}
