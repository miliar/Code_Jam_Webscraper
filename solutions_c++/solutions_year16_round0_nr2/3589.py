#include<iostream>
#include<cstdint>

int main(){
	int n_cases; std::cin>>n_cases;
	for(auto case_i=0; case_i<n_cases; ++case_i){
		std::cout<<"Case #"<<case_i+1<<": ";
		std::string s; std::cin>>s;
		int reverse_count=0;
		char plus_minus[]={'+','-'};
		int ok=0;
		while(!s.empty()){
			if(s.back()==plus_minus[ok]) {s.pop_back(); continue;}
			++reverse_count;
			ok=!ok;
		}
		std::cout<<reverse_count<<std::endl;
	}

	return 0;
}

