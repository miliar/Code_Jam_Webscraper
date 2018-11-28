#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <array>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <bitset>
#include <utility>
#include <limits>
#include <iterator>
#include <numeric>
#include <climits>

using namespace std;

int main(int argc, char** argv){

	unsigned long T;
	cin >> T;

	for(unsigned long t=1; t<=T; ++t){
		cout << "Case #" << t << ": ";

		long A,N;
		cin >> A >> N;

		vector<long> motes(N);
		generate(motes.begin(),motes.end(), [](){
				long m;
				cin >> m;
				return m;
		});

		sort(motes.begin(), motes.end());

		long size = A;
		long min_steps = motes.size();
		long steps = 0;
		long rest = motes.size();

		for(auto mote : motes){
			if(size <= 1) {
				steps = min_steps;
				break;
			}

			if(steps + rest < min_steps){
				min_steps = steps + rest;
			}

			//add new motes
			while(size <= mote){
				size += (size-1);
				steps++;
			}
			size += mote;

			rest--;
		}
		if(steps < min_steps) min_steps = steps;

		cout << min_steps;

		cout << endl;
	}

	return 0;
}
