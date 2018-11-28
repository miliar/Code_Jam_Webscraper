#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <iomanip>
#include <sstream>

using namespace std;

void Solve(vector<vector<int>> &str, int i, vector<bool> &en, vector<bool> &fr, vector<bool> &both, int &min)
{
  if(i == str.size())
  {
    int count = 0;
    for(int i=0; i<both.size();i++)
      if(both[i])
        count++;

    if(min > count)
      min = count;
  }
  else
  {
    vector<bool> ten=en, tfr=fr, tboth=both;

    for(int j=0; j<str[i].size(); j++)
    {
      en[str[i][j]]=1;
      if(fr[str[i][j]] == 1)
        both[str[i][j]]=1;
    }

    Solve(str,i+1,en,fr,both, min);

    en=ten;
    both=tboth;
    fr=tfr;

    for(int j=0; j<str[i].size(); j++)
    {
      fr[str[i][j]]=1;
      if(en[str[i][j]] == 1)
        both[str[i][j]]=1;
    }

    Solve(str,i+1,en,fr,both, min);
  }
}

int main()
{
  int T;

  //ifstream in("test.in");
  //ofstream out("test.out");

  ifstream in("C-small-attempt2.in");
  ofstream out("C-small-attempt2.out");

  //ifstream in("C-large.in");
  //ofstream out("C-large.out");
  
  in >> T;

  for(int testCase=0; testCase<T; ++testCase)
  {
    int solve = 0; 
    int n;

    in >> n;

    map<string,int> m;
    vector<vector<int>> str(n);
    int num = 1;

    string empty;
    getline(in,empty);

    for(int i=0; i<n; i++)
    {
      string s;
      getline(in,s);

      istringstream iss(s);

      while(!iss.eof())
      {
        string ss;
        iss >> ss;

        auto it = m.find(ss);

        if(it != m.end())
          str[i].push_back(it->second);
        else
        {
          m[ss]=num;
          str[i].push_back(num);
          num++;
        }
      }
    }

    solve = m.size();

    vector<bool> en(solve+1), fr(solve+1), both(solve+1);

    for(int j=0; j<str[0].size(); j++)
      en[str[0][j]]=1;

    for(int j=0; j<str[1].size(); j++)
    {
      fr[str[1][j]]=1;
      if(en[str[1][j]]==1)
        both[str[1][j]]=1;
    }

    Solve(str,2,en,fr,both,solve);

    out << "Case #"<<testCase+1<<": ";

    out << solve << endl;
  }

  return 0;
}