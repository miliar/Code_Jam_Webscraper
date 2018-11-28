#include <cstdio>

using namespace std;

int main()
{
  int t;
  int c = 1;
  int arr1[4][4], arr2[4][4];
  scanf("%d", &t);
  while(t--)
  {
    int r1, r2;
    scanf("%d", &r1);
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        scanf("%d", &arr1[i][j]);
    scanf("%d", &r2);
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        scanf("%d", &arr2[i][j]);
    int count = 0;
    int pos = 0;
    r2--;
    r1--;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        if(arr1[r1][i] == arr2[r2][j])
        {
          count++;
          pos = i;
        }
    printf("Case #%d: ", c++);
    if(count == 1)
      printf("%d\n", arr1[r1][pos]);
    else if(count > 1)
      printf("Bad magician!\n");
    else if(count == 0)
      printf("Volunteer cheated!\n");
  }
  return 0;  
}
