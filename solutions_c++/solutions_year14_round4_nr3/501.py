#include <iostream>
#include <cstring>

#define W 105
#define H 505

using namespace std;

#define INF 0x33333333

const int MAX_N = 200005;     // max no. of node
const int MAX_M = 4000000;    // max no. of edge

const int SIZE = MAX_N * 10;

struct Node {
  int id, c;               // capacity of vertex [vertex constraint]
};

typedef struct Edge {
  int u, v;
  int c;
  struct Edge *rev, *next;
} * edge_pointer;

int level[MAX_N], queue[SIZE];
edge_pointer head[MAX_N], edge_tail;

Edge edge[MAX_M];

int node_num, source, sink;

/***   Useful functions prototype   ***/

void init(int num_of_node);
void add_edge(int u, int v, int c);
Node make_node(int id, int c);
int max_flow(int s, int t);

/***   Useful functions prototype   ***/

/**-----------------------------------------------------------**/
/*            Here below are implementation details            */
/**-----------------------------------------------------------**/

inline int min(int a, int b) {
  return a < b ? a : b;
}

void init(int num_of_node) {
  node_num = num_of_node;
  edge_tail = edge;
  for (int i = 0; i < node_num; i++)
    head[i] = NULL;
}

void add_edge(int u, int v, int c) {
  edge_pointer edge_ptr1;
  edge_pointer edge_ptr2;

  edge_ptr1 = edge_tail++;
  edge_ptr2 = edge_tail++;

  edge_ptr1->u = u;
  edge_ptr1->v = v;
  edge_ptr1->c = c;
  edge_ptr1->rev = edge_ptr2;
  edge_ptr1->next = head[u];
  head[u] = edge_ptr1;

  edge_ptr2->u = v;
  edge_ptr2->v = u;
  edge_ptr2->c = 0;
  edge_ptr2->rev = edge_ptr1;
  edge_ptr2->next = head[v];
  head[v] = edge_ptr2;
}

bool BFS() {
  edge_pointer edge_ptr;
  int node_id, *qf, *qb;

  memset(level, 0xff, node_num * sizeof(int));
  level[source] = 0;
  qf = qb = queue;
  *qb++ = source;

  while (qf < qb) {
    node_id = *qf++;
    for (edge_ptr = head[node_id]; edge_ptr != NULL; edge_ptr = edge_ptr->next)
      if (level[edge_ptr->v] == -1 && edge_ptr->c > 0) {
        level[edge_ptr->v] = level[node_id] + 1;
        if (edge_ptr->v == sink)
          return true;
        *qb++ = edge_ptr->v;
      }
  }

  return false;
}

int DFS(int node_id, int min_cap) {
  int flow;
  edge_pointer edge_ptr;

  if (node_id == sink)
    return min_cap;

  for (edge_ptr = head[node_id]; edge_ptr != NULL; edge_ptr = edge_ptr->next)
    if (edge_ptr->c > 0 && level[edge_ptr->v] == level[node_id] + 1)
      if (flow = DFS(edge_ptr->v, min(min_cap, edge_ptr->c))) {
        edge_ptr->c -= flow;
        edge_ptr->rev->c += flow;
        return flow;
      }

  level[node_id] = -1;

  return 0;
}

int max_flow(int s, int t) {
  int f, flow;

  source = s;
  sink = t;
  flow = 0;

  while (BFS())
    while (f = DFS(source, (int) INF))
      flow += f;

  return flow;
}

/**-----------------------------------------------------------**/
/*            Here above are implementation details            */
/**-----------------------------------------------------------**/

bool grid[W][H];
const int mx[] = {1, -1, 0, 0};
const int my[] = {0, 0, 1, -1};

int get_innode_id(int x, int y) {
	return 2 * (505 * x + y) + 1;
}

int get_outnode_id(int x, int y) {
	return 2 * (505 * x + y) + 2;
}

void init() {
	init(200005);
	memset(grid, false, sizeof grid);
}

void solve(int case_no) {
	int w, h, b, ans, src_node, dest_node;

	init();

	cin >> w >> h >> b;
	while (b--) {
		int x0, y0, x1, y1;
		cin >> x0 >> y0 >> x1 >> y1;
		for (int x = x0; x <= x1; x++)
			for (int y = y0; y <= y1; y++)
				grid[x][y] = true;
	}

	for (int x = 0; x < w; x++)
		for (int y = 0; y < h; y++) {
			if (grid[x][y])
				continue;
			src_node = get_outnode_id(x, y);
			for (int dir = 0; dir < 4; dir++) {
				int nx = x + mx[dir];
				int ny = y + my[dir];
				if (nx < 0 || ny < 0 || nx >= w || ny >= h || grid[nx][ny])
					continue;
				dest_node = get_innode_id(nx, ny);
				add_edge(src_node, dest_node, 1);
			}
		}

    // build internal edge
    for (int x = 0; x < w; x++)
        for (int y = 0; y < h; y++)
            if (!grid[x][y]) {
                src_node = get_innode_id(x, y);
                dest_node = get_outnode_id(x, y);
                add_edge(src_node, dest_node, 1);
            }

	src_node = 0;
    for (int x = 0; x < w; x++)
        if (!grid[x][0]) {
            dest_node = get_innode_id(x, 0);
            add_edge(src_node, dest_node, 1);
        }

    dest_node = 200004;
    for (int x = 0; x < w; x++)
        if (!grid[x][h-1]) {
            src_node = get_outnode_id(x, h - 1);
            add_edge(src_node, dest_node, 1);
        }

	ans = max_flow(0, 200004);
	cout << "Case #" << case_no << ": " << ans << endl;
}

int main(int argc, char* argv[]) {
	int t;

	ios::sync_with_stdio(0);

	cin >> t;
	for (int case_no = 1; case_no <= t; case_no++)
		solve(case_no);

	return 0;
}