#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

vvi edges;
vvi redges;

bool seen[1000];
int comp[1000];

vi res1;
void topo1(int node)
{
  if (seen[node])
    return;
  seen[node] = true;
  
  for (auto x : edges[node])
    topo1(x);
  
  res1.push_back(node);
}

void topo2(int node, int c)
{
  if (seen[node])
    return;
  seen[node] = true;
  
  for (auto x : redges[node])
    topo2(x, c);
  
  comp[node] = c;
}

int topo3(int node, int forbidden)
{
  int best = 0;
  for (auto x : redges[node])
    if (x != forbidden)
      best = max(topo3(x, forbidden), best);
  return best+1;
}

void main2()
{
  int N; cin >> N;
  edges.clear();
  redges.clear();
  for (int i=0; i<N; i++)
  {
    int bff; cin >> bff;
    edges.push_back(vi(1, bff-1));
    redges.push_back(vi());
  }
  
  for (int i=0; i<N; i++)
    for (auto x : edges[i])
      redges[x].push_back(i);
  
  res1.clear();
  for (int i=0; i<N; i++)
    seen[i] = false;
  for (int i=0; i<N; i++)
    topo1(i);
  
  int nb_comp = 0;
  for (int i=0; i<N; i++)
  {
    seen[i] = false;
    comp[i] = -1;
  }
  for (int i=0; i<N; i++)
  {
    if (comp[res1[N-1-i]] != -1) continue;
    topo2(res1[N-1-i], nb_comp++);
  }
  
  if (nb_comp == 1)
  {
    cout << N << endl;
    return;
  }
  
  vvi component(nb_comp);
  for (int i=0; i<N; i++)
    component[comp[i]].push_back(i);
  
  int result = 0;
  for (int c=0; c<nb_comp; c++)
  if (component[c].size() == 2)
  {
    result += topo3(component[c][0], component[c][1]);
    result += topo3(component[c][1], component[c][0]);
  }
  
  for (int c=0; c<nb_comp; c++)
    result = max(result, (int)component[c].size());
  
  cout << result << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
