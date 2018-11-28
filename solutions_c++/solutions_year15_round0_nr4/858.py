#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("D-large.in","r", stdin);
    freopen("D_large_output.txt", "w", stdout);

    int r,c,x,t=1,T;
    cin>>T;
    while(T--)
    {
        cin>>x>>r>>c;
        printf("Case #%d: ",t);
        if(x==1)
            printf("GABRIEL\n");

        else if(x>r && x>c)     /// x*1 doesn't fit
            printf("RICHARD\n");

        else if((r*c)%x!=0)       /// Area isn't divisible by x: There will always be some cells that can't be covered
            printf("RICHARD\n");

        else if((x+1)/2 > min(r,c)) /// Some x-ominos don't fit length or width, and will leave empty cells in other dimension
            printf("RICHARD\n");

        else if(x==4 && (min(r,c)<=2) ) /// The `-. shape will not fit
            printf("RICHARD\n");

        else if(x==5 && (max(r,c)==5 && min(r,c)==3) ) /// .-'` will not fit
            printf("RICHARD\n");

        else if(x==6 && (min(r,c) <= 3) ) /// There's a shape that will not fit (stairs shape)
            printf("RICHARD\n");

        else if(x>=7)               /// We can form a hollow square which will never cover the grid.
            printf("RICHARD\n");

        else
            printf("GABRIEL\n");
        t++;
    }
}
