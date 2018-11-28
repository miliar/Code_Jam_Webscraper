#include <iostream>
#include <numeric>
#include <algorithm>
#include <functional>
#include <iterator>
#include <set>
#include <vector>
#include <utility>

	// 1 = 0, i = 1, j = 2, k = 3, -1 = 4, -i = 5, -j = 6, -k = 7 //
	char jumps[8][8] = {
	//   1  i  j  k -1 -i -j -k
		{0, 1, 2, 3, 0, 0, 0, 0}, //  1
		{1, 4, 3, 6, 0, 0, 0, 0}, //  i
		{2, 7, 4, 1, 0, 0, 0, 0}, //  j
		{3, 2, 5, 4, 0, 0, 0, 0}, //  k
		{0, 0, 0, 0, 0, 0, 0, 0}, // -1
		{0, 0, 0, 0, 0, 0, 0, 0}, // -i
		{0, 0, 0, 0, 0, 0, 0, 0}, // -j
		{0, 0, 0, 0, 0, 0, 0, 0}, // -k
	};


char jump(char from, char to) { return jumps[from][to]; }

int main() {
	for (int i=0;i<4;++i)
	for (int j=4;j<8;++j)
		jumps[i][j] = (jumps[i][j-4] + 4) % 8;
	
	for (int i=4;i<8;++i)
	for (int j=0;j<8;++j)
		jumps[i][j] = (jumps[i-4][j] + 4) % 8;
/*	
	for (int i=0;i<8;++i) {
		for (int j=0;j<8;++j) {
			std::clog << (short)jumps[i][j] << " ";
		}
		std::clog << std::endl;
	}
*/	
	unsigned n;
	std::cin >> n;
	for (unsigned i=0; i<n; ++i) {
		unsigned strLen, repeats;
		std::cin >> strLen;
		std::cin >> repeats;
		
		std::string str;
		std::cin >> str;
		
		typedef char Q;

		std::vector<Q> v;
		v.reserve(str.size() * repeats);
		for (int r=0; r<repeats; ++r) {
			std::transform(str.begin(), str.end(), std::back_inserter(v), std::bind2nd(std::minus<char>(), 'i'-1));
		}

		bool gotIt = false;
		bool canGet = false;
		int iEnd=0, jEnd=1;
		std::vector<Q>::iterator it, jt;
	
		Q prod = std::accumulate(v.begin(), v.end(), 0, &jump);
		canGet = prod == 4; // ijk is -1

		if (canGet) {
	
		it = v.begin();
		Q iTry = 0;
		for (iEnd=0; iEnd + 2 < v.size() && !gotIt; ++iEnd) {
			iTry = jump(iTry, *it++);
			if (iTry != 1)
				continue;

			Q jTry = 0;
			jt = it; // already ++
			for (jEnd=iEnd+1; jEnd + 1 < v.size(); ++jEnd) {
				//std::clog << ":" << iEnd << " / " << jEnd << std::endl;
				jTry = jump(jTry, *jt++);
				if (jTry != 2)
					continue;
				Q kTry = std::accumulate(jt, v.end(), 0, &jump);
				if (kTry == 3) {
					//std::clog << iEnd << " / " << jEnd << std::endl;
					gotIt = true;
					break;
				}
			}
		}
	
		}

		std::cout << "Case #" << i+1 << ": " << (gotIt ? "YES" : "NO") << std::endl;
	}
	return 0;
}

