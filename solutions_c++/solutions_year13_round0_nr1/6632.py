// written by lonerdude(dvdreddy)
// all rights reserved
//the template by dvdreddy
#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <iostream>
#include <cstring>
#include <string>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sf(x) scanf("%lf",&x)
#define ss(x) scanf("%s",&x)

#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(i,n)  f(i,0,n)

typedef long long ll;

int main(){
  int t; int cur = 1;
  si(t);
  while (t--){
    cout << "Case #" << cur << ": ";
    cur++;
    string s1[4];
    string s2[4];
    fr (i, 4){
      cin >> s1[i];
      s2[i] = s1[i];
    }

    fr (i, 4){
      fr (j, 4){
	if (s1[i][j] == 'T'){
	  s1[i][j] = 'X';
	}
      }
    }

    fr (i, 4){
      fr (j, 4){
	if (s2[i][j] == 'T'){
	  s2[i][j] = 'O';
	}
      }
    }
    
    bool b = false;
    bool bx[4];  bool bx2 = false; 
    fr (i, 4){
      bx[i] = true;
      if (s1[i] == "XXXX"){
	b = true;
      }
      fr (j, 4){
	if (s1[j][i] != 'X'){
	  bx[i] = false; break;
	}
      }
      bx2 = bx2 | bx[i];
    }

    if (b || bx2){
      cout << "X won\n";
      continue;
    }
    
    bool b1 = true;
    bool b2 = true;
    fr (i, 4){
      if (s1[i][i] != 'X'){
	b1 = false;
      }
      if (s1[i][3 - i] != 'X'){
	b2 = false;
      }
    }
    
    if (b1 || b2){
      cout << "X won\n";
      continue;
    }
    
    
    b = false;
    bx2 = false;
    fr (i, 4){
      bx[i] = true;
      if (s2[i] == "OOOO"){
	b = true;
      }
      fr (j, 4){
	if (s2[j][i] != 'O'){
	  bx[i] = false; break;
	}
      }
      bx2 = bx2 | bx[i];
    }

    if (b || bx2){
      cout << "O won\n";
      continue;
    }
    
    b1 = true;
    b2 = true;
    fr (i, 4){
      if (s2[i][i] != 'O'){
	b1 = false;
      }
      if (s2[i][3 - i] != 'O'){
	b2 = false;
      }
    }
    
    if (b1 || b2){
      cout << "O won\n";
      continue;
    }
    
    b = false;
    
    fr (i, 4){
      fr (j, 4){
	if (s1[i][j] == '.'){
	  b = true;
	  break;
	}
      }
    }
    
    if (b){
      cout << "Game has not completed\n";
    } else {
      cout << "Draw\n";
    }   
  }
}
