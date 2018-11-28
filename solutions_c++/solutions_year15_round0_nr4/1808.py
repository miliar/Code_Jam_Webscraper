#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("Dinput.in","r",stdin);
    freopen("Doutput.txt","w",stdout);
    int T;
    scanf("%d",&T);

    for(int it=1;it<=T;it++)
    {
        int X,R,C;
        scanf("%d%d%d",&X,&R,&C);
        int ans=0;

        printf("Case #%d: ",it);

        int sum_blocks = R*C;
        if(X==sum_blocks && X!=1 && X!=2)
        {
            printf("RICHARD\n");
        }
        else if(sum_blocks%X==0 && X!=4)
        {
            printf("GABRIEL\n");
        }
        else if(sum_blocks%X==0 && X==4 && sum_blocks>=12)
        {
            printf("GABRIEL\n");
        }
        else
        {
            printf("RICHARD\n");
        }
    }


}


