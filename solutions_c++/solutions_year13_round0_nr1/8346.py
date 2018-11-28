#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
using namespace std;



char maze[7][7];
int main()
{
    int t,ti=1;
    scanf("%d",&t);
    while(t--)
    {
        int x=-1,y=-1;
        bool con=0;
        for(int i=0;i<4;i++)
        {
            scanf("%s",maze[i]);
            for(int j=0;maze[i][j];j++)
            {
                if(maze[i][j]=='.') con=1;
                if(maze[i][j]=='T') x=i,y=j;
            }
        }
        int win=0;
        for(int i=0;i<4;i++)
        {
            if(x!=-1 && y!=-1) maze[x][y]='O';
            if(maze[i][0]=='O' && maze[i][1]=='O' && maze[i][2]=='O' &&maze[i][3]=='O') win=1;
            if(maze[0][i]=='O' && maze[1][i]=='O' && maze[2][i]=='O' &&maze[3][i]=='O') win=1;
            if(x!=-1 && y!=-1) maze[x][y]='X';
            if(maze[i][0]=='X' && maze[i][1]=='X' && maze[i][2]=='X' &&maze[i][3]=='X') win=-1;
            if(maze[0][i]=='X' && maze[1][i]=='X' && maze[2][i]=='X' &&maze[3][i]=='X') win=-1;
        }
        if(x!=-1 && y!=-1) maze[x][y]='X';
        if(maze[0][0]=='X' && maze[1][1]=='X' && maze[2][2]=='X' &&maze[3][3]=='X') win=-1;
        if(maze[3][0]=='X' && maze[2][1]=='X' && maze[1][2]=='X' &&maze[0][3]=='X') win=-1;
        if(x!=-1 && y!=-1) maze[x][y]='O';
        if(maze[0][0]=='O' && maze[1][1]=='O' && maze[2][2]=='O' &&maze[3][3]=='O') win=1;
        if(maze[3][0]=='O' && maze[2][1]=='O' && maze[1][2]=='O' &&maze[0][3]=='O') win=1;
        printf("Case #%d: ",ti++);
        if(win==0)
        {
            if(con) printf("Game has not completed\n");
            else printf("Draw\n");
        }
        else
        {
            if(win==1) printf("O won\n");
            else printf("X won\n");
        }
    }
    return 0;
}

































