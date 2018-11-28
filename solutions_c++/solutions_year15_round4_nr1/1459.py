#include <cstdio>
#include <cstring>
#define MAXN 105

using namespace std;

char board[MAXN][MAXN];
int prefix[MAXN][MAXN][4]; // left, up, right, down
int r, c;

int main() {
  int tc;
  scanf("%d", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%d %d\n", &r, &c);
    for(int i = 0; i < r; i++)
      scanf("%s\n", board[i]);
    memset(prefix, 0, sizeof prefix);
    for(int i = 0; i < r; i++) {
      for(int j = 0; j < c; j++) {
	prefix[i][j][0] = prefix[i][j][1] = board[i][j] == '.' ? 0 : 1;
	if(j > 0)
	  prefix[i][j][0] += prefix[i][j-1][0];
	if(i > 0)
	  prefix[i][j][1] += prefix[i-1][j][1];
      }
    }
    for(int i = r - 1; i > -1; i--) {
      for(int j = c - 1; j > -1; j--) {
	prefix[i][j][2] = prefix[i][j][3] = board[i][j] == '.' ? 0 : 1;
	if(j < c - 1)
	  prefix[i][j][2] += prefix[i][j+1][2];
	if(i < r - 1)
	  prefix[i][j][3] += prefix[i+1][j][3];
      }
    }
    int ans = 0;
    bool possible = true;
    for(int i = 0; i < r; i++) {
      for(int j = 0; j < c; j++) {
	int& left = prefix[i][j][0];
	int& up = prefix[i][j][1];
	int& right = prefix[i][j][2];
	int& down = prefix[i][j][3];
	//printf("i=%d j=%d left=%d up=%d right=%d down=%d\n", i, j, left, up, right, down);
	if(board[i][j] == '.')
	  continue;
	if(left > 1 && up > 1 && right > 1 && down > 1)
	  continue;
	if(left == 1 && up == 1 && right == 1 && down == 1) {
	  possible = false;
	  break;
	} else {
	  if(board[i][j] == '<' && left == 1)
	    ans++;
	  if(board[i][j] == '^' && up == 1)
	    ans++;
	  if(board[i][j] == '>' && right == 1)
	    ans++;
	  if(board[i][j] == 'v' && down == 1)
	    ans++;
	  //printf("i=%d j=%d ans=%d\n", i, j, ans);
	}
      }
      if(!possible)
	break;
    }
    if(possible)
      printf("Case #%d: %d\n", kase, ans);
    else
      printf("Case #%d: IMPOSSIBLE\n", kase);
  }
  return 0;
}
