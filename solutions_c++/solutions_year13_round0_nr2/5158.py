#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int uint;

int sign(int x) {
	return x > 0 ? 1 : x < 0 ? -1 : 0;
}

bool possible(uint x, uint y, int *table, uint xi, uint yi) {
	int d = table[xi * y + yi];
	bool a = true;
	for(uint x2 = 0; x2 != x; x2++) {
		if(table[x2 * y + yi] > d) {
			a = false;
			break;
		}
	}
	if(a) {
		return true;
	}

	a = true;
	for(uint y2 = 0; y2 != y; y2++) {
		if(table[xi * y + y2] > d) {
			a = false;
			break;
		}
	}

	return a;
}


bool possible(uint x, uint y, int *table) {
	for(uint xi = 0; xi != x; xi++) {
		for(uint yi = 0; yi != y; yi++) {
			if(!possible(x, y, table, xi, yi)) {
				//cout<<"Failed at : "<<xi<<" "<<yi<<endl;
				return false;
			}
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
		uint x = 0;
		uint y = 0;
		in>>x>>y;
		int *table = new int[x * y];
		for(uint xi = 0; xi != x; xi++) {
			for(uint yi = 0; yi != y; yi++) {
				in>>table[xi * y + yi];
			}
		}

		cout<<"Case #"<<i + 1<<": "<<(possible(x, y, table) ? "YES" : "NO")<<endl;

	}
	return 0;
}

