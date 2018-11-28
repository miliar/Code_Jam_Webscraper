#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <math.h>
#include <gmpxx.h>
#include <algorithm>
#include <assert.h>

void solve(std::ifstream& in)
{
	int a, b, k;
	in >> a >> b>> k;
	if(a <=k || b <=k) {
		printf("%d\n", a*b);
		return;
	}
	
	int result = a * k + b * k - k * k;

	for(int i =k; i < a;++i) {
		for(int j = k; j < b;++j) {
			if( (i & j) < k) {
				result++;
			}
		}
	}
	printf("%d\n", result);

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
