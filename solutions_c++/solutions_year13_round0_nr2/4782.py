#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;
int w[101][101];
int row[101];
int col[101];
bool notcomplete;

int main(int argc, char const *argv[])
{
  int count = 0;
  scanf("%d", &count);

  for (int counter = 1; counter <= count; ++counter)
  {
    cout<<"Case #"<<counter<<": ";
    int r = 0, c =0;
    scanf("%d %d",&r, &c);

    for (int i = 0; i < r; ++i)
    {
      row[i]=0;
      for (int j = 0; j < c; ++j)
      {
        scanf("%d", &w[i][j]);
        if(w[i][j] > row[i]) row[i] = w[i][j];
      }
    }
    // cout<<"test\n";
    for (int i = 0; i < c; ++i)
    {
      col[i]=0;
      for (int j = 0; j < r; ++j)
      {
        if(w[j][i] > col[i]) col[i] = w[j][i];
      }
    }
    bool broken = false;
    for (int i = 0; i < r; ++i)
    {
      for (int j = 0; j < c; ++j)
      {
        if(w[i][j] != min(row[i], col[j])) {broken = true;}
      }
    }
    if(broken) cout<<"NO\n";
    else cout<<"YES\n";
  }

  return 0;
}