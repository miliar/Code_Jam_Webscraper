//============================================================================
// Name        : Counter Culture
//============================================================================

#include <iostream>
#include <fstream>

#include <boost/config.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/dijkstra_shortest_paths.hpp>

using namespace std;
using namespace boost;

// Graph typedefs
typedef adjacency_list<vecS, vecS, directedS, no_property,
		property<edge_weight_t, int> > Graph;
typedef graph_traits<Graph>::edge_descriptor Edge;			// Edge type
typedef property_map<Graph, edge_weight_t>::type WeightMap;	// Map edge -> weight

long reverse(long number) {
	long reverse = 0;

	for( ; number!= 0 ; ) {
		reverse = reverse * 10;
		reverse = reverse + number%10;
		number = number/10;
	}

	return reverse;
}

Graph g(1000001);
WeightMap weightMap = get(edge_weight, g);

void buildGraph() {
	long max = 1000000;
	queue<long> q;
	q.push(1);
	while(!q.empty()) {
		long cur = q.front();
		q.pop();

		long inc = cur + 1;
		long rev = reverse(cur);

		bool success;
		Edge e;

		if (inc <= max) {
			tie(e, success) = add_edge(cur, inc, g);
			weightMap[e] = 1;
		}
		if (cur != rev && rev <= max) {
			tie(e, success) = add_edge(cur, rev, g);
			weightMap[e] = 1;
		}

		if (inc <= max) {
			q.push(inc);
		}
	}
}

int main() {

	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	ifstream in("in.txt");
	cin.rdbuf(in.rdbuf());

	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	buildGraph();
	//dijsktra
	vector<long> distances(num_vertices(g));
	dijkstra_shortest_paths(g, 1, distance_map(&distances[0]));

	long t;
	cin >> t;



	for (long i = 0; i < t; i++) {
		long n;
		cin >> n;
		long testCase = distances[n] + 1;
		cout << "Case #" << i + 1 << ": " << testCase << '\n';
	}

	in.close();
	out.close();

	return 0;
}
