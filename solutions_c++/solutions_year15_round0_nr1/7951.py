// cjam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;


template < class ContainerT >
void split(const std::string& str, ContainerT& tokens,
	const std::string& delimiters = " ", bool trimEmpty = false)
{
	std::string::size_type pos, lastPos = 0;

	using value_type = typename ContainerT::value_type;
	using size_type = typename ContainerT::size_type;

	while (true) {
		pos = str.find_first_of(delimiters, lastPos);
		if (pos == std::string::npos) {
			pos = str.length();

			if (pos != lastPos || !trimEmpty)
				tokens.push_back(value_type(str.data() + lastPos,
				(size_type)pos - lastPos));

			break;
		} else {
			if (pos != lastPos || !trimEmpty)
				tokens.push_back(value_type(str.data() + lastPos,
				(size_type)pos - lastPos));
		}

		lastPos = pos + 1;
	}
}



int opera(string str, int clapping, int extra, int k, int max)
{
	if (str.length() == 1) {
		return 0;
	}

	if (k > max) return extra;

	int k_n = str[k] - '0';
	if (k_n == 0) return opera(str, clapping, extra, k + 1, max);
	if (k == 0) return opera(str, k_n, extra, k + 1, max);
	int diff = k - clapping;
	return  k <= clapping ? opera(str, clapping + k_n, extra, k + 1, max) : opera(str, clapping + k_n + diff, extra + diff, k + 1, max);
}


int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	string line = "";
	int T;
	cin >> T;
	getline(cin, line);
	for (int i = 0; i < T; i++) {
		getline(cin, line);
		vector<string> tokens;
		split(line, tokens, " ");
		int len = stoi(tokens[0]);
		string str = tokens[1];
		auto r = opera(str, 0, 0, 0, len);
		cout << "Case #" << i + 1 << ": " << r << "\n";
	}
	return 0;
}