#include <cstdio>

int a1, a2;
int cards1[4][4], cards2[4][4];

void readcards(int c[][4])
{
  for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
      scanf("%d",&c[i][j]);
}

void solve(int tt)
{
  scanf("%d",&a1);
  readcards(cards1);
  scanf("%d",&a2);
  readcards(cards2);
  a1--;
  a2--;

  int sc = 0;
  int snum;
  for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
      if(cards1[a1][i] == cards2[a2][j]) {
        sc++;
        snum = cards1[a1][i];
      }

  printf("Case #%d: ",tt+1);
  if(sc == 1)
    printf("%d\n",snum);
  else if(sc == 0)
    printf("Volunteer cheated!\n");
  else
    printf("Bad magician!\n");
}

main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt<t; tt++)
    solve(tt);
}
