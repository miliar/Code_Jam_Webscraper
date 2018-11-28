#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>


std::vector<std::vector<std::string> > starts;

void initStarts() {

	std::vector<std::string> nextStart;

	nextStart.push_back("P");
	nextStart.push_back("R");
	nextStart.push_back("S");
	starts.push_back(nextStart);

	for (unsigned i=1; i<13; ++i) {
		nextStart.clear();
		nextStart.push_back(std::string(starts[i-1][0]).append(starts[i-1][1]));
		nextStart.push_back(std::string(starts[i-1][0]).append(starts[i-1][2]));
		nextStart.push_back(std::string(starts[i-1][1]).append(starts[i-1][2]));
		starts.push_back(nextStart);
	}
}


unsigned count(const std::string& str, char c) {
	unsigned r = 0;
	for (unsigned i=0;i<str.length();++i) {
		if (str[i]==c) {
			++r;
		}
	}
	return r;
}

std::string findStart(unsigned n, unsigned r, unsigned p, unsigned s) {

	for (unsigned i=0;i<3;++i) {
		if (count(starts[n][i],'R') == r
				&& count(starts[n][i],'P') == p
				&& count(starts[n][i],'S') == s)
		{
			return starts[n][i];
		}
	}

	return "IMPOSSIBLE";
}


int main(int argc, char **argv) {

	initStarts();

	unsigned T;
	std::cin >> T;

	for (unsigned i=0; i<T; ++i) {
		unsigned N, R, P, S;
		std::cin >> N >> R >> P >> S;

		printf("Case #%d: %s\n",i+1,findStart(N,R,P,S).c_str());
	}

	return 0;
}










