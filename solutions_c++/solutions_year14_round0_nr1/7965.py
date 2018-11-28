#include<cstdio>
int i, j, d, a, l, x, y, t[4][4];
bool b[17];
int main()
{
  scanf("%d", &d);
  
  for(y = 1; y <= d; y++)
  {
    scanf("%d", &a);
    a--;
    for(i = 0; i < 4; i++)
    {
      for(j = 0; j < 4; j++)
      {
	scanf("%d", &t[i][j]);
	if (i == a){b[t[i][j]] = 1;}
      }
    }
    scanf("%d", &a);
    a--;
    l = 0;
    for(i = 0; i < 4; i++)
    {
      for(j = 0; j < 4; j++)
      {
	scanf("%d", &t[i][j]);
	if (i == a && b[t[i][j]] == 1){x = t[i][j];l++;}
	if (b[t[i][j]] == 1){b[t[i][j]] = 0;}
      }
    }
    printf("Case #%d: ", y);
    if (l == 0){printf("Volunteer cheated!\n");}
    if (l == 1){printf("%d\n", x);}
    if (l > 1){printf("Bad magician!\n");}
  }
  
  
  
return 0;
}