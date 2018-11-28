#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int main(void)
{
    int ca,cases;
    int r,x,c;
    freopen("D-small-attempt2.in","r+",stdin);
    freopen("D_out.txt","w+",stdout);
    scanf("%d",&cases);
    for (ca=1;ca<=cases;ca++)
    {
        scanf("%d%d%d",&x,&r,&c);
        printf("Case #%d: ",ca);
        if (x>max(r,c)||(r*c)%x!=0||x>=7||(x+1)/2>min(r,c))
            printf("RICHARD\n");
        else
        {
            if (x==4&&(min(r,c)==2))
                printf("RICHARD\n");
            else
            printf("GABRIEL\n");
        }
    }
    return 0;
}
