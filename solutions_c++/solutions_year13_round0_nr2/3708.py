#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i!=(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define dbg(x)   (cout << #x << ":" << (x) << "\t") 
#define dbge(x) (cout << #x << ":" << (x) << "\n") 
#define all(c) c.begin(), c.end() 
#define cpresent(container, element) (find(all(container),element) != container.end())

int gridmaxheight(vector <vector<int> > &grid){
  int maxheight = 0;
  int minheight = 100;
  for(int i=0; i< grid.size(); i++){
    for(int j=0; j< grid[0].size(); j++ ){
      if(grid[i][j]>maxheight)
        maxheight = grid[i][j];
    }
  }

  return maxheight;
}


int main() {
  int count, h, w, num, counter = 0;
  cin >> count;

  while(counter < count)
  {
    cin >> h >> w;

    vector <vector<int> > grid(h);

    for(int j=0;j<h;j++)
    {
      for(int l=0;l<w;l++)
      {
        cin >> num;
        grid[j].push_back(num);
      }
    }


    int gridmax = gridmaxheight(grid);

    bool possible = true;

    for(int i=0;i<h;i++)
    {
      for(int j=0;j<w;j++)
      {
        bool row_possible = true, col_possible = true;
        if(grid[i][j] < gridmax)
        {
          for(int l=0;l<grid.size();l++)
          {
            if(grid[l][j] > grid[i][j])
            {
//             cout << "Setting column check false for (" << i << ","<< j<< ") " << grid[i][j] << endl;
              col_possible = false;  
              break;
            }
          }

          for(int l=0;l<grid[0].size();l++)
          {
            if(grid[i][l] > grid[i][j])
            {
//              cout << "Setting row check false for (" << i << ","<< j<< ") " << grid[i][j] << endl;
              row_possible = false;  
              break;
            }
          }
        }

        if(!row_possible && !col_possible)
        {        
     //     cout << "Row possible = " << row_possible << endl;
      //    cout << "Col possible = " << col_possible << endl;
        }

        possible = row_possible || col_possible;
        if(!possible) {
          break;  
        }
      }

      if(!possible)
        break;
    }

    if(possible)
      cout << "Case #" << (counter+1) << ": YES" << endl;
    else
      cout << "Case #" << (counter+1) << ": NO" << endl;

  	counter++;
  }
  return 0;
}
