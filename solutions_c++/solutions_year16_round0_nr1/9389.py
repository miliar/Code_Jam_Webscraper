#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int t, n, used[10];
void inmake()
{ scanf("%d", &t);
  for (int e = 0; e < t; e++)
  { scanf("%d", &n);
    
    if (n == 0)
    { printf("Case #%d: INSOMNIA\n", e + 1);
      continue;
     }
    
    memset(used, 0, sizeof(used));
    int br = 0;
    int i = 1;
    while (1)
    { int n1 = i * n;
      while (n1 != 0)
      { if (used[n1 % 10] == 0)
        { br++;
          used[n1 % 10]++;
         }
        
        n1 /= 10;
       }
      
      //cout << "br = " << br << " i = " << i << " n = " << n << " i * n = " << i * n << endl;
      
      if (br == 10)
      { printf("Case #%d: %d\n", e + 1, i * n);
        break;
       }
      
      i++;
     }
   }
}

int main()
{ 
  //freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  inmake();
  
  return 0;
}
