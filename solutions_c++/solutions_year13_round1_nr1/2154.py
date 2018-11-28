#include<stdio.h>
#include<algorithm>
#include<string>
#include<math.h>
using namespace std;


int main()
{
    int t,n,r,w,test;
    scanf("%d",&test);
    for(w=1;w<=test;w++)
    {
        scanf("%d%d",&r,&t);
        r=2*r-1;
        n=(sqrt(r*r+8*t)-r)/4;
        printf("Case #%d: %d\n",w,n);
    }

}
