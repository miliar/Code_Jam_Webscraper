#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
int main()
{
    int _,T,A,B,X;
    scanf("%d",&T);
    for (_=1; _<=T; _++)
    {
        printf("Case #%d: ",_);
        scanf("%d%d%d",&X,&A,&B); if (A>B) swap(A,B);
        if (X==1) puts("GABRIEL"); else
        {
            if (X==2)
            {
                if (A*B%2==0) puts("GABRIEL"); else puts("RICHARD");
            } else
              if (X==3)
              {
                  if (A*B%3==0 && min(A,B)!=1) puts("GABRIEL"); else puts("RICHARD");
              } else if (B==4 && A>=3) puts("GABRIEL");else puts("RICHARD");
        }
    }
    return 0;
}
