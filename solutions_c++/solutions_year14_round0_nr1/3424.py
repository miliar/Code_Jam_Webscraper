/*
 * COMP: CODE JAM 2014
 * PROG: A.Magic Trick
 * LANG: C++
 * AUTH: paelletadecaragols@gmail.com
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);

  for(int i = 0; i < T; i++)
  {
    int chosen, n_results = 0;
    int cards[16] = {0};
    for(int j = 0; j < 2; j++)
    {
      int n, replay;
      scanf("%d", &replay);

      for(int k = 0; k < 16; k++)
      {
        cin >> n;
        if(k/4 == replay-1) cards[n-1]++;
      }
    }

    for(int j = 0; j < 16; j++) if(cards[j] == 2) { n_results++; chosen = j+1; }

    if(n_results == 0) printf("Case #%d: Volunteer cheated!\n", i+1);
    else if(n_results == 1) printf("Case #%d: %d\n", i+1, chosen);
    else printf("Case #%d: Bad magician!\n", i+1);
  }
}
