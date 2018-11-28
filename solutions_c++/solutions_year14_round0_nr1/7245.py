#include <iostream>
#include <cstdio>
using namespace std;

int t, pom[17];

void foo (int row)
{
  for (int i=1; i<=4; i++)
    for (int j=1; j<=4; j++)
    {
      int a;
      scanf ("%d", &a);
      if (i==row) pom[a]++;
    }
}

int main ()
{
  scanf ("%d", &t);
  
  for (int yolo=1; yolo<=t; yolo++)
  {
    int a;
    for (int i=1; i<=16; i++) pom[i]=0;

    scanf ("%d", &a);
    foo (a);
    
    scanf ("%d", &a);
    foo (a);
    
    int ile=0, w;
    
    for (int i=1; i<=16; i++)
      if (pom[i]==2) ile++, w=i;
      
    printf ("Case #%d: ", yolo);
    if (ile==1) printf (" %d\n", w);
    if (ile>1) printf (" Bad magician!\n");
    if (ile<1) printf (" Volunteer cheated!\n");
  }
  
  return 0;
}