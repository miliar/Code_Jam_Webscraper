#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<pii> vpii;
typedef vector<vi> vvi;
typedef vector<vi> vvi;

void main2()
{
  int N; cin >> N;
  
  set<string> first, second;
  vector<pair<string, string> > topics;
  for (int i=0; i<N; i++)
  {
    pair<string, string> topic;
    cin >> topic.first >> topic.second;
    first.insert(topic.first);
    second.insert(topic.second);
    topics.push_back(topic);
  }
  
  int res = 0;
  for (int i=0; i<(1<<N); i++)
  {
    int nb = 0;
    set<string> a, b;
    for (int j=0; j<N; j++)
    if (1&(i>>j))
    {
      a.insert(topics[j].first);
      b.insert(topics[j].second);
    }
    else
      nb++;
    if (a.size() == first.size() && b.size() == second.size())
      res = max(res, nb);
  }
  
  cout << res << endl;
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
