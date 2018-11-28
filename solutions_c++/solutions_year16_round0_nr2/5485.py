#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;

//use dijkstra

map<string,int> distances;
set<string> visited;
set<string> frontier;

int get_distance(string s)
{
  auto it = distances.find(s);
  if (it == distances.end())  {return 10000000;}
  else  {return it->second;}
}
void set_distance(string s, int d)
{
  distances[s] = d;
}

string flip_first(string s, int n)
{
  reverse(s.begin(), s.begin()+n);
  replace(s.begin(), s.begin()+n, '+', 'p');
  replace(s.begin(), s.begin()+n, '-', '+');
  replace(s.begin(), s.begin()+n, 'p', '-');
  return s;
}

bool is_visited(string s)
{
  return (visited.find(s) != visited.end());
}

void add_visited(string s)
{
  visited.insert(s);
}

int shortest_path(string start, string end)
{
  frontier.insert(start);
  string current = start;
  int thisDistance = 0;
  
  while (current != end)
  {
    //cout << "current: " << current << " (" << thisDistance << ")" << endl;
    for (int i=1; i <= current.length(); i++)
    {
      string nei = flip_first(current, i);
      //cout << "i: " << i << ", nei: " << nei << endl;
      if (!is_visited(nei))
      {
        int newDistance = min(get_distance(nei), 1+thisDistance);
        set_distance(nei, newDistance);
        frontier.insert(nei);
      }
    }
    add_visited(current);
    frontier.erase(current);

    int minDistance = 10000000;
    
    for (string s : frontier)
    {
      int d = get_distance(s);
      //cout << "s: " << s << ", d: " << d << endl;
      if (d < minDistance)
      {
        minDistance = d;
        current = s;
      }
    }
    thisDistance = minDistance;
  }
  return thisDistance;
}

void tick()
{
  string start;
  cin >> start;
  string end = start;
  fill(end.begin(), end.end(), '+');

  visited.clear();
  distances.clear();
  frontier.clear();
  cout << shortest_path(start, end) << endl;
}

int main()
{
  int bigN;
  cin >> bigN;
  for (int i=0; i < bigN; i++)
  {
    cout << "Case #" << (i+1) << ": ";
    tick();
  }
  return 0;
}
