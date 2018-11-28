#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <queue>
#include <algorithm>
using namespace std;


int main() {
  int t;
  cin >> t;
  for(int caseno = 1; caseno <= t; caseno++) {
    map<string, int> dist;
    queue<string> q;
    string start, end = "";
    cin >> start;
    dist[start] = 0;
    for(int i = 0; i < (int)start.size(); i++) {
      end += "+";
    }
    q.push(start);
    while(!q.empty()) {
      string cur = q.front();
      q.pop();
      for(int i = 1; i <= (int)cur.size(); i++) {
	string neigh = cur;
	reverse(neigh.begin(), neigh.begin()+i);
	for(int j = 0; j < i; j++)
	  neigh[j] = (neigh[j]=='+')?'-':'+';
	if(dist.find(neigh) == dist.end()) {
	  dist[neigh] = dist[cur]+1;
	  q.push(neigh);
	  if(neigh == end) goto here;
	}
      }
    }
  here:
    cout << "Case #" << caseno << ": " << dist[end] << endl;
  }
  return 0;
}
