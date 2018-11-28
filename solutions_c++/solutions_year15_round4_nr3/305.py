#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

const int infinity = 1e9 + 9;

int N;
vector<string> S[209];
vector<int> I[209];
string temp;
string s;

set<string> allWords;
bool ENG[4009];
bool FRE[4009];

vector<bool> bits(int m, int count)
{
  vector<bool> ans;
  for (int i = 0; i < count; ++i)
  {
    ans.push_back(m % 2 == 1);
    m /= 2;
  }
  return ans;
}

int main()
{
  int T;
  cin >> T;
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // init & input
    allWords.clear();
    cin >> N;
    getline(cin, temp);
    for (int n = 0; n < N; ++n)
    {
      S[n].clear();
      getline(cin, s);
      stringstream myss(s);
      while (getline(myss, temp, ' '))
      {
        S[n].push_back(temp);
        allWords.insert(temp);
      }
    }
    int wordCount = allWords.size();
    
    // map words to numbers
    map<string, int> wordInd;
    int ind = 0;
    for (set<string>::iterator it = allWords.begin(); it != allWords.end(); it++)
    {
      wordInd[*it] = ind;
      ind++;
      //cout << "mapping " << *it << " to " << ind << endl;
    }
    
    for (int n = 0; n < N; ++n) {
      I[n].clear();
      for (unsigned int i = 0; i < S[n].size(); ++i)
        I[n].push_back(wordInd[S[n][i]]);
    }
    
    /*
    for (int n = 0; n < N; ++n)
    {
      for (unsigned int i = 0; i < S[n].size(); ++i)
        cout << S[n][i] << " ; ";
      cout << endl;
    }
    */
    
    int best = infinity;
    for (int mask = 0; mask < (1 << (N - 2)); ++mask)
    {
      //cout << "mask = " << mask << endl;
      
      for (int i = 0; i < wordCount; ++i)
      {
        ENG[i] = false;
        FRE[i] = false;
      }
      for (unsigned int i = 0; i < I[0].size(); ++i)
        ENG[I[0][i]] = true;
      for (unsigned int i = 0; i < I[1].size(); ++i)
        FRE[I[1][i]] = true;
      
      int x = mask;
      for (int k = 2; k < N; ++k)
      {
        if (x % 2 == 0) // ENG
        {
          for (unsigned int i = 0; i < I[k].size(); ++i)
            ENG[I[k][i]] = true;
        }
        else // FRE
        {
          for (unsigned int i = 0; i < I[k].size(); ++i)
            FRE[I[k][i]] = true;
        }
        x /= 2;
      }
      
      int intersection = 0;
      for (int i = 0; i < wordCount; ++i)
        if (ENG[i] && FRE[i])
          intersection++;
      //cout << intersection << endl;
      best = min(best, intersection);
    }
    
    // output
    cout << "Case #" << Ti << ": " << best << endl;
  }
  return 0;
}
