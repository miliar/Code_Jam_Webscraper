#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string input;
bool is_ij[10000];
bool is_k[10000];

struct Node {
	Node(char ch, int sign) {
		this->ch = ch;
		this->sign = sign;
	}
	char ch;
	int sign;
};

const char trans[4][5] = {"1234", "2143", "3412", "4321"};
const int trans_sign[4][4] = {{1, 1, 1, 1}, {1, -1, 1, -1}, {1, -1, -1, 1}, {1, 1, -1, -1}};

Node mul(const Node &a, const Node &b) {
	Node res(trans[a.ch - '1'][b.ch - '1'], a.sign * b.sign * trans_sign[a.ch - '1'][b.ch - '1']);
	return res;
}

int main() {
	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.out");
	int t;
	fin >> t;
	for (int i = 1; i <= t; i++) {
		int l, x;
		fin >> l >> x;
		fin >> input;
		string str;
		while (x--) str += input;
		Node m('1', 1);
		bool has_i = false;
		for (int j = 0; j < str.size(); j++) {
			Node node(str[j] - 'i' + '2', 1);
			m = mul(m, node);
			is_ij[j] = (has_i && m.ch == '4' && m.sign == 1);
			if (!has_i && m.ch == '2' && m.sign == 1)
				has_i = true;
		}
		Node m2('1', 1);
		for (int j = str.size() - 1; j >= 0; j--) {
			Node node(str[j] - 'i' + '2', 1);
			m2 = mul(node, m2);
			is_k[j] = (m2.ch == '4' && m2.sign == 1);
		}
		bool res = false;
		for (int j = 0; j < str.size() - 1; j++)
			if (is_ij[j] && is_k[j + 1]) {
				res = true;
				break;
			}
		fout << "Case #" << i << ": " << (res ? "YES" : "NO") << endl;
	}
	return 0;
}