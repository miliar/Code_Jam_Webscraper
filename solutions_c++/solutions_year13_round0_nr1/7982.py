#include <iostream>

using namespace std;

const int N=4;

char mat[10][10];
int add[][2]={-1,0,-1,1,0,1,1,1};

int Win(char ch)
{
    int i,j,k;
    for(i=1;i<=N;i++)
    for(j=1;j<=N;j++)
    {
        if(mat[i][j]==ch)
        {
            int k;
            for(k=0;k<4;k++)
            {
                int cnt=0;
                int l;
                for(l=1;l<=3;l++)
                {
                    int addi=i+l*add[k][0];
                    int addj=j+l*add[k][1];
                    //printf("addi, addj: %d %d\n",addi,addj);
                    if(addi<=0||addj<=0||addi>4||addj>4) break;
                    if(mat[addi][addj]==ch||mat[addi][addj]=='T') cnt++;
                    else break;
                }
                if(cnt==3) return 1;
            }
        }
    }
    return -1;
}

int Uncomplete()
{
    int i,j;
    for(i=1;i<=N;i++)
    for(j=1;j<=N;j++)
    if(mat[i][j]=='.')
    return 1;
    return -1;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,cas=1;
    scanf("%d",&cases);
    while(cases--)
    {
        int i,j;
        //int tx=-1,ty=-1;
        for(i=1;i<=N;i++)
        for(j=1;j<=N;j++)
        {
            scanf(" %c",&mat[i][j]);
//            if(mat[i][j]=='T')
//            {
//                tx=i;
//                ty=j;
//            }
        }
        int win=-1;

        //if(tx!=-1) mat[tx][ty]='X';
        win=Win('X');
        if(win!=-1)
        {
            printf("Case #%d: X won\n",cas++);
            continue;
        }

        //if(tx!=-1) mat[tx][ty]='O';
        win=Win('O');
        if(win!=-1)
        {
            printf("Case #%d: O won\n",cas++);
            continue;
        }

        win=Uncomplete();
        if(win!=-1)
        {
            printf("Case #%d: Game has not completed\n",cas++);
            continue;
        }
        printf("Case #%d: Draw\n",cas++);
    }
    return 0;
}
