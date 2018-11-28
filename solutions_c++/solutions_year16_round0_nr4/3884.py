#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int T,cas = 1;
    int K,C,S;
    freopen("C:\\Users\\L\\Downloads\\D-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\L\\Downloads\\D-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",cas++);
        scanf("%d %d %d",&K,&C,&S);
        printf("%d",1);
        for(int i=2;i<=S;i++)
            printf(" %d",i);
        printf("\n");
    }
    return 0;
}
