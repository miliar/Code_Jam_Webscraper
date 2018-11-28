#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int cnt[16];

void solve ()
{
   int p;
  
   memset( cnt, 0, sizeof(cnt) );
   
   for(int o = 0; o < 2; o++)
   {
     scanf ("%d", &p);

     for(int i = 0; i < 4; i++)
       for(int j = 0; j < 4; j++)
       {
         int temp;
         scanf ("%d", &temp);
         if(p == i + 1)
           cnt[temp-1] ++;
       }

   }

   int found = 0;

   for(int i = 1; i <= 16; i ++)
   {
      if(cnt[i-1] == 2)
      {
        if(found){
          printf ("Bad magician!\n");
          return;
        }
        found = i;
      }
   }

   if(!found)
     printf ("Volunteer cheated!\n");
    else
    printf ("%d\n", found);
}

int main ()
{
  int k;
  scanf("%d", &k);
  for(int i = 1; i <=k;i ++)
  {
    printf ("Case #%d: ", i);
    solve();
  }
}
