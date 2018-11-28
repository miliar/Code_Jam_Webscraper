#include<cstdio>
#include<algorithm>
#include<string>

using namespace std;

// r <= c
bool check(int x,int r,int c)
{
    if(x==1) return true;
    if(x==2)
    {
        if((r*c)%x != 0) return false;
    }
    if(x==3)
    {
        if((r*c)%x != 0) return false;
        if(r==1) return false;
    }
    if(x==4)
    {
        if((r*c)%x != 0) return false;
        if(r==1) return false;
        if(r==2 and c==2) return false;
        if(r==2 and c==4) return false;
        if(r==3) return true;
        if(r==4) return true;
    }
    return true;
}

int main()
{
    int t,it;
    char ans[2][10] = {"RICHARD", "GABRIEL"};
    scanf("%d",&t);
    it = t;
    while(t-- > 0)
    {
        int x,r,c;
        scanf("%d %d %d",&x,&r,&c);
        printf("Case #%d: %s\n",it-t,ans[check(x,min(r,c),max(r,c))]);
    }
    return 0;
}
