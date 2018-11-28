/* Round 1C
 * Problem A
 * intrepid
 */
#include <cassert>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>
#include <numeric>
#include <memory>
#include <limits>
#include <random>
#include <chrono>
using namespace std;

bool is_c(char c)
{
	return ! (
		( c == 'a' ) ||
		( c == 'e' ) ||
		( c == 'i' ) ||
		( c == 'o' ) ||
		( c == 'u' )
	);
}

int main(int /*argc*/, char **/*argv[]*/)
{
	cout << scientific << setprecision(6);
	int runs;
	cin >> runs;
	for (int run=1; run <= runs; ++run) {
		cout << "Case #" << run << ": ";
		
		// Start solving
		string name;
		int n;
		cin >> name >> n;
		int L = name.size();
		
		vector<int> starts;
		vector<int> sizes;
		
		bool finding = false;
		int numStrands = 0;
		for (int i=0; i<L; ++i) {
			if ( !finding && is_c(name[i]) ) {
				finding = true;
				starts.push_back(i);
				++numStrands;
			}
			else if ( finding && !is_c(name[i]) ) {
				finding = false;
				sizes.push_back(i-starts[numStrands-1]);
			}
		}
		if ( finding ) sizes.push_back(L - starts[numStrands-1]);
		
		unsigned long long count = 0;
		for (int test_size = L; test_size >= n; --test_size) {
			for (int pos = 0; pos <= L - test_size; ++pos) {
				for (int i = 0; i < numStrands; ++i) {
					if ( ( starts[i] >= pos + n - sizes[i] ) &&
						( starts[i] <= pos + test_size - n ) &&
						( sizes[i] >= n )
					) {
						++count;
						break;
					}
				}
			}
		}
		
		cout << count;
		
		cout << "\n";
	}
	if ( !cin.good() ) cerr << "Error reading!\n" << endl;
	
	return 0;
}
