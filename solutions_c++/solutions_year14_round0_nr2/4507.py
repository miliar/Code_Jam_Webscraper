#include <iostream> 
#include <fstream>
#include <string>
#include <vector>
#include <algorithm> 
#include <iomanip>
#include <limits>

int main(int argc, char **argv) { 
	std::shared_ptr<std::istream> in;
	std::ifstream infile; 
	if( argc > 1 ) { 
		in.reset(new std::ifstream(argv[1])); 
	} else { 
		in.reset(&(std::cin),[](...){});
	}
	double cps = 0.0, default_cps = 2.0, goal = 0.0; 
	double total = 0.0, best_total;
	double factory_cost = 0.0, factory_speedup = 0.0; 
	unsigned long factories; 
	unsigned long target_factories = 0 ; 
	int rounds; 
	*in >> rounds; 	
	//std::cout << "There will be " << rounds << " rounds " << std::endl;
	for(int i = 0; i < rounds; i++) { 
		*in >> factory_cost >> factory_speedup >> goal; 
		//std::cout << "Cost: " << factory_cost << " Speedup: " << factory_speedup << " Goal " << goal << std::endl ; 
		target_factories=0; 
		best_total = std::numeric_limits<double>::infinity(); 
		while( total <= best_total ) { 
			factories = 0; 			
			total = 0.0; 
			cps = default_cps;
			while( factories < target_factories ) { 
				total += factory_cost / cps; 	
				cps += factory_speedup;
				factories++; 
			}
			total += goal / cps; 
			if( total <= best_total) { 
				best_total = total; 
			}
			//std::cout << "Total: " << best_total << std::endl; 
			target_factories++; 
		}
		std::cout << "Case #" << i+1 << ": ";
		std::cout << std::fixed << std::setprecision(7) << best_total << std::endl; 
	}	

	return 0;
}
