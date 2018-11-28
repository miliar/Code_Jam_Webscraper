#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int t, n;
char a[107];
void RemoveLastPluses()
{ while (n > 0 && a[n - 1] == '+')
  n--;
}

void inmake()
{ scanf("%d", &t);
  for (int e = 0; e < t; e++)
  { memset(a, '\0', sizeof(a));
    scanf("%s", &a);
    n = strlen(a);
    
    int ans = 0;
    RemoveLastPluses();
    while (n > 0)
    { if (a[0] == '+')
      { int st = 0;
        while (st < n && a[st] == '+')
        a[st++] = '-';
        
        ans++;
       }
      
      for (int i = 0; i < n; i++)
      { if (a[i] == '+')
        a[i] = '-';
        
        else a[i] = '+';
       }
      
      reverse(a, a + n);
      ans++;
      RemoveLastPluses();
     }
    
    printf("Case #%d: %d\n", e + 1, ans);
   }
}

int main()
{ 
  //freopen("B.in", "r", stdin);
  freopen("B.out", "w" ,stdout);
  inmake();
  
  return 0;
}
