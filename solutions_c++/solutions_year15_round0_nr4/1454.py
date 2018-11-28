#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<stdio.h>
#include<set>
#include<cmath>

using namespace std;

int main() {
    freopen("exam.in","r",stdin);
    freopen("exam.out","w",stdout);
    int T,x,r,c;

    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        scanf("%d%d%d",&x,&r,&c);
        bool ans=true;
        if((r*c)%x==0)
        {

            if(x==1) ans=false;
            if(x==2) ans=false;
            if(x==3)
            {
                ans=false;
            }
            if(x==4)
            {
                ans = min(r,c)<=2;
            }
            if((x+1)/2>min(r,c)) ans=true;
            if(x>r && x>c) ans=true;
        }
        if(ans) printf("Case #%d: RICHARD\n",t);
        else printf("Case #%d: GABRIEL\n",t);
    }
    return 0;
}
