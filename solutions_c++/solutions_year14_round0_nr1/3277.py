#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#include<sstream>

using namespace std;

void readIntoGrid(vector<vector<int> >& grid)
{
  for(int i = 0; i < grid.size(); i++)
  {
    for(int j = 0; j < grid[i].size(); j++)
    {
      cin >> grid[i][j];
    }
  }
}

string integer2string(int in)
{
  stringstream ss;
  ss << in;
  return ss.str();
}

string evaluate(vector<vector<int> >& grid1, int ans1, vector<vector<int> >& grid2, int ans2)
{
  set<int> possibleCards1(grid1[ans1].begin(), grid1[ans1].end());
  set<int> possibleCards2(grid2[ans2].begin(), grid2[ans2].end());
  set<int> intersect;

  set_intersection (possibleCards1.begin(), possibleCards1.end(),
                    possibleCards2.begin(), possibleCards2.end(),
                    std::inserter(intersect,intersect.begin()));
  
  if (intersect.size() == 1) return integer2string(*(intersect.begin()));
  else if (intersect.size() > 1) return "Bad magician!";
  else return "Volunteer cheated!";
}


int main(void)
{
  int t, ans1, ans2, card;
  vector<vector<int> > grid1(4, vector<int>(4, 0));
  vector<vector<int> > grid2(4, vector<int>(4, 0));
  
  cin >> t;

  for(int i = 1; i <= t; i++)
  {
    cin >> ans1;
    readIntoGrid(grid1);
    cin >> ans2;
    readIntoGrid(grid2);
    cout  <<"Case #" << i << ": " << evaluate(grid1, ans1 - 1, grid2, ans2 - 1) 
          << endl;
  }

  return 0;
}
