#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

int sol[3][13][3];

string gen(int lv,int fn)
{
    if (lv==0)
    {
        if (fn==0)
            return string("P");
        if (fn==1)
            return string("R");
        if (fn==2)
            return string("S");
    }
    string a;
    string b;
    a=gen(lv-1,fn);
    b=gen(lv-1,(fn+1)%3);
    if (a<b)
        return a+b;
    else
        return b+a;
}

int main()
{
    freopen("D:/in.txt","r",stdin);
    freopen("D:/out.txt","w",stdout);
    memset(sol,0,sizeof(sol));
    sol[0][0][0]=1;
    sol[1][0][1]=1;
    sol[2][0][2]=1;

    for (int lv=1; lv<13; lv++)
        for (int fn=0; fn<3; fn++)
            for (int i=0; i<3; i++)
                sol[fn][lv][i]=sol[fn][lv-1][i]+sol[fn][lv-1][(i+2)%3];
    int tc;
    scanf("%d",&tc);
    for (int itr=1; itr<=tc; itr++)
    {
        printf("Case #%d: ",itr);
        int n,p,r,s;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        //printf(">>%d %d %d\n",p,r,s);
        //printf("SOL %d %d %d\n",sol[0][0][0],sol[0][0][1],sol[0][0][2]);
        //printf("SOL %d %d %d\n",sol[0][1][0],sol[0][1][1],sol[0][1][2]);
        int ok=0;
        if (sol[0][n][0]==p && sol[0][n][1]==r && sol[0][n][2]==s)
        {
            ok=1;
            cout << gen(n,0);
            printf("\n");
            continue;
        }
        if (sol[1][n][0]==p && sol[1][n][1]==r && sol[1][n][2]==s)
        {
            ok=1;
            cout << gen(n,1);
            printf("\n");
            continue;
        }
        if (sol[2][n][0]==p && sol[2][n][1]==r && sol[2][n][2]==s)
        {
            ok=1;
            cout << gen(n,2);
            printf("\n");
            continue;
        }
        printf("IMPOSSIBLE\n");
    }
}
