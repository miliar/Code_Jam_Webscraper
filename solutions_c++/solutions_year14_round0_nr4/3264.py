/*
 * COMP: CODE JAM 2014
 * PROG: D.Deceitful War
 * LANG: C++
 * AUTH: paelletadecaragols
 */

#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);

  for(int x = 0; x < T; x++)
  {
    int N;
    scanf("%d", &N);

    long double blocks[2][N];
    for(int i = 0; i < 2*N; i++) scanf("%Lf", &blocks[i/N][i%N]);

    sort(blocks[0], blocks[0]+N);
    sort(blocks[1], blocks[1]+N);

    int y = 0, z = 0;
    for(int i = 0; i < N; i++)
    {
      if(blocks[0][i] > blocks[1][y]) y++;
      if(blocks[0][N-i-1] < blocks[1][N-1-z]) z++;
    }
    printf("Case #%d: %d %d\n", x+1, y, N-z);
  }
}
