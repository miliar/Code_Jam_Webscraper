#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;
int a,b,c;
void rez()
{
    scanf("%d %d %d",&a,&b,&c);
    int k=0;
    for(int i=0;i<a;i++)
        for(int j=0;j<b;j++)
    {
        int cc=i&j;
        if(cc<c)
            k++;
    }
    printf("%d",k);
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int n;
    scanf("%d",&n);
    for(int run=1;run<=n;run++)
    {
        printf("Case #%d: ",run);
        rez();
        printf("\n");
    }
    return 0;
}
