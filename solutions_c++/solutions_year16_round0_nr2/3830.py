#include <fstream>
#include <iostream>
#include <map>

using namespace std;

struct node
{
	int a;
	int b;
	node() {
		a = 0;
		b = 0;
	}
	node(int aa, int bb) {
		a = aa;
		b = bb;
	}
};

int main() {
	map<string, node> p;
	p.insert(pair<string, node>("+", node(0, 1)));
	p.insert(pair<string, node>("-", node(1, 0)));
	map<string, node> m, k;
	m = p;
	for (int i = 1; i <= 10; i++) {
		for (map<string, node>::iterator it = m.begin(); it != m.end(); ++it) {
			string tmp = it -> first;
			tmp += '+';
			k.insert(pair<string, node>(tmp, node((it -> second).a, (it -> second).a + 1)));
			//
			tmp = it -> first;
			tmp += '-';
			k.insert(pair<string, node>(tmp, node((it -> second).b + 1, (it -> second).b)));
		}
		for (map<string, node>::iterator it = k.begin(); it != k.end(); ++it) {
			p.insert(pair<string, node>(it -> first, it -> second));
		}
		m.clear();
		m = k;
		k.clear();
	}
	fstream infile, outfile;
	infile.open("B-small-attempt1.in", ios::in);
	outfile.open("tmp.out", ios::out);
	int n;
	infile >> n;
	for (int i = 1; i <= n; i++) {
		string test;
		infile >> test;
		outfile << "Case #" << i <<": "<< p[test].a << endl;
	}
	return 0;
}