#include <iostream>
#include<stdio.h>
using namespace std;

void lotterygame(int t);
int main()
{
    int t;
    scanf("%d",&t);
    int i;
    for(i=1;i<=t;i++)
    {
        lotterygame(i);
    }
    return 0;
}
void lotterygame(int t)
{
    int a,b,k;
    int c=0;
    int i,j;
    scanf("%d%d%d",&a,&b,&k);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {

                if((i&j)<k)
                {
                    c++;
 //                   printf("i=%d  j=%d   i&j=%d \n",i,j,(i&j));
                }
            }
        }
    printf("Case #%d: %d\n",t,c);
}
