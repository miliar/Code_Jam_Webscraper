#include <fstream>
using namespace std;

#include "Discs.cpp"

int main() {
	ifstream infile("A-large.in");
	ofstream outfile("results.out");
	Discs test;
	test.go(infile, outfile);
}