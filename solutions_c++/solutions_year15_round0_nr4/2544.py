#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

typedef long long ll;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    int T,tc=1,i,sol,x,r,c;
    scanf("%d",&T);
    while(T > 0)
    {
        scanf("%d %d %d",&x,&r,&c);
        if(x == 1)
        {
            sol = 1;
        }
        else if(x == 2)
        {
            if(r == 1 && c == 1)
            {
                sol = 0;
            }
            if((r == 1 && c == 2) || (r == 2 && c == 1))
            {
                sol = 1;
            }
            if((r == 1 && c == 3) || (r == 3 && c == 1))
            {
                sol = 0;
            }
            if((r == 1 && c == 4) || (r == 4 && c == 1))
            {
                sol = 1;
            }
            if(r == 2 && c == 2)
            {
                sol = 1;
            }
            if((r == 2 && c == 3) || (r == 3 && c == 2))
            {
                sol = 1;
            }
            if((r == 2 && c == 4) || (r == 4 && c == 2))
            {
                sol = 1;
            }
            if(r == 3 && c == 3)
            {
                sol = 0;
            }
            if((r == 3 && c == 4) || (r == 4 && c == 3))
            {
                sol = 1;
            }
            if(r == 4 && c == 4)
            {
                sol = 1;
            }
        }
        else if(x == 3)
        {
            if(r == 1 && c == 1)
            {
                sol = 0;
            }
            if((r == 1 && c == 2) || (r == 2 && c == 1))
            {
                sol = 0;
            }
            if((r == 1 && c == 3) || (r == 3 && c == 1))
            {
                sol = 0;
            }
            if((r == 1 && c == 4) || (r == 4 && c == 1))
            {
                sol = 0;
            }
            if(r == 2 && c == 2)
            {
                sol = 0;
            }
            if((r == 2 && c == 3) || (r == 3 && c == 2))
            {
                sol = 1;
            }
            if((r == 2 && c == 4) || (r == 4 && c == 2))
            {
                sol = 0;
            }
            if(r == 3 && c == 3)
            {
                sol = 1;
            }
            if((r == 3 && c == 4) || (r == 4 && c == 3))
            {
                sol = 1;
            }
            if(r == 4 && c == 4)
            {
                sol = 0;
            }
        }
        else if(x == 4)
        {
            if(r == 1 && c == 1)
            {
                sol = 0;
            }
            if((r == 1 && c == 2) || (r == 2 && c == 1))
            {
                sol = 0;
            }
            if((r == 1 && c == 3) || (r == 3 && c == 1))
            {
                sol = 0;
            }
            if((r == 1 && c == 4) || (r == 4 && c == 1))
            {
                sol = 0;
            }
            if(r == 2 && c == 2)
            {
                sol = 0;
            }
            if((r == 2 && c == 3) || (r == 3 && c == 2))
            {
                sol = 0;
            }
            if((r == 2 && c == 4) || (r == 4 && c == 2))
            {
                sol = 0;
            }
            if(r == 3 && c == 3)
            {
                sol = 0;
            }
            if((r == 3 && c == 4) || (r == 4 && c == 3))
            {
                sol = 1;
            }
            if(r == 4 && c == 4)
            {
                sol = 1;
            }
        }
        if(sol == 0)
            printf("Case #%d: RICHARD\n",tc);
        else
            printf("Case #%d: GABRIEL\n",tc);
        tc++;
        T--;
    }
    return 0;
}
