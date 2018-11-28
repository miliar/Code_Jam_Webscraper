#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;


unsigned int solution(vector<unsigned int> pancakes) {
	// cout << "SOLVING" << endl;
	auto it = max_element(pancakes.begin(), pancakes.end());
	auto max_location = distance(pancakes.begin(), it);
	// cout << "MaX " << *it << " and length " << pancakes.size() << endl;
	if (*it <= 3)
		return *it; // Solution
	unsigned quickest = *it;
	// Search for solution by division
	for (unsigned int i = 2; i <= sqrt(pancakes.at(max_location)); ++i) {
		unsigned int temp = pancakes.at(max_location);
		pancakes.at(max_location) = (temp / i) * (i - 1);
		pancakes.push_back(temp / i + temp % i);
		unsigned int sol = 1 + solution(pancakes);
		if (sol < quickest)
			quickest = sol;
		pancakes.at(max_location) = temp;
		pancakes.pop_back();
	}

	return quickest;
}

int main(int argc, char* argv[]) {
	unsigned int tests;
	unsigned int count = 0;
	cin >> tests;

	while (count < tests) {
		vector<unsigned int> pancakes;
		unsigned int numPancakes;
		cin >> numPancakes;
		unsigned int currPancakes = 0;
		while (currPancakes < numPancakes) {
			unsigned int currDiner;
			cin >> currDiner;
			pancakes.push_back(currDiner);
			currPancakes++;
		}
		// cout << "PRINTING PANCAKES " << endl;
		// for (auto i : pancakes)
		// 	cout << "    " << i << endl;
		// cout << endl << endl;
		count++;
		cout << "Case #" << count << ": " << solution(pancakes) << endl;
	}

	return 0;
}