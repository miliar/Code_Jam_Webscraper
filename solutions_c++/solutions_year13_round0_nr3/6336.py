#include <iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>

using namespace std;
int f[1006];
void fun()
{
    f[0]=1;
    f[1]=1;
    f[4]=1;
    f[9]=1;
    f[121]=1;
    f[484]=1;
}

int main()
{
    freopen("A0.in","r",stdin);
    freopen("A00.in","w",stdout);
    fun();
    int t,a,b,coun,i,c=1;
    scanf("%d",&t);
    while(t--)
    {
        coun=0;
        scanf("%d %d",&a,&b);
        for(i=a;i<=b;i++)
            if(f[i]==1)
            coun++;
            printf("Case #%d: %d\n",c++,coun);
    }
    return 0;
}
