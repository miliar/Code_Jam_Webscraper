#include <cstdio>
#include <deque>
#include <string>
#include <sstream>

using std::deque;
using std::string;

bool isPali(unsigned long long val)
{
	string num;
	std::stringstream out;
	
	out << val;
	num = out.str();
	
	string::iterator ini, fim;
	
	ini = num.begin();
	fim = num.end();
	fim--;
	
	while(ini < fim){
		if(*ini != *fim){
			return false;
		}
		
		ini++;
		fim--;
	}
	
	return true;
}

int main(void)
{
	deque<unsigned long long> valores;
	
	unsigned long long a, b;
	int t, k;
	
	for(unsigned long long i = 1; i <= 10000000; i++){
		if(isPali(i)){
			unsigned long long quad = i*i;
			if(quad <= 100000000000000){
				if(isPali(quad)){
					valores.push_back(quad);
				}
			}
		}
	}

	scanf("%d\n", &t);
	
	for(k = 1; k <= t; k++){
	
		deque<unsigned long long>::iterator it;
		int total, cont;
		
		cont = 0;
		
		scanf("%llu %llu\n", &a, &b);
		
		it = valores.begin();
		
		while(it != valores.end() && (*it < a)){
			it++;
			cont++;
		}
		
		if(it == valores.end()){
			total = 0;
		} else{
			total = cont;

			while(it != valores.end() && (*it <= b)){
				it++;
				cont++;
			}
			
			total = cont - total;
		}
		
		printf("Case #%d: %d\n", k, total);
	}
	
	return 0;
}
