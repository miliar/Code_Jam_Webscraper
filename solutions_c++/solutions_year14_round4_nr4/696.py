#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

int max_num = 0;
int num_ways = 0;

int get_num_substrings(vector<string>& S, int N, vector<int>& assign)
{
  vector<int> all_covered(N,0);
  for (int i=0; i<assign.size(); i++)
    all_covered[assign[i]]++;
  for (int i=0; i<N; i++)
    if (all_covered[i] == 0)
      return 0;
  int total = N;
  for (int i=0; i<N; i++)
  {
    set<string> stringset;
    for (int j=0; j<S.size(); j++)
      if (assign[j] == i)
        for (int k=1; k<=S[j].size(); k++)
          stringset.insert(S[j].substr(0,k));
    total += stringset.size();
  }
  if (total == max_num)
  {
    num_ways++;
  }
  if (total > max_num)
  {
    max_num = total;
    num_ways = 1;
  }
  return total;
}

int dfs(vector<string>& S, int M, int N, vector<int>& assign)
{
  if (M == 0)
    return get_num_substrings(S, N, assign);
  int worst_result = 0;
  if (assign[M-1] == -1)
  {
    for (int j=0; j<N; j++)
    {
      assign[M-1] = j;
      int cur_result = dfs(S, M-1, N, assign);
      if (cur_result > worst_result)
        worst_result = cur_result;
    }
    assign[M-1] = -1;
  }
  return worst_result;
}

int main()
{
  int Nprob;
  cin >> Nprob;
  string s;
  getline(cin, s);
  for (int np=0; np<Nprob; np++)
  {
    max_num = 0;
    num_ways = 0;
    int M, N;
    cin >> M >> N;
    vector<string> S;
    vector<int> assign;
    for (int i=0; i<M; i++)
    {
      string tmp;
      cin >> tmp;
      S.push_back(tmp);
      assign.push_back(-1);
    }
    dfs(S, M, N, assign);
    cout << "Case #" << np+1 <<": " << max_num << " " << num_ways << "\n";
  }
}
