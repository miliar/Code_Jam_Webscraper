#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct node {
	vector<unsigned> plates;
	unsigned stackingCost;
	unsigned max;
	bool destination;
};

class nodeComparator {
	public:
		bool operator() (const node& lhs, const node& rhs) const {
			return (lhs.stackingCost ) > (rhs.stackingCost );
		}
};

typedef priority_queue< node, vector<node>, nodeComparator> nodeList;

int main() {
	unsigned t;
	cin >> t;
	for (unsigned caseNum = 1; caseNum <= t; caseNum++) {
		unsigned d;
		cin >> d;
		node diners;
		// implementation of Dijkstra's
		for (unsigned i = 0; i < d; i++) { // readin the input and put into vector where diners[n] is the number of diners with n pancakes
			unsigned diner;
			cin >> diner;
			if (diners.plates.size() <= diner) {
				diners.plates.resize(diner+1);
			}
			diners.plates[diner]++;
		}
		// get the max cost and set stackingCost
		diners.stackingCost = 0;
		diners.destination = false;
		for (unsigned o = diners.plates.size()-1; o > 0; o--) {
			if (diners.plates[o] != 0) {
				diners.max = o;
				break;
			}
		}
		// create queue for nodes and push in starting point
		nodeList dinerqueue;
		dinerqueue.push(diners);
		while (!dinerqueue.empty()) {
			node state = dinerqueue.top();
			dinerqueue.pop();
			if (state.destination) { // reached destination
				cout << "Case #" << caseNum << ": " << state.stackingCost << "\n";
				break;
			}
			if (state.max > 1) { // is leaf node
			// add each division of the highest value to a new node and push into the queue
				for (unsigned i = 2; (state.max-(state.max/i)) < (state.max-1); i++) {
					node newNode = state;
					newNode.plates[state.max]--;
					newNode.plates[state.max/i]++;
					newNode.plates[state.max-(state.max/i)]++;
					newNode.stackingCost++;
					// find new max number in vector
					for (unsigned o = state.max; o > 0; o--) {
						if (newNode.plates[o] != 0) {
							newNode.max = o;
							break;
						}
					}
					dinerqueue.push(newNode);
				}
			}
			node endNode = state;
			endNode.destination = true;
			endNode.stackingCost = state.max + state.stackingCost;
			endNode.max = 0;
			dinerqueue.push(endNode);
		}
	}
	return 0;
}