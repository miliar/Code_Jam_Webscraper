#include<cstdio>
using namespace std;

int check(int a,int b)
{
    int c=0;
    int p[] = {1,4,9,121,484};
    for(int x=0;x<5;x++)
    {
        if(p[x]>=a && p[x]<=b)
            c++;
    }
    return c;
}
int main()
{

    int c,a,b;
    scanf("%d",&c);
    for(int x=1;x<=c;x++)
    {
        scanf("%d %d",&a,&b);
        printf("Case #%d: %d\n",x,check(a,b));
    }
}
