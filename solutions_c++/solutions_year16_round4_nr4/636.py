#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <unordered_map>

using namespace std;

template <class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
	cout << "Case #" << caseNumber << ": " << ans << endl;
}


int GetNumEdges(const vector< vector<bool> >& graph) {
    int n = graph.size();
    int res = 0;
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            res += graph[y][x];
        }
     }
    return res;
}

bool HasSelectionOrder(const vector<int>&arrivalOrder, const vector< vector<bool> >& graph, int pos, vector<bool>& used) {
    bool ans = true;

    if (pos == arrivalOrder.size()) {
        return true;
    }
    bool f = false;
    for (int i = 0; i < arrivalOrder.size(); i++) {
        if (!used[i] && graph[arrivalOrder[pos]][i]) {
            used[i] = true;
            f = true;
            ans = ans && HasSelectionOrder(arrivalOrder, graph, pos + 1, used);
            used[i] = false;
        }
    }
    return ans && f;
}


int SolveBruteForce(vector< vector<bool> > graph) {
    int n = graph.size();
    int numEdges = GetNumEdges(graph);
    int ans = 1000;
    vector< vector<bool> > newGraph(n, vector<bool>(n, false));
    for (int mask = 1; mask < (1 << (n * n)); mask++) {
        for (int j = 0; j < n * n; j++) {
            if (mask & (1 << j)) {
                newGraph[j / n][j % n] = true;
            } else {
                newGraph[j / n][j % n] = false;
            }
        }
        bool isValid = true;
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                if (!newGraph[y][x] && graph[y][x]) {
                    isValid = false;
                }
            }
        }
        if (!isValid) {
            continue;
        }

        bool good = true;
        vector<int> arrivalOrder(n);
        for (int i = 0; i < n; i++) {
            arrivalOrder[i] = i;
        }

        do {
            vector<bool> used(n, false);
            good = good && HasSelectionOrder(arrivalOrder, newGraph, 0, used);
        } while (next_permutation(arrivalOrder.begin(), arrivalOrder.end()));
        if (good) {
            ans = min(ans, GetNumEdges(newGraph) - numEdges);
        }
    }
    return ans;
}

int SolveTestCase() {
    int n;
    cin >> n;
    string tmp;
    vector< vector<bool> > graph(n, vector<bool>(n, false));
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        for (int j = 0; j < n; j++) {
            graph[i][j] = (tmp[j] == '1');
        }
    }

    
    return SolveBruteForce(graph);
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("small.in", "r", stdin);
	//freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase() );

	return 0;
}