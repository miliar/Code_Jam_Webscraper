#include <iostream>
#include <bitset>

using big_uint = unsigned long long;

std::string solve_case(const unsigned case_num, const big_uint case_seed){
	std::string ret = "Case #" + std::to_string(case_num) +": ";
	if(case_seed == 0) return ret + "INSOMNIA";
	std::bitset<10> has_found;
	auto look_at = 0;
	do{
		look_at += case_seed;
		auto copy = look_at;
		do{
			has_found[copy%10] = true;
		}while((copy/=10) != 0);
	}while(!has_found.all());
	return ret + std::to_string(look_at);
}

int main(){
	unsigned n;
	std::cin >> n;
	big_uint buf;
	for(unsigned i=1;i<=n;++i){
		std::cin >> buf;
		std::cout << solve_case(i,buf) << std::endl;
	}
}
