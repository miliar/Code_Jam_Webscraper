#include<cstdio>
#include<iostream>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

int h[1100][1100][4];
int lawn[1100][1100];
int main()
{
  int t;
  int m, n;
  cin >> t;
  for(int cnt = 1; cnt <= t; cnt++)
  {
    cin >> n >> m;
    bool ans = true;
    for(int i = 0; i < n; i++)
    {
      for(int j = 0; j < m; j++)
      {
        cin >> lawn[i][j];
      }
    }
    for(int i = 0; i < n; i++)
    {
      for(int j = 0; j < m; j++)
      {
        if(j == 0)
        {
          h[i][j][0] = lawn[i][j];
          h[i][m - j - 1][1] = lawn[i][m - j - 1];
        }
        else
        {
          h[i][j][0] = max(h[i][j - 1][0], lawn[i][j - 1]);
          h[i][m - j - 1][1] = max(h[i][m - j][1], lawn[i][m - j]);
        }
        if(i == 0)
        {
          h[i][j][2] = lawn[i][j];
          h[n - i - 1][j][3] = lawn[n - i - 1][j];
        }
        else
        {
          h[i][j][2] = max(h[i - i][j][2], lawn[n - i][j]);
          h[n - i - 1][j][3] = max(h[n - i][j][3], lawn[n - i - 1][j]);
        }
      }
    }
    //for(int s = 0; s < 4; s++)
    {
    for(int i = 0; i < n; i++)
    {
      for(int j = 0; j < m; j++)
      {
        //cout << h[i][j][s];
        ans = ans && (lawn[i][j] >= max(h[i][j][0], h[i][j][1]) || lawn[i][j] >= max(h[i][j][2], h[i][j][3])); 
      }
      //cout << endl;
    }
    //cout << endl;
    } 
    printf("Case #%d: %s\n", cnt, ans ? "YES" : "NO");
  }
  return 0;
}
