#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <list>
#include <cmath>

using namespace std;

int solve(const vector<string>& words)
{
  vector<vector<int> > reps(words.size(), vector<int>());
  vector<int> means;
  string last_base;
  
  for (int j = 0; j < words.size(); ++j)
  {
    string word = words[j];
    string base;
    int rep = 1;
    for (int k = 1; k < word.length(); ++k)
    {
      if (word[k-1] != word[k])
      {
	reps[j].push_back(rep);
	rep = 0;
	base += word[k-1];
      }
      else
	++rep;
    }
    base += word.back();
    reps[j].push_back(rep);
    if (!last_base.empty() && base != last_base)
      return -1;
    last_base = base;
  }
  for (int j = 0; j < reps[0].size(); ++j)
  {
    int sum = 0;
    for (int k = 0; k < reps.size(); ++k)
      sum += reps[k][j];
    means.push_back(round(((double)sum)/words.size()));
  }
  
  int res = 0;
  
  for (int j = 0; j < reps.size(); ++j)
  {
    for (int k = 0; k < reps[j].size(); ++k)
      res += abs(means[k]-reps[j][k]);
  }
  
  return res;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    int N;
    cin >> N;
    vector<string> words;
    copy_n(istream_iterator<string>(cin), N, back_inserter(words));
    
    cout << "Case #" << i << ": "; 
    
    int res = solve(words);
    
    if (res == -1)
      cout << "Fegla Won" << endl;
    else
      cout << res << endl;
  }
  return 0;
}
