//wise words from the departing:
//eat your greens, especially broccoli
//remember to say thank you for all the things
//you haven't had
#include <ctime>
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <map>
#include <bitset>
#include <string.h>
#include <stdio.h>
#include <set>
#include <stdlib.h>
#include <memory.h>

using namespace std;

#define		FOR(i,a,b) for(int i=int(a);i<int(b);++i)
#define		X first
#define		Y second
typedef pair <int,int> pii;
#define MP(a,b) make_pair(a,b);
typedef vector <int> vi;
typedef set <int> si;

//1 - x won
//2 - o won
//0 - nobody won
int w(string s) {
  int x,y,z;
  x = y = z = 0;
  
  for(int i = 0; i<4; i++) {
    if(s[i] == 'T')
      z++;
    if(s[i] == 'X')
      x++;
    if(s[i] == 'O')
      y++;
  }
  
  if(x+z == 4)
    return 1;
  if(y+z == 4)
    return 2;
    
  return 0;
}

int main()
{
#ifndef ONLINE_JUDGE
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
#endif
#ifdef ONLINE_JUDGE
  //freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
#endif
  int T;
  
  cin >> T;
  
  string board[5], t[4], diag[2];
  getline(cin, board[0]);
  int d;
  FOR(i, 0, T) {
    FOR(j,0,5)
      getline(cin, board[j]);
    
    d = w(board[0]) | w(board[1]) | w(board[2]) | w(board[3]);
    FOR(j, 0, 4) {
      FOR(k, 0, 4)
        t[j].push_back(board[k][j]);
    }
    d |= w(t[0]) | w(t[1]) | w(t[2]) | w(t[3]);
    
    FOR(j, 0, 4) {
      diag[0].push_back(board[j][j]);
      diag[1].push_back(board[j][3-j]);
    }
    
    d |= w(diag[0]) | w(diag[1]);
    
    if(d == 1) {
      cout << "Case #" << i+1 << ": X won" << endl;
    }
    else if(d == 2) {
      cout << "Case #" << i+1 << ": O won" << endl;
    }
    else {
      bool draw = true;
      FOR(j,0,4)
        FOR(k,0,4)
          if(board[j][k] == '.')
            draw = false;
            
      if(draw)
        cout << "Case #" << i+1 << ": Draw" << endl;
      else
        cout << "Case #" << i+1 << ": Game has not completed" << endl;
    }
    FOR(j,0,4)
      t[j].clear();
    FOR(j,0,2)
      diag[j].clear();
  }
  return 0;
}
