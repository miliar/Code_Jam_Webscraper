#include <iostream>
#include <algorithm>
#include <utility>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>

typedef long long int ll;

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
	std::stringstream ss(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}


std::vector< std::vector<ll> > capacity;
std::vector< std::vector<ll> > residual;
std::vector<ll> h;

ll dfs(ll node, ll flow, ll source, ll sink)
{
	if (node == sink) {
		return flow;
	}

	for (ll i = 0; i < capacity.size(); i++) {
		if (residual[node][i] > 0 && h[node] == h[i] + 1) {
			ll df = dfs(i, std::min(flow, residual[node][i]), source, sink);

			if (df) {
				residual[node][i] -= df;
				residual[i][node] += df;
				return df;
			}
		}
	}

	/* no admissible edge */
	h[node]++;
	return 0;
}

ll max_flow(ll source, ll sink)
{
	/* Initial residual graph */
	residual.resize(capacity.size());
	for (ll i = 0; i < residual.size(); i++) {
		residual[i].resize(capacity[i].size());
		for (ll j = 0; j < residual[i].size(); j++) {
			residual[i][j] = capacity[i][j];
		}
	}

	/* Initial h label */
	h.resize(capacity.size());
	std::fill(h.begin(), h.end(), 0);

	ll flow = 0;
	while (h[source] < capacity.size()) {
		flow += dfs(source, LONG_MAX, source, sink);
	}
	return flow;
}


int main(int argc, char *argv[])
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);

	int ncases;
	std::cin >> ncases;

	capacity.resize(1200);
	for (int i = 0; i < capacity.size(); i++) {
		capacity[i].resize(1200);
	}

	for (int i = 1; i <= ncases; i++) {
		int n, word_index;
		std::string line;
		std::map<std::string, int> wordmap;

		for (int j = 0; j < capacity.size(); j++) {
			std::fill(capacity[j].begin(), capacity[j].end(), 0);
		}



		std::cin >> n;
		word_index = n + 1;
		std::getline(std::cin, line);
		for (int j = 1; j <= n; j++) {
			std::getline(std::cin, line);
			std::vector<std::string> words;
			words = split(line, ' ', words);

			for (int k = 0; k < words.size(); k++) {
				if (wordmap[words[k]] == 0) {
					// new word
					wordmap[words[k]] = word_index++;
				}
				capacity[j][wordmap[words[k]]] = 1;
				capacity[wordmap[words[k]]][j] = 1;
			}
		}

		std::cout << "Case #" << i << ": " << max_flow(1, 2) << std::endl;
	}


	
	return 0;
}