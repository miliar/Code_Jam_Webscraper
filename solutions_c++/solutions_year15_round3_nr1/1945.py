#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

int main()
{    
    freopen("A-small-attempt4.in","r",stdin);
    freopen("A_output_small.txt","w",stdout);
    int T,R,C,W;
    int result;
    scanf("%d",&T);
    for (int index=1;index<=T;index++)
    {
        scanf("%d%d%d",&R,&C,&W);
        if (W==C) 
        {
            result=R+W-1;
        }else if (2*W>C)
        {
            result=R+W;
        }else{
            if (C%W==0) result=R*(C/W+W-1);
            else result=R*(C/W+W);
        }
        printf("Case #%d: %d\n",index,result);
    }
    return 0;
}
