#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;

int N;
int M;

int zips[50];
vector< vector<int> > edges;

void leggi()
{
    cin >> N >> M;
    for (int i = 0; i < N; i += 1)
    {
        cin >> zips[i];
    }
    edges.clear();
    edges.assign(N, vector<int>());
    int u, v;
    for (int i = 0; i < M; i += 1)
    {
        cin >> u >> v;
        edges[u-1].push_back(v-1);
        edges[v-1].push_back(u-1);
    }
}




struct node {
    node *p; // parent
    int rank;
    int top;
};

void link(node* x, node* y)
{
    if (x->rank > y->rank)
    {
        y->p = x;
        x->top = min(x->top, y->top);
    }
    else
    {
        x->p = y;
        y->top = min(x->top, y->top);
        if (x->rank == y->rank)
        {
            y->rank += 1;
        }
    }
}

node* find(node* x)
{
    if (x != x->p)
    {
        x->p = find(x->p);
    }
    return x->p;
}

void unione(node* x, node* y)
{
    x = find(x);
    y = find(y);
    if (x != y)
    {
        link(x, y);
    }
}






bool visited[50];
int depth[50];
node part[50];
vector<int> pila;





void reset_part()
{
    for (int i = 0; i < N; i += 1)
    {
        part[i].p = part+i;
        part[i].rank = 1;
        part[i].top = 1000000000;
    }
}

int choose_start()
{
    int min_idx = 0;
    int min_val = zips[0];
    for (int i = 1; i < N; i += 1)
    {
        if (min_val > zips[i])
        {
            min_idx = i;
            min_val = zips[i];
        }
    }
    return min_idx;
}

pair<int,int> choose_next(int min_height)
{
    int parent = -1;
    int min_idx = -1;
    int min_val = 1000000000;
    for (int i = pila.size() - 1; i >= min_height; i -= 1)
    {
        int u = pila[i];
        for (int j = 0; j < edges[u].size(); j += 1)
        {
            int v = edges[u][j];
            if (!visited[v])
            {
                if (min_val > zips[v])
                {
                    min_idx = v;
                    min_val = zips[v];
                    parent = u;
                }
            }
        }
    }
    return make_pair(parent, min_idx);
}

void stampa_zip(int idx)
{
    int v = zips[idx];
    cout << v;
}

void elabora()
{
    memset(visited, 0, 50*sizeof(bool));
    memset(depth, -1, 50*sizeof(int));
    pila.clear();

    int idx = choose_start();
    visited[idx] = true;
    depth[idx] = 0;
    pila.push_back(idx);
    stampa_zip(idx);

    //cout << "start from " << idx+1 << endl;

    for (int foo = 1; foo < N; foo += 1)
    {
        reset_part();
        for (int u = 0; u < N; u += 1)
        {
            if (!visited[u])
            {
                for (int j = 0; j < edges[u].size(); j += 1)
                {
                    int v = edges[u][j];
                    if (visited[v] && depth[v] >= 0)
                    {
                        node* a = find(part+u);
                        a->top = min(a->top, depth[v]);
                    }
                    else if (!visited[v])
                    {
                        unione(part+u, part+v);
                    }
                }
            }
        }
        int min_height = 0;
        for (int u = 0; u < N; u += 1)
        {
            if (!visited[u])
            {
                //cout << u+1 << " is unvisited, belongs to partition " << find(part+u) << " which mins to " << find(part+u)->top << endl;
                min_height = max(min_height, find(part+u)->top);
            }
        }

        //cout << "stack is ";
        //for (int i = 0; i < pila.size(); i += 1)
        //{
            //cout << pila[i] << " ";
        //}
        //cout << endl;

        //cout << "min height is " << min_height << endl;

        pair<int,int> b = choose_next(min_height);
        //cout << "I chose to continue to " << b.second+1 << " (from " << b.first+1 << ")" << endl;
        while (pila.back() != b.first)
        {
            depth[pila.back()] = -1;
            pila.pop_back();
        }
        visited[b.second] = true;
        depth[b.second] = pila.size();
        pila.push_back(b.second);
        stampa_zip(b.second);
    }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i += 1)
    {
        leggi();
        cout << "Case #" << i << ": ";
        elabora();
        cout << "\n";
    }
}
