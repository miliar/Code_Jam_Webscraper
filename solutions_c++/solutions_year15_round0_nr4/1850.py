#include<cstdio>
#include<algorithm>
#include<vector>
#include<limits.h>
#include<list>
#include<stack>
#include<set>
#include<string.h>
#include<iostream>
#include<map>

using namespace std;

int main()
{
    freopen("D.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t,x,r,c,k,i;
    bool rich;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        rich=true;
        scanf("%d %d %d",&x,&r,&c);
        switch(x)
        {
            case 1: rich=false;
                    break;

            case 2: if(r%2==0 || c%2==0)
                        rich=false;
                    break;

            case 3: if((r==3 && c>1)||(c==3 && r>1))
                        rich=false;
                    break;

            case 4: if((r==4 && c>2) || (c==4 && r>2))
                        rich=false;
                    break;
        }
        if(rich)
            printf("Case #%d: RICHARD\n",k);
        else
            printf("Case #%d: GABRIEL\n",k);
    }
    return 0;
}
