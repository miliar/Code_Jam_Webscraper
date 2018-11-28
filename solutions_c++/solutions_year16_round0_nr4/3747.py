#include <stdio.h>
#include <iostream>

using namespace std;

int main(){

    freopen("input.in", "r", stdin );
    freopen( "output.out", "w", stdout );

	int t;
    scanf("%d",&t);
    int k,c,s,i,x;
    for(x=1;x<=t;x++){
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",x);
        for(i=1;i<=s;i++)
            printf("%d ",i);
        printf("\n");
    }
    return 0;
}
