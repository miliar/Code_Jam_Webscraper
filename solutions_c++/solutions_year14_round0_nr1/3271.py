#include<stdio.h>

struct Magic
{
    int guess;
    int card[4][4];
}magic[2];

void readin()
{
    for(int i = 0; i < 2; i++)
    {
        scanf("%d\n", &magic[i].guess);
        magic[i].guess--;
        for(int j = 0; j < 4; j++)
            for(int k = 0; k < 4; k++)
                scanf("%d", &magic[i].card[j][k]);
    }
}
void solve()
{
    int ans, count = 0;
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(magic[0].card[magic[0].guess][i] == magic[1].card[magic[1].guess][j])
            {
                ans = magic[0].card[magic[0].guess][i];
                count++;
            }
    if(count == 1)
        printf("%d\n", ans);
    else if(count == 0)
        printf("Volunteer cheated!\n");
    else
        printf("Bad magician!\n");
}

int main()
{
  #ifndef ONLINE_JUDGE
	   freopen("data.txt","r",stdin);
       freopen("out.txt","w",stdout);
  #endif

  int T;
  scanf("%d\n", &T);
  
  for(int i = 1; i <= T; i++)
  {
      printf("Case #%d: ", i);
      readin();
      solve();
  }
  return 0;

}
 