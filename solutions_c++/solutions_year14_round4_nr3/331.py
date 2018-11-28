//
// flow.cpp
//
// Siwakorn Srisakaokul - ping128
// Written on Saturday, 31 May 2014.
//

#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <map>
#include <ctype.h>
#include <string.h>

#include <assert.h>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<PII, int> PII2;

#define MAXW 105
#define MAXH 505

int board[MAXH][MAXW];
int R, C;
int B;

struct MaximumFlowFordFulkerson {

    // runtime: O(E F), E = #edges, F = max flow values

    typedef struct edge {
	int v;
	int capacity; 
	int flow; // current amount allowed to flow
	edge(int v, int c, int f) : v(v), capacity(c), flow(f) {}
    } Edge;
 
    int N; // node from 0 to N - 1
    vector<vector<Edge> > maxFlowEdge;
    int mark;   // global variable for checking if a node is already visited
    vector<int> seen;  // status of each node

    MaximumFlowFordFulkerson(int numNode){
	N = numNode;
	maxFlowEdge = vector<vector<Edge> >(numNode);
	seen = vector<int>(numNode);
	mark = 0;
    }

    void addEdge(int from, int to, int cap){
	maxFlowEdge[from].push_back(Edge(to, cap, cap));
	maxFlowEdge[to].push_back(Edge(from, 0, 0));
    }
 
    void resetFlow(){
	for(int i = 0; i < N; i++ ){
	    int sz = maxFlowEdge[i].size();
	    for(int j = 0; j < sz; j++ ){
		maxFlowEdge[i][j].flow = maxFlowEdge[i][j].capacity;
	    }
	}
    }
 
    int findAugmentingPath(int at, int sink, int val){
	int sol = 0;
	seen[at] = mark;
	if(at == sink) return val;
	int sz = maxFlowEdge[at].size();
	for(int i = 0; i < sz; i++ ){
	    int v = maxFlowEdge[at][i].v;
	    int f = maxFlowEdge[at][i].flow;
	    if(seen[v] != mark && f > 0){
		sol = findAugmentingPath(v, sink, min(f, val));
		if(sol){
		    maxFlowEdge[at][i].flow -= sol;
		    for(int j = 0; j < maxFlowEdge[v].size(); j++ ){
			if(maxFlowEdge[v][j].v == at){
			    maxFlowEdge[v][j].flow += sol;
			    break;
			}
                    }
		    return sol;
		}
	    }
	}
	return 0;
    }
 
    int getMaximumFlow(int S, int T){
	int res = 0;
	while(1){
	    mark++;
	    int flow = findAugmentingPath(S, T, 1000000000);
	    if(flow == 0) break;
	    else res += flow;
	}
	return res;
    }
};

int cx[] = {0, 0, 1, -1}, cy[] = {-1, 1, 0, 0};

void solve() {
    for (int i = 0; i < MAXH; i++)
        for (int j = 0; j < MAXW; j++)
            board[i][j] = 0;
    
    cin >> C >> R >> B;
    for (int i = 0; i < B; i++) {
        int jj1, ii1, jj2, ii2;
        cin >> jj1 >> ii1 >> jj2 >> ii2;
        for (int j = ii1; j <= ii2; j++) {
            for (int k = jj1; k <= jj2; k++) {
                board[j][k] = 1;
            }
        }
    }
    /*
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) cout << board[i][j] << " ";
        cout << endl;
    }
    */
    MaximumFlowFordFulkerson solver = MaximumFlowFordFulkerson(R * C * 2 + 2);
    int SOURCE = R * C * 2;
    int SINK = R * C * 2 + 1;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            int id = i * C + j;
            if (board[i][j] == 0)
                solver.addEdge(id * 2, id * 2 + 1, 1);
            else
                solver.addEdge(id * 2, id * 2 + 1, 0);
            for (int k = 0; k < 4; k++) {
                int ii = i + cx[k];
                int jj = j + cy[k];
                if (ii >= 0 && jj >= 0 && ii < R && jj < C) {
                    int id2 = ii * C + jj;
                    solver.addEdge(id * 2 + 1, id2 * 2, 1);
                }
            }
        }
    }

    for (int j = 0; j < C; j++) {
        solver.addEdge(SOURCE, j * 2, 1);
    }

    for (int j = 0; j < C; j++) {
        int id = (R - 1) * C + j;
        solver.addEdge(id * 2 + 1, SINK, 1);
    }

    cout << solver.getMaximumFlow(SOURCE, SINK) << endl;

}

int main() {
    int test;
    scanf("%d", &test);
    for (int tt = 0; tt < test; tt++) {
        printf("Case #%d: ", tt + 1);
        solve();
    }
    return 0;
}
