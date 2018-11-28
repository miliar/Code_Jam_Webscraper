//C.cpp

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <bitset>
#include <set>
#include <cmath>

using namespace std;

// http://www-h.eng.cam.ac.uk/help/importedHTML/languages/C++/Thinking_in_C++/tic0226.html
template<const int bits>
bitset<bits> randBitset() {
  bitset<bits> r(rand());
  for(int i = 0; i < bits - 1; i++) {
    r <<= bits;
    r |= bitset<bits>(rand()); 
  }
  r |= (1<<bits-1) | 1;
  return r;
}

const int N = 16;
const int J = 50; 

typedef unsigned long long int uint64_t;

int firstDivisor(uint64_t n) {
	int n_sqrt = (int) sqrt(n) + 1;
	for (int i = 2; i < n_sqrt; ++i) {
		if (0 == n%i) return i;
	}
	return -1;
}

bool validate(bitset<N> b) {
	int divs[11];
	bool ok = true;
	for (int nbase = 2; nbase <= 10; ++nbase) {
		uint64_t val10 = 0;
		for (int i = 0; i < N; ++i) {
			if (b.test(i)) {
				val10 += pow(nbase, i);
			}
		}
		int div = firstDivisor(val10);
		if (div < 0) {
			ok = false;
			break;
		}
		divs[nbase] = div;
	}

	if (ok) {
		cout << b << "\t";
		for (int nbase = 2; nbase < 10; ++nbase) {
			cout << divs[nbase] << "\t";
		}
		cout << divs[10] << endl;
	}

	return ok;
}


int main()
{
	srand(time(0));
	set < unsigned long > allsets;

	cout << "Case #1: \n";

	while (allsets.size() < J) {
    	bitset<N> b = randBitset<N>();
        unsigned long ul = b.to_ulong();
        if (allsets.find(ul) != allsets.end()) {
        	continue;
        }

        if (validate(b)) allsets.insert(ul);
	}
    
    return 0;
}