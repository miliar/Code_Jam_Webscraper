#include <string>
#include <fstream>
#include <iostream>
#include <vector>

template<typename T>
std::ostream& operator<< (std::ostream& out, const std::vector<T>& v) {
    out << "[";
    size_t last = v.size() - 1;
    for(size_t i = 0; i < v.size(); ++i) {
        out << v[i];
        if (i != last) 
            out << ", ";
    }
    out << "]";
    return out;
}

/*unsigned op(std::vector<unsigned> &Pi){
	unsigned max = 0;
	unsigned imax = 0;
	for(unsigned i=0; i<Pi.size(); i++)
		if(Pi[i] > max){
			max = Pi[i];
			imax = i;
		}

	auto Pmax = Pi[imax];
	Pi[imax] /= 2;
	Pi.push_back(Pmax - Pi[imax]);
	
	max = 0;
	for(unsigned i=0; i<Pi.size(); i++)
		if(Pi[i] > max){
			max = Pi[i];
		}
	
	return max;
}


unsigned int solve(	unsigned int D, std::vector<unsigned> &Pi){
	unsigned best = 0;
	for(unsigned i=0; i<Pi.size(); i++)
		best = std::max(best, Pi[i]);
	
	unsigned step = 0;
	unsigned max = 0;
	unsigned max_steps = D + 1;
	do{
		max = op(Pi);
		step ++;	
		if(best > step + max){
			best = step + max;
			max_steps = Pi.size() + 1;
		}
		max_steps--;
	}while(max>1);
	return best;
}*/

unsigned solve(std::vector<unsigned> Pi, unsigned split){
	unsigned max = 0;
	unsigned imax = 0;
	for(unsigned i=0; i<Pi.size(); i++)
		if(Pi[i] > max){
			max = Pi[i];
			imax = i;
		}

	//std::cout << "SplitIn "<<split << " -> " << Pi << "\n";
		
	auto Pmax = Pi[imax];
	Pi[imax] /= split;
	Pi.push_back(Pmax - Pi[imax]);
	//std::cout << "SplitOut"<<split << " -> " << Pi << "\n";
	
	unsigned best = 0;
	for(auto P:Pi)
		best = std::max(best, P);
	
	for(unsigned i=2; i<=best/2; i++)
		best =  std::min(solve(Pi, i) + 1, best);
	return best;
}


unsigned int solve(std::vector<unsigned> &Pi){
std::cout << "Start -> " << Pi << "\n";
	unsigned best = 0;
	for(auto P:Pi)
		best = std::max(best, P);

	for(unsigned i=2; i<=best/2; i++)
		best =  std::min(solve(Pi, i) + 1, best);
	std::cout << "Best = "<< best << "\n";
	return best;
}



int main (int argn, char** args){
	std::string in = args[1];
	std::string out = args[2];

	std::fstream input(in, std::ios_base::in);
	std::fstream output(out, std::ios_base::out);
	
	unsigned int cases;
	input >> cases;
	for(unsigned i=0; i<cases; i++){
		unsigned int D;
		std::vector<unsigned> Pi;
		input >> D;
		for(unsigned i=0; i<D; i++){
			unsigned t;
			input >> t;
			Pi.push_back(t);
		}
		
		output << "Case #" << (i+1) << ": " << solve(Pi) << "\n";
	}


	return 0;
}