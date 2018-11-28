#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

int main() {
	long g;
	cin >> g;
	for(int i = 0; i< g; i++) {
		long b;
		cin >> b;
		string c;
		cin >> c;
		long f = 0;
		long e = 0;
		for(int j = 0; j< b+1; j++) {
			char cc[1];
			cc[0] = c.c_str()[j];
			long u = atol(cc);
			if(u > 0)
				e+= u-1;
			else if(e>0) 
				e--;
			else 
				f++;
		}
		cout << "Case #" << i+1 << ": " << f << endl;
	}
}