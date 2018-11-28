//darkstallion's template

#include<bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
#define PI acos(-1)
#define eps 1e-9
using namespace std;

int r,c;
string mat[150];

char f (int x, int y, int ch)
{
  bool ada1 = false, ada2 = false, ada3 = false, ada4 = false;
  FOR(i,y+1,c)
    if (mat[x][i] != '.')
    {
      ada1 = true;
      break;
    }
  FOR(i,x+1,r)
    if (mat[i][y] != '.')
    {
      ada2 = true;
      break;
    }
  FOR(i,0,y)
    if (mat[x][i] != '.')
    {
      ada3 = true;
      break;
    }
  FOR(i,0,x)
    if (mat[i][y] != '.')
    {
      ada4 = true;
      break;
    }
  if (!ada1 && !ada2 && !ada3 && !ada4)
    return '.';
  if (ada1 && (ch == '>'))
    return ch;
  if (ada2 && (ch == 'v'))
    return ch;
  if (ada3 && (ch == '<'))
    return ch;
  if (ada4 && (ch == '^'))
    return ch;
  if (ada1)
    return '>';
  if (ada2)
    return 'v';
  if (ada3)
    return '<';
  if (ada4)
    return '^';
}

int main()
{
  int t;
  scanf("%d",&t);
  FORN(i,t)
  {
    scanf("%d%d",&r,&c);
    FORN(j,r)
      cin >> mat[j];
    int ans = 0;
    bool benar = true;
    FORN(j,r)
      if (benar)
      {
        FORN(k,c)
          if (mat[j][k] != '.')
          {
            char z = f(j,k,mat[j][k]);
            if (z == '.')
            {
              benar = false;
              break;
            }
            if (mat[j][k] != z)
              ans++;
          }
      }
      else
        break;
    if (benar)
      printf("Case #%d: %d\n",i+1,ans);
    else
      printf("Case #%d: IMPOSSIBLE\n",i+1);
  }
}