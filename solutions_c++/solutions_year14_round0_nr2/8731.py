#include<iostream>
#include<iomanip>

const unsigned int INF=1000009;

int main(){
	std::ios_base::sync_with_stdio(false);
	std::cout.precision(14);
	unsigned int T;
	std::cin>>T;
	
	for(unsigned int i=0;i<T;++i){
		long double C,F,X;
		std::cin>>C>>F>>X;
		
		long double sum_c=0;
		long double r=INF;
		long double f=2;
		while(sum_c<r){
			r=std::min(r,sum_c+(X/f));
			sum_c+=C/f;
			f+=F;
		}
		
		std::cout<<"Case #"<<(i+1)<<": "<<r<<"\n";
	}
	
	return 0;
}
