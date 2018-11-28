#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cstdio>

using namespace std;

// Network Flow
// Using Edmonds-Karp algorithm (Ford-Fulkersson with BFS)
// Complexity: O(V*E^2)

struct TEdge
{
	int src,dest,flow,cap;
	TEdge(int a, int b, int c) : src(a),dest(b),flow(0),cap(c) {};
};

struct TVertex
{
	vector<TEdge*> e;
	int slack;
	TEdge *used;
};

vector<TVertex> vert;

void addedge(int src, int dest, int cap)
{
	if (src==dest) return;
	TEdge* e=new TEdge(src,dest,cap);
	vert[src].e.push_back(e);
	vert[dest].e.push_back(e);
}

bool find_augmenting_path(int source, int sink)
{
	int q[vert.size()],head=0,tail=0;
	for(int i=0;i<vert.size();i++)
		vert[i].used=0;
	vert[source].slack=1<<30;
	q[tail++]=source;
	while ((head<tail) && !vert[sink].used) {
		int x=q[head++];
		for(int i=0;i<vert[x].e.size();i++) {
			TEdge *e=vert[x].e[i];
			int y=e->src+e->dest-x;
			if (vert[y].used) continue;
			int s=e->src==x?(e->cap-e->flow):e->flow;
			if (s) {
				vert[y].slack=min(vert[x].slack,s);
				vert[y].used=e;
				q[tail++]=y;
			}
		}
	}
	return vert[sink].used;
};

void use_path(int source, int sink)
{
	int x=sink,slack=vert[sink].slack;
	while (x!=source) {
		//cout << x << " <- ";
		if (vert[x].used->dest==x) {
			vert[x].used->flow+=slack;
			x=vert[x].used->src;
		} else {
			vert[x].used->flow-=slack;
			x=vert[x].used->dest;
		}
	}
	//cout << x << "   slack = " << slack << endl;
}

int find_max_flow(int source, int sink)
{
	while (find_augmenting_path(source,sink))
		use_path(source,sink);
	int flow=0;
	for(int i=0;i<vert[source].e.size();i++)
		if (vert[source].e[i]->src==source)
			flow+=vert[source].e[i]->flow;
	return flow;
}

vector<TEdge*> find_min_cut(void)
{
	vector<TEdge*> mincut;
	for(int i=0;i<vert.size();i++) {
		if (!vert[i].used) continue;
		for(int j=0;j<vert[i].e.size();j++) {
			TEdge *e=vert[i].e[j];
			if (e->src!=i || vert[e->dest].used) continue;
			mincut.push_back(e);
		}
	}
	return mincut;
}

void showgraph(void)
{
	for(int i=0;i<vert.size();i++) {
		cout << "Vertex " << i << ":" << endl;
		for(int j=0;j<vert[i].e.size();j++) {
			TEdge *e=vert[i].e[j];
			if (e->src!=i) continue;
			cout << " " << e->src << " -> " << e->dest << ": "
				<< e->flow << " (" << e->cap << ")" << endl;
		}
	}
}

bool map[1000][1000];

int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};

void solve() {
	int xsize,ysize,n;
	cin >> xsize >> ysize >> n;
	memset(map,0,sizeof(map));
	for(int i=0;i<n;i++) {
		int x0,y0,x1,y1;
		cin >> x0 >> y0 >> x1 >> y1;
		for(int x=x0;x<=x1;x++)
			for(int y=y0;y<=y1;y++)
				map[y][x]=true;
	}
	vert.clear();
	vert.resize(xsize*ysize*2+2);
	int SRC = xsize*ysize*2, SINK = SRC + 1;

	for (int y = 0; y < ysize; y++) {
        for (int x = 0; x < xsize; x++) {
            if (!map[y][x]) {
            	addedge((y * xsize + x) * 2, (y * xsize + x) * 2 + 1, 1); // Flow through cell
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i], ny = y+dy[i];
                    if (nx >= 0 && ny >= 0 && nx < xsize && ny < ysize && !map[ny][nx]) {
                        addedge((y * xsize +x) * 2 + 1, (ny * xsize + nx) * 2, 1);
                    }
                }
            }
        }
    }

    for (int x = 0; x < xsize; x++) {
        if (!map[0][x]) {
            addedge(SRC, x * 2, 1);
        }
        if (!map[ysize-1][x]) {
            addedge(((ysize - 1) * xsize + x) * 2 + 1, SINK, 1);
        }
    }


    int flow = find_max_flow(SRC, SINK);
    //showgraph();
    cout << flow << endl;
}

int main(void)
{
	int n,source,sink,a,b,c;

	cin >> n;

	for(int i=0;i<n;i++) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
	return 0;
}

