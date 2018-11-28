#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


void flip (int range, std::vector<bool>& seq) {
	std::reverse(seq.begin(),seq.begin() + range);
	for (int i = 0; i < range; ++i) {
		seq[i].flip();
	}
}

uint32_t sorted (std::vector<bool>& seq) {
	uint32_t count = 0;
	for (int i = seq.size() -1; i >= 0 && seq[i] == 1; --i) {
		++count;
	}
	return count;
}

int main () {
	uint32_t T;
	std::cin >> T;

	for (int t = 0; t < T; ++t) {
		int count = 0;
		std::string S;
		std::cin >> S;
		std::vector<bool> seq;
		for (int i = 0; i < S.length(); ++i) {
			seq.push_back(S[i] == '+');
		} 
		
		while (sorted(seq) != seq.size()) {
			if (seq.front() == 0) {
				flip(seq.size() - sorted(seq),seq);
				++count; 
			}
			else {
				auto it = std::find(seq.begin(),seq.end(),0);
				if (it != seq.end()) {	
					flip(it - seq.begin(), seq);
					++count;
				}
			}
		}
		std::cout << "Case #"<< t+1 << ": " << count << std::endl;
	}
	return 0;
}
