#include <bits/stdc++.h>
using namespace std;
#define TAM       101 

int n;
vector<int> G[TAM];
int idx[TAM], low[TAM], cur;
bool art[TAM];

void go ( int i, int pi ) {
  idx[i] = low[i] = cur++;
  int cnt = 0;
  for ( int j : G[i] ) {
    if ( j == pi ) continue;
    if ( idx[j] == -1 ) {
      cnt++;
      go ( j, i );
      if ( low[j] >= idx[i] )
        art[i] = true;
      low[i] = min ( low[i], low[j] );
    }
    else
      low[i] = min ( low[i], idx[j] );
  }
  if ( !i )
    art[i] = ( cnt > 1 );
}

int main()
{
  string line;
  while ( scanf ( "%d", &n ) && n ) {
    for ( int i = 0; i < n; ++i ) G[i].clear();
    getline ( cin, line );
    for ( int i, j; getline ( cin, line ); ) {
      stringstream ss ( line );
      if ( (ss >> i) && !i ) break;
      while ( ss >> j ) {
        G[i-1].push_back(j-1);
        G[j-1].push_back(i-1);
      }
    }

    memset ( idx, -1, sizeof(idx) );
    memset ( art, 0, sizeof(art) );
    cur = 0;
    go ( 0, -1 );
    cout << count(art,art+n,true) << '\n';
  }
  return 0;
}
