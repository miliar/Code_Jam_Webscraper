#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<iomanip>
#include<algorithm>
using namespace std;
int a[205];
char s[105][105];
int check(int x,int y,int dir,int R,int C)
{
    if(x<0 || x>=R || y<0 || y>=C)
    {
        if(x<0)return y+1;
        else if(y>=C)return C+x+1;
        else if(x>=R)return R+2*C-y;
        else return 2*(R+C)-x;
    }
    if(dir==0 && s[x][y]=='/')return check(x,y-1,1,R,C);
    if(dir==0 && s[x][y]=='\\')return check(x,y+1,3,R,C);
    if(dir==1 && s[x][y]=='/')return check(x+1,y,0,R,C);
    if(dir==1 && s[x][y]=='\\')return check(x-1,y,2,R,C);
    if(dir==2 && s[x][y]=='/')return check(x,y+1,3,R,C);
    if(dir==2 && s[x][y]=='\\')return check(x,y-1,1,R,C);
    if(dir==3 && s[x][y]=='/')return check(x-1,y,2,R,C);
    if(dir==3 && s[x][y]=='\\')return check(x+1,y,0,R,C);
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int R,C;
        scanf("%d%d",&R,&C);
        for(int i=1;i<=2*(R+C);i++)
            scanf("%d",&a[i]);
        bool isok=0;
        memset(s,0,sizeof(s));
        for(int mask=0;mask<(1<<R*C) && !isok;mask++)
        {
            for(int i=0;i<R;i++)
                for(int j=0;j<C;j++)
                {
                    if(mask&(1<<i*C+j))s[i][j]='/';
                    else s[i][j]='\\';
                }
            bool flag=1;
            for(int i=1;i<=2*(R+C);i+=2)
            {
                int x,y,dir;
                if(a[i]<=C)dir=0,x=0,y=a[i]-1;
                else if(a[i]<=R+C)dir=1,x=(a[i]-C)-1,y=C-1;
                else if(a[i]<=R+2*C)dir=2,x=R-1,y=C-(a[i]-R-C);
                else dir=3,x=R-(a[i]-R-2*C),y=0;
                if(check(x,y,dir,R,C)!=a[i+1])flag=0;
            }
            isok|=flag;
        }
        printf("Case #%d:\n",ca);
        if(isok)for(int i=0;i<R;i++)printf("%s\n",s[i]);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
