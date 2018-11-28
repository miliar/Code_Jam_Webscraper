#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

double nao[1005];
double ken[1005];

int main()
{
    freopen("d.txt","r",stdin);
    freopen("d_out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int a=0; a<tc; a++)
    {
        int n;
        scanf("%d",&n);
        for (int i=0; i<n; i++)
        {
            scanf("%lf",nao+i);
        }
        for (int i=0; i<n; i++)
        {
            scanf("%lf",ken+i);
        }
        sort(nao,nao+n);
        sort(ken,ken+n);
        int pen=0;
        int p1=0,p2=0;
        for (int i=0; i<n; i++)
        {
            if (nao[p1]<ken[p2])
            {
               p1+=1;
               pen+=1;
            }
            else
            {
                p1+=1;
                p2+=1;
            }
        }
        p1=0,p2=0;
        while (p2<n)
        {
              //printf("p1: %d,p2: %d\n",p1,p2);
              while (p2<n && nao[p1]>ken[p2])
              {
                    p2+=1;
              }
              if (p2<n)
              {
                 p1+=1;
                 p2+=1;
              }
        }
        printf("Case #%d: %d %d\n",a+1,n-pen,n-p1);
    }
}
