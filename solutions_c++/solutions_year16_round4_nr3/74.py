#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

int R, C;
char tab[100][100];
vpii couples;

bool check()
{
  for (auto c : couples)
  {
    typedef pair<pii, int> t;
    t pos;
    if (1 <= c.first && c.first <= C)
      pos = t(pii(0, c.first-1), 0);
    if (C+1 <= c.first && c.first <= C+R)
      pos = t(pii(c.first-1-C, C-1), 1);
    if (C+R+1 <= c.first && c.first <= C+R+C)
      pos = t(pii(R-1, C+R+C-c.first), 2);
    if (C+R+C+1 <= c.first && c.first <= C+R+C+R)
      pos = t(pii(C+R+C+R-c.first, 0), 3);
    
    //cout << c.first << " " << c.second << endl;
    while (true)
    {
      //cout << pos.first.first << " " << pos.first.second << " " << pos.second << endl;
      if (pos.second == 0)
      {
        if (tab[pos.first.first][pos.first.second] == '/')
        {
          pos.second = 1;
          pos.first.second--;
        }
        else
        {
          pos.second = 3;
          pos.first.second++;
        }
      }
      else if (pos.second == 1)
      {
        if (tab[pos.first.first][pos.first.second] == '/')
        {
          pos.second = 0;
          pos.first.first++;
        }
        else
        {
          pos.second = 2;
          pos.first.first--;
        }
      }
      else if (pos.second == 2)
      {
        if (tab[pos.first.first][pos.first.second] == '/')
        {
          pos.second = 3;
          pos.first.second++;
        }
        else
        {
          pos.second = 1;
          pos.first.second--;
        }
      }
      else
      {
        if (tab[pos.first.first][pos.first.second] == '/')
        {
          pos.second = 2;
          pos.first.first--;
        }
        else
        {
          pos.second = 0;
          pos.first.first++;
        }
      }
      
      //cout << endl;
      
      if (pos.first.first < 0) break;
      if (pos.first.second < 0) break;
      if (pos.first.first >= R) break;
      if (pos.first.second >= C) break;
    }
    
    int res;
    if (pos.first.first < 0)
      res = pos.first.second+1;
    else if (pos.first.second >= C)
      res = pos.first.first+1+C;
    else if (pos.first.first >= R)
      res = C+R+C-pos.first.second;
    else
      res = C+R+C+R-pos.first.first;
       
    if (res != c.second)
      return false;
  }
  
  return true;
}

void main2()
{
  cin >> R >> C;
  
  couples.clear();
  for (int i=0; i<R+C; i++)
  {
    int a, b;
    cin >> a >> b;
    couples.push_back(pii(a, b));
  }
  
  for (int i=0; i<R; i++)
    tab[i][C] = '\0';
  
  for (int mask=0; mask<(1 << (R*C)); mask++)
  {
    for (int i=0; i<R*C; i++)
      if (mask & (1 << i))
        tab[i % R][i / R] = '/';
      else
        tab[i % R][i / R] = '\\';
    
    if (check())
    {
      for (int i=0; i<R; i++)
        cout << tab[i] << endl;
      return;
    }
  }
  
  cout << "IMPOSSIBLE" << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ":" << endl;
    main2();
  }
}
