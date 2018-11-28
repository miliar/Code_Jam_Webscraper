#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <queue>
using namespace std;

const int INFINI = 1000000000;

int N;

vector<string> mots[200];
map<string, list<int> > id;

vector<vector<int> > noeud;
vector<pair<int, int> > arete;

void main2()
{
  id.clear();
  noeud.clear();
  cin >> N;
  cin.ignore();
  
  for (int i=0; i<N; i++)
  {
    mots[i].clear();
    string line, s;
    getline(cin, line);
    istringstream l(line);
    while (l >> s)
      id[s].push_back(i);
    
    noeud.push_back(vector<int>());
  }
  
  for (auto x : id)
  {
    int tmp = noeud.size();
    noeud.push_back(vector<int>());
    noeud.push_back(vector<int>());
    
    int tmp2 = arete.size();
    arete.push_back(make_pair(tmp+1, 1));
    arete.push_back(make_pair(tmp, 0));
    
    noeud[tmp].push_back(tmp2);
    noeud[tmp+1].push_back(tmp2+1);
    
    for (auto i : x.second)
    {
      tmp2 = arete.size();
      arete.push_back(make_pair(tmp, INFINI));
      arete.push_back(make_pair(i, 0));
      noeud[i].push_back(tmp2);
      noeud[tmp].push_back(tmp2+1);
      
      tmp2 = arete.size();
      arete.push_back(make_pair(i, INFINI));
      arete.push_back(make_pair(tmp+1, 0));
      noeud[tmp+1].push_back(tmp2);
      noeud[i].push_back(tmp2+1);
    }
  }
  
  int res = 0;
  int S = 0;
  int T = 1;
  int taille = noeud.size();
  int dist[taille];
  int prec[taille];
  
  while (true)
  {
    for (int i=0; i<taille; i++)
      dist[i] = 0;
    
    dist[S] = INFINI;
    
    priority_queue<pair<int, int> > encours;
    encours.push(make_pair(INFINI, S));
    
    while (!encours.empty())
    {
      int act = encours.top().second;
      encours.pop();
      
      for (int i=0; i<(int)noeud[act].size(); i++)
      {
        int j = arete[noeud[act][i]].first;
        int p = arete[noeud[act][i]].second;
        if (dist[j] < min(dist[act], p))
        {
          dist[j] = min(dist[act], p);
          prec[j] = noeud[act][i];
          encours.push(make_pair(dist[j], j));
        }
      }
    }
    
    if (dist[T] == 0) break;
    
    res += dist[T];
    
    int act = T;
    while (act != S)
    {
      int next = arete[prec[act]^1].first;
      arete[prec[act]].second -= dist[T];
      arete[prec[act]^1].second += dist[T];
      act = next;
    }
  }
  
  cout << res << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int i=1; i<=T; i++)
  {
    cout << "Case #" << i << ": ";
    main2();
  }
}
