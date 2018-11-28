#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;
typedef long long ll;
#define MAX_L 10005
int S[MAX_L];
int S_L[MAX_L];
int S_R[MAX_L];

int part[MAX_L][MAX_L];

int G[4][4][4];
// i = 2, j = 3, k = 4
#define I 2
#define J 3
#define K 4

int convert[5][5] = {
  {0, 0,  0,  0,  0},
  {0, 1,  I,  J,  K},  
  {0, I, -1,  K, -J},
  {0, J, -K, -1,  I},
  {0, K,  J, -I, -1},
};

int a_block;

int calc_blocks(int num) {
  if (a_block == 1) return 1;

  num %= 4;
  switch(num) {
  case 0:
    return 1;
  case 1:
    return a_block;
  case 2:
    return -1;
  default:
    return -a_block;
  }
}

int multi_chars( int a, int b) {
  int sign_a = (a > 0) ? 1 : -1;
  int sign_b = (b > 0) ? 1 : -1;
  int ret = convert[abs(a)][abs(b)] * sign_a * sign_b;
  //  printf("convert[%d][%d] = %d\n", abs(a), abs(b), ret);
  return ret;
}

bool check_chars( int a, int b, int c ) {
  if (a != I) return false;
  if (b != J) return false;
  if (c != K) return false;

  return true;
}

char int2char( int n ) {
  char c;
  switch(abs(n)) {
  case 2:
    c = 'i';
  case 3:
    c = 'j';
  case 4:
    c = 'k';
  default:
    c = '1';
  }
  return c;
}

int main()
{
  int T;
  scanf("%d", &T);
  
  for (int i = 0; i < T; i++) {
    ll L, X;
    bool enable = false;
    scanf("%lld %lld", &L, &X);

    a_block = 1;
    for (int j = 0; j < L; j++) {
      char c;
      cin >> c;
      S[j] = c - 'g';
      a_block = multi_chars( a_block, S[j] );
    }

    if ( L * X < 3 ) {
      printf("Case #%d: NO\n", (i+1));      
      continue;
    }
    

    for (int j = 0; j <= L; j++) {
      for (int k = j; k <= L; k++) {
        if (j == k) {
          part[j][k] = 1;
        } else {
          part[j][k] = multi_chars( part[j][k-1],  S[k-1] );
        }
        //        printf("part[%d][%d] = %d\n", j, k, part[j][k]);
      }
    }
    
    // left div and right div are in same block.
    for (int left = 0; left <= L; left++) {
      if ( enable ) break;
      for (int right = left; right <= L; right++) {
        if ( enable ) break;
        int t_l_char   = part[0][left];
        int m_char     = part[left][right];
        int t_r_char   = part[right][L];
        for ( int l_b_n = 0; l_b_n < 4; l_b_n++ ) {
          for ( int r_b_n = 0; r_b_n < 4; r_b_n++ ) {
            ll need = 1 + l_b_n + r_b_n;
            if ( X < need ) continue;
            if ( (X - need) % 4 != 0 ) continue;
            
            int l_char = multi_chars( calc_blocks(l_b_n), t_l_char );
            int r_char = multi_chars( t_r_char, calc_blocks(r_b_n) );
            if ( check_chars( l_char, m_char, r_char ) ) {
              enable = true;
              break;
            }
          }
        }
        if ( enable ) break;
      }
    }

    if ( !enable && X > 1 ) {
      //left div and right div are in different block
      for (int left = 0; left <= L; left++) {
        if ( enable ) break;
        for (int right = 0; right <= L; right++) {
          if ( enable ) break;
          int t_l_char  = part[0][left];
          int t_r_char  = part[right][L];

          for ( int l_b_n = 0; l_b_n < 4; l_b_n++ ) {
            for ( int r_b_n = 0; r_b_n < 4; r_b_n++ ) {
              for ( int m_b_n = 0; m_b_n < 4; m_b_n++ ) {
                ll need = 2 + l_b_n + r_b_n + m_b_n;
                if ( X < need ) continue;
                if ( (X - need) % 4 != 0 ) continue;
                int l_char = multi_chars( calc_blocks(l_b_n), t_l_char );
                int r_char = multi_chars( t_r_char, calc_blocks(r_b_n) );
                int m_char = multi_chars( part[left][L], multi_chars( calc_blocks(m_b_n), part[0][right] ) );
                if ( check_chars( l_char, m_char, r_char ) ) {
                  enable = true;
                  break;
                }
              }
            }
          }
        }
      }
    }

    if ( enable ) printf("Case #%d: YES\n", (i+1));
    else printf("Case #%d: NO\n", (i+1));
  }
}
