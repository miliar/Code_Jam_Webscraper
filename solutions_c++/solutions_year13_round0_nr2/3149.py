#include <stdio.h>
#include <set>

#define size 2

using namespace std;

set<int>s;
set<int>::iterator it;

int row,col;
int board[120][120],num[120],eRow[120],eCol[120];//edit Row


void reset()
{
    int i,j;
    for(i=0;i<size;i++)
        num[i]=0;
}

void print()
{
    int i,j;
     printf("\n");
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
            printf("%d ",board[i][j]);
        printf("\n");
    }
     printf("\n");
}

int main()
{
    int i,j,bad=0;
    int ptER,ptEC,file,nFile,min,min2;
    scanf("%d",&nFile);
    for(file=1;file<=nFile;file++)
    {
        scanf("%d %d",&row,&col);
        for(i=0;i<row;i++)
        {
            for(j=0;j<col;j++)
            {
                scanf("%d",&board[i][j]);
                if(s.find(board[i][j])==s.end())
                    s.insert(board[i][j]);
            }
        }
        while(true)
        {
            if(s.empty()==1)
                break;
            it=s.begin();   min=*it;
            ptER=-1;
            //row
            for(i=0;i<row;i++)
            {
                bad=0; //bad row mean have size in that row;
                for(j=0;j<col;j++)
                {
                    if(board[i][j]!=min)
                    {
                        bad=1;
                        break;
                    }
                    //num[board[i][j]]++;
                }
                if(bad==0)
                {
                    eRow[++ptER]=i;
                }
            }

            ptEC=-1;//
            //row
            for(j=0;j<col;j++)
            {
                bad=0; //bad row mean have size in that row;
                for(i=0;i<row;i++)
                {
                    if(board[i][j]!=min)
                    {
                        bad=1;
                        break;
                    }
                    //num[board[i][j]]++;
                }
                if(bad==0)
                {
                    eCol[++ptEC]=j;
                }
            }

            s.erase(min);
            if(s.empty()==1)
                break;
            it=s.begin();   min2=*it;
            //edit
            for(i=0;i<=ptER;i++)
            {
                for(j=0;j<col;j++)
                {
                    board[eRow[i]][j]=min2;
                }
            }
            for(j=0;j<=ptEC;j++)
            {
                for(i=0;i<row;i++)
                {
                    board[i][eCol[j]]=min2;
                }
            }
        }

        bad=0;
        min=board[0][0];
        for(i=0;i<row;i++)
        {
            for(j=0;j<col;j++)
            {
                if(board[i][j]!=min)
                {
                    bad=1;
                    break;
                }
            }
            if(bad==1)
                break;
        }

        if(bad==1)
            printf("Case #%d: NO\n",file);
        else
            printf("Case #%d: YES\n",file);

    }

    scanf(" ");
    return 0;
}
