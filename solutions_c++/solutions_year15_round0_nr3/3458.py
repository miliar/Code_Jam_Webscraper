// practice.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stdio.h>
#include <algorithm>
#include <deque>
#include <string>
#include <unordered_map>

using namespace std;

unordered_map<char, unordered_map<char, string>> matrix = {
	{ '1', { { '1', "1" }, { 'i', "i" }, { 'j', "j" }, { 'k', "k" } } },
	{ 'i', { { '1', "i" }, { 'i', "-1" }, { 'j', "k" }, { 'k', "-j" } } },
	{ 'j', { { '1', "j" }, { 'i', "-k" }, { 'j', "-1" }, { 'k', "i" } } },
	{ 'k', { { '1', "k" }, { 'i', "j" }, { 'j', "-i" }, { 'k', "-1" } } }
};

class IJK {
private:
	int L, X;
	string str;
	vector<vector<string>> matrixInt;

public:

	string multiply(const string& i, const string& j) {
		char indi, indj;
		int signi = 1, signj = 1;
		if (i[0] == '-') { indi = i[1]; signi = -1; }
		else indi = i[0];
		if (j[0] == '-') { indj = j[1]; signj = -1; }
		else indj = j[0];
		int sign = signi * signj;
		string val = matrix[indi][indj];
		if (sign == -1) val = (val[0] == '-') ? val.substr(1) : "-" + val;
		return val;
	}
	void parseData() {
		string line;

		cin >> L;
		cin >> X;
		getline(cin, line);
		cin >> str;
		getline(cin, line);
	}


	string solve() {
		string res;
		string src;
		set<char> cs;

		for (int i = 0; i < X; ++i)
			src += str;

		string fromLeft = "1";
		string toRight = "1";

		//vector<vector<string>> product(src.size(), vector<string>(src.size(), ""));
		size_t start = 0;
		for (; start < src.size(); ++start) {
			fromLeft = multiply(fromLeft, src.substr(start, 1));
			if (fromLeft == "i") break;
		}
		if (start == src.size()) return "NO";
		++start;
		size_t end = src.size();
		for (; end > 0; --end) {
			toRight = multiply(src.substr(end - 1, 1), toRight);
			if (toRight == "k") break;
		}
		if (end == 0) return "NO";
		--end;
		string mid = "1";
		for (size_t ind = start; ind < end; ++ind) {
			mid = multiply(mid, src.substr(ind, 1));
		}
		if (mid == "j") return "YES"; else return "NO";
	}
};

int main(int argc, char* argv[])
{
	string line;
	int count;

	cin >> count;
	getline(cin, line);

	for (int i = 1; i <= count; ++i) {
		IJK so;
		so.parseData();
		cout << "Case #" << i << ": " << so.solve() << endl;
	}
	return 0;
}

