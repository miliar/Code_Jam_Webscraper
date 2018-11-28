#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main(){

   freopen( "input.in", "r", stdin );
freopen( "output.out", "w", stdout );

	int t;
    scanf("%d",&t);
    int k,c,s,i,z;
    for(z=1;z<=t;z++)
    {
        scanf("%d%d%d",&k,&c,&s);
        if(s<k)
        {
            printf("IMPOSSIBLE");
        }
        else{
        printf("Case #%d: ",z);
        for(i=1;i<=s;i++){
        printf("%d ",i);
        }
        }
        printf("\n");
    }
    return 0;
}
