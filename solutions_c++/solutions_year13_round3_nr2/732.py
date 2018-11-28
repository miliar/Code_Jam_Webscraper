#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;

void solve(){

    int x,y;
    scanf("%d %d",&x,&y);
    if ( y > 0 )
    {
        for (int i=0;i<y;i++)
                putchar('S'),putchar('N');
    }
    else if ( y < 0 ) {
        y = -y;
        for (int i=0;i<y ;i++)
                putchar('N'),putchar('S');
    }
    if ( x < 0 )
    {
        x = - x;
        for (int i=0;i<x ;i++)
                putchar('E'),putchar('W');
    }
    else if ( x > 0 ) {
        for (int i=0;i<x;i++)
                           putchar('W'),putchar('E');
    }

    putchar('\n');
    


}

int main(){
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
