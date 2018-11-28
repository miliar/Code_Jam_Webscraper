#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <math.h>
#include <stack>
#include <queue>
#include <stdio.h>

using namespace std;

#define INF 0x3FFFFFFF

#define MAX_VERTICES 100*500*6
#define MAX_EDGES 5 * MAX_VERTICES

struct vertex;
struct edge
{
	vertex *from, *to;
	int used, mi, ma; // min may be -max

	vertex* opposite(vertex* p)
	{ return (p == from ? to : from); }
	int left(vertex* p) // Source vertex, capacity left from p
	{ return (p == from ? ma - used : used - mi); }
	void add(vertex* p, int flow) // Source vertex, add from p
	{ used += (p == from ? flow : -flow); }
};
struct vertex
{
	vector<edge*> e; // Edge index
	edge* in; // Incoming edge, used in the breath first search
};

vertex v[MAX_VERTICES];
int numv = 0;
int nume = 0;
edge e[MAX_EDGES];

bool AugPath(vertex* source, vertex* dest)
{
	// Breadth-first search
	for(int i = 0; i < numv; ++i)
		v[i].in = 0;
	source->in = (edge*)-1; // reinterpret_cast<edge*>(-1)

	queue<vertex*> q;
	q.push(source);
	while(!q.empty())
	{
		vertex* cur = q.front();
		q.pop();
		// Check edges
		for(vector<edge*>::iterator it = cur->e.begin();
			it != cur->e.end(); ++it)
		{
			if((*it)->left(cur) > 0)
			{
				vertex* recv = (*it)->opposite(cur);
				if(!recv->in)
				{
					recv->in = *it;
					if(recv == dest)
						return true; // Found a path
					q.push(recv);
				}
			}
		}
	}
	return false;
}

int MaxFlow(vertex* source, vertex* dest)
{
	int maxflow = 0;
	while(AugPath(source, dest))
	{
		// Find flow to add
		int flow = 0x7FFFFFFF;
		edge* e;
		vertex* sender = dest; // The sender (in the loop)
		while((e = sender->in) != (edge*)-1)
			flow=min(flow,e->left(sender=e->opposite(sender)));
		// Add the flow
		sender = dest;
		while((e = sender->in) != (edge*)-1)
			e->add(sender = e->opposite(sender), flow);
		maxflow += flow;
	}
	return maxflow;
}

int grid[4000][4000];

void addV(int s, int t) {
	edge *ed = &e[nume++];
	ed->from = &v[s];
	ed->to = &v[t];
	ed->used = 0;
	ed->mi = 0;
	ed->ma = 1;

	v[s].e.push_back(ed);
	v[t].e.push_back(ed);
}

int main() {
	int w, h, b;
	int c;
	cin >> c;
	for (int cc = 1; cc <= c; cc++) {
		cin >> w >> h >> b;
		for (int i = 0; i < MAX_VERTICES; i++) {
			v[i].e.clear();
		}
		nume = 0;
		memset(grid, 0, sizeof grid);
		numv = 2 + w*h*2;
		for (int i = 0; i < b; i++) {
			int x0, y0, x1, y1;
			cin >> x0 >> y0 >> x1 >> y1;
			for (int x = x0; x <= x1; x++) {
				for (int y = y0; y <= y1; y++) {
					grid[x][y] = 1;
				}
			}
		}

		for (int i = 0; i < w; i++) {
			for (int j = 0; j < h; j++) {
				if (grid[i][j]) continue;
				if (i != 0 && !grid[i-1][j]) {
					addV(w*h + j*w+i, j*w+i-1);
				}
				if (j != 0 && !grid[i][j-1]) {
					addV(w*h + j*w+i, (j-1)*w+i);
				}
				if (i != w-1 && !grid[i+1][j]) {
					addV(w*h + j*w+i, j*w+i+1);
				}
				if (j != h-1 && !grid[i][j+1]) {
					addV(w*h + j*w+i, (j+1)*w+i);
				}
				addV(j*w+i, w*h + j*w+i);
			}
		}
		int SOURCE = 2*w*h+1;
		int SINK = 2*w*h;
		for (int i = 0; i < w; i++) {
			if (grid[i][0]) continue;
			addV(SOURCE, i);
		}
		for (int i = 0; i < w; i++) {
			if (grid[i][h-1]) continue;
			addV(w*h + w*(h-1)+i, SINK);
		}

		printf("Case #%d: %d\n", cc, MaxFlow(&v[SOURCE], &v[SINK]));
	}
	return 0;
}
