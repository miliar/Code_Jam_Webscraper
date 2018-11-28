#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <functional>
#include <queue>
using namespace std;
int main() {
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");
	int t;
	input >> t;
	for (int ccase = 1; ccase < t + 1; ++ccase) {
		output << "Case #" << ccase << ": ";
		priority_queue < pair<int, char>, vector<pair<int, char>>> senate;
		int a;
		char curr = 'A';
		input >> a;
		int z = 0;
		for (int i = 0; i < a; ++i) {
			int b;
			input >> b;
			senate.push(make_pair(b, curr));
			++curr;
			z = z + b;
		}
		int currr;
		char cur;
		if (z % 2 > 0) {
			cur = senate.top().second;
			currr = senate.top().first-1;
			output << cur << " ";
			senate.pop();
			senate.push(make_pair(currr, cur));
			--z;
		}
		while (z > 0) {
			cur = senate.top().second;
			currr = senate.top().first-1;
			output << cur;
			senate.pop();
			senate.push(make_pair(currr, cur));
			cur = senate.top().second;
			currr = senate.top().first-1;
			output << cur << " ";
			senate.pop();
			senate.push(make_pair(currr, cur));
			z = z - 2;
		}
		output << endl;
	}
	input.close();
	output.close();
	return 0;
}