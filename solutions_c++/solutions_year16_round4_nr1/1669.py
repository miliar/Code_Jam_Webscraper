#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int T;
int N,R,P,S;

void extract(int d,int t)
{
    if(d==0)
    {
        if(t==0)printf("P");
        if(t==1)printf("R");
        if(t==2)printf("S");
        return ;
    }
    if(t==0){extract(d-1,0);extract(d-1,1);}
    if(t==2){extract(d-1,d>2?2:0);extract(d-1,d>2?0:2);}
    if(t==1){extract(d-1,d>1?2:1);extract(d-1,d>1?1:2);}
}

bool possible(int p,int r,int s)
{
    if(p+r+s==1)
    {
        if(p==1)extract(N,0);
        else if(r==1)extract(N,1);
        else if(s==1)extract(N,2);
        return true;
    }
    int x=p+r-s,y=s+p-r,z=r+s-p;
    if((x&1)||(y&1)||(z&1)||x<0||y<0||z<0)return false;
    else return possible(x/2,z/2,y/2);
}

int main()
{
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%d%d%d%d",&N,&R,&P,&S);
        printf("Case #%d: ",kase);
        if(possible(P,R,S))
        {
            puts("");
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
