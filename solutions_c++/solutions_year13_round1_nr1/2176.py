#include<iostream>
#include<vector>
//#include<cmath>
#include<gmpxx.h>

struct rt{
	//unsigned long long r,t;
	mpf_class r,t;
};

std::vector<rt> cases;

void parse_input(std::istream& input){
	int cases_n; 	input>>cases_n; 
	cases.resize(cases_n);
	for(auto& c:cases){
		input>>c.r; input>>c.t;
	}
}

mpz_class solve_case(const rt& c){
	//long double tmp=(2*c.r+3)/4;
	//return 1+std::floor(std::sqrt((c.t-(2*c.r+1))/2+tmp*tmp)-tmp);
	mpf_class tmp=(2*c.r+3)*0.25;
	return 1+floor(sqrt((c.t-(2*c.r+1))/2+tmp*tmp)-tmp);
}

int main(){
	parse_input(std::cin);
	for(int i=0;i<cases.size();i++){
		std::cout<<"Case #"<<i+1<<": "<<solve_case(cases[i])<<std::endl;
	}

	return 0;
}
