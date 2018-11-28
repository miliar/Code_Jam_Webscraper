#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <utility>

using namespace std;

bool iks(const int tab[4][4])
{
    for(int i=0;i<4;i++)
    {
        int red=0;
        for(int j=0;j<4;j++)
        {
            if(tab[i][j]>-1) red++;
        }
        if(red==4) return true;
    }

    for(int i=0;i<4;i++)
    {
        int red=0;
        for(int j=0;j<4;j++)
        {
            if(tab[j][i]>-1) red++;
        }
        if(red==4) return true;
    }
    int red=0;

    for(int i=0;i<4;i++) if(tab[i][i]>-1) red++;
    if(red==4) return true;
    red=0;
    int j=0;
    for(int i=3;i>-1;i--) {if(tab[i][j]>-1) red++;j++;}
    if(red==4) return true;
    return false;
}

int tar[4][4];

bool oks(const int tab[4][4])
{

    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(tab[i][j]==0) tar[i][j]=0;
            if(tab[i][j]==-2) tar[i][j]=-2;
            if((tab[i][j]<0)&&(tab[i][j]!=-2)) tar[i][j]=1;
            if(tab[i][j]==1) tar[i][j]=-1;
            //printf("%d ",tar[i][j]);
        }
        //printf("\n");
    }


    for(int i=0;i<4;i++)
    {
        int red=0;
        for(int j=0;j<4;j++)
        {
            if(tar[i][j]>-1) red++;
        }
        if(red==4) return true;
    }

    for(int i=0;i<4;i++)
    {
        int red=0;
        for(int j=0;j<4;j++)
        {
            if(tar[j][i]>-1) red++;
        }
        if(red==4) return true;
    }
    int red=0;

    for(int i=0;i<4;i++) if(tar[i][i]>-1) red++;
    if(red==4) return true;
    red=0;
    int j=0;
    for(int i=3;i>-1;i--) {if(tar[i][j]>-1) red++;j++;}
    if(red==4) return true;
    return false;
}

    int tab[4][4];

int main()
{
    //freopen("NOVObig.txt","w",stdout);
    int n;
    scanf("%d",&n);
    scanf("\n");
    char t;
    string tmp;

    for(int k=1;k<n+1;k++)
    {
        bool ima=false;
        for(int x=0;x<4;x++)
        {
            cin>>tmp;
            for(int y=0;y<4;y++)
            {
                t=tmp[y];
                if(t=='.') {tab[x][y]=-2;ima=true;}
                if(t=='X') tab[x][y]=1;
                if(t=='T') tab[x][y]=0;
                if(t=='O') tab[x][y]=-1;
            }
            //getchar();
            //scanf("\n");
        }
        getchar();
        bool ix=iks(tab);
        bool ox=oks(tab);
        if(ix) printf("Case #%d: X won\n",k);
        if(ox) printf("Case #%d: O won\n",k);
        if((!ox)&&(!ix))
        {
            if(ima)
            {
                printf("Case #%d: Game has not completed\n",k);
            }else
            {
                printf("Case #%d: Draw\n",k);
            }
        }

    }
    return 0;
}
