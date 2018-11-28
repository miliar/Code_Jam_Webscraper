#include <iostream>
#include <cmath>
#include <vector>

bool palindrome(double i);

int main(){
	int t_cases, r;
	double a, b;
	
	scanf("%d",&t_cases);
	for(int t = 0; t < t_cases; ++t){
		scanf("%lf %lf",&a, &b);
		r = 0;
		for(double i = a; i <= b; i+=1.0){
			if(palindrome(i) && palindrome(sqrt(i))){
				//std::cout << i << " | "<< sqrt(i) << std::endl;
				r++;
			}
		}
		std::cout << "Case #" << t+1 << ": " << r << std::endl;
	}
	return 0;
}

bool palindrome(double i){
	long l = static_cast<long>(i);
	if((i - l) > 0.0){
		return false;
	}
	
   	std::vector<int> digs;
	while(l){
		digs.push_back(l%10);
		l /= 10;
	}
	
	std::vector<int>::iterator it = digs.begin();
	std::vector<int>::reverse_iterator rit = digs.rbegin();
	while(it != digs.end() && rit != digs.rend()){
		if(*it != *rit){
			return false;
		}
		++it;
		++rit;
	}
	return true;
}

///EOF
