#include <iostream>
#include <vector>
#include <algorithm>

using big_uint = unsigned long long;

std::vector<bool> seed_to_bool_vec(const std::string& s){
	const auto size = s.size();
	std::vector<bool> ret(size,false);
	for(size_t i=0;i<size;++i){
		if(s[i] == '+') ret[i] = true;
	}
	return ret;
}

bool all(const std::vector<bool>& vec){
	return std::all_of(vec.begin(),vec.end(),[](bool v){return v;});
}

void partial_flip(std::vector<bool>& vec, size_t index){ // frip vec from top to index
	for(size_t i=0;i<=index;++i) vec[i] = !vec[i];
}

std::string solve_case(const unsigned case_num, const std::string case_seed){
	std::string ret = "Case #" + std::to_string(case_num) +": ";
	auto cakes = seed_to_bool_vec(case_seed);
	unsigned n = 0;
	for(;!all(cakes);++n){
		size_t i = 0;
		if(cakes[0]) for(;cakes[i] && i<cakes.size();++i);
		else for(;!cakes[i] && i<cakes.size();++i);
		partial_flip(cakes,(i!=0?--i:0));
	}
	return ret + std::to_string(n);
}

int main(){
	unsigned n;
	std::cin >> n;
	std::string buf;
	for(unsigned i=1;i<=n;++i){
		std::cin >> buf;
		std::cout << solve_case(i,buf) << std::endl;
	}
}
