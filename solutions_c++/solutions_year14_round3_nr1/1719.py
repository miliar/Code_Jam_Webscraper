#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <math.h>
#include <gmpxx.h>
#include <algorithm>
#include <assert.h>

long long gcd(long long p, long long q) {
	while(1) {
		long long t = q%p;
		if( t== 0) {
			return p;
		}
		else if (t==1) {
			return 1;
		}
		q = p;
		p =t;
	}

}

void solve(std::ifstream& in)
{
	long long p, q;
	char abc;
	in >> p >> abc>> q;
	long long t = gcd(p, q);
	q = q/t;
	p = p/t;
	for(int i =0; i <= 40;++i) {
		long long t = 1 << i;
		if(q == t) {
			break;
		}
		else if(q < t ) {
			printf("impossible\n");
			return;
		}
	}
	int gen =1;
	while(1) {
		p = p *2;
		if(p >=q) {
			printf("%d\n", gen);
			return;
		}
		gen++;
	}
}
int main(int argc, char* argv[]) 
{
	if(argc < 2) {
		std::cerr << "missing input file\n" ;
		return 1;
	}

	std::ifstream in(argv[1]);
	int c ;
	in  >> c;
	for(int i =1; i <=c;++i) {
		printf("Case #%d: ", i);
		solve(in);
	}
	return 0;
}
