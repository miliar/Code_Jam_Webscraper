#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <sstream>

typedef unsigned int uint;
typedef uint64_t uint64;

using namespace std;

template<typename T>
string fromNum(T i) {
	std::ostringstream oss;
	oss.precision(256);
	oss<<i;
	return oss.str();
}

bool pal(const string &str) {
	const char *ch = str.c_str();
	uint size = str.size();
	for(uint i = 0; i != size / 2; i++) {
		if(ch[i] != ch[size - i - 1]) {
			return false;
		}
	}
	return true;
}

int main()
{
	ifstream in;
	in.open("test.txt");

	if(!in.is_open()) {
		cerr<<"Unable to open input file"<<endl;
		return 1;
	}

	uint t = 0;
	in>>t;


	for(uint i = 0; i != t; i++) {
		double dmin = 0;
		double dmax = 0;
		in>>dmin>>dmax;

		uint64 sqmin = floor(sqrt(dmin));
		uint64 sqmax = ceil(sqrt(dmax)) + 1;
		uint64 max = dmax;
		uint64 min = dmin;

		while(sqmin * sqmin < min) {
			sqmin++;
		}
		uint64 count = 0;
		for(uint64 w = sqmin; w * w <= max; w++) {
			if(pal(fromNum(w)) && pal(fromNum(w * w))) {
				count++;
				//cout<<w * w<<" ("<<w<<")"<<endl;
			}
		}

		cout<<"Case #"<<i + 1<<": "<<count<<endl;

	}
	return 0;
}

