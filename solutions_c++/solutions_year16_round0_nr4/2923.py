#include<iostream>
#include<cstdint>

int main(){
	int n_cases; std::cin>>n_cases;
	for(auto case_i=0; case_i<n_cases; ++case_i){
		std::cout<<"Case #"<<case_i+1<<": ";
		int base, digits, numbers;
		std::cin>>base>>digits>>numbers;
		std::cerr<<"b: "<<base<<", digits: "<<digits<<std::endl;
		if(base>numbers*digits){
			std::cout<<"IMPOSSIBLE"<<std::endl;
			continue;
		}
		for(auto digit=0; digit<base; ){
			uint64_t number=0;
			uint64_t base_exp_i=1;
			for(auto i=0; i<digits && digit<base; ++i, base_exp_i*=base, ++digit){
				number+=digit*base_exp_i;
				std::cerr<<"i: "<<i<<"n: "<<number<<std::endl;
			}
			std::cout<<number+1<<" ";
		}
		std::cout<<std::endl;
	}

	return 0;
}

