#include <iostream>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

int M, N;
string S[8];

int max_nodes, freq;
void search(int set_id[], int start)
{

  if (start >= M) {
    int nodes = 0;
    for (int i = 0; i < N; i++) {
      set<string> suffix;
      for (int j = 0; j < M; j++) {
	if (set_id[j] != i) continue;
	for (int k = 0; k <= S[j].length(); k++) {
	  suffix.insert(S[j].substr(0, k));
	}
      }
      nodes += suffix.size();
    }

    if (nodes > max_nodes) {
      max_nodes = nodes;
      freq = 1;
    } else if (nodes == max_nodes) {
      freq++;
    }
    
    return;
  }    

  for (int i = 0; i < N; i++) {
    set_id[start] = i;
    search(set_id, start+1);
  }
}

void solve()
{
  cin >> M >> N;

  for (int i = 0; i < M; i++) {
    cin >> S[i];
  }

  max_nodes = 0;
  freq = 0;
  
  int set_id[8];
  search(set_id, 0);
  cout << max_nodes << ' ' << freq << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
