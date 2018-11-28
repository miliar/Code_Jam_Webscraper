#include <stdio.h>
#include <algorithm>

using namespace std;

struct node
{
    int row;
    int col;
    int val;
}que[10000];

int grass[100][100];

bool cmp(const node &a,const node &b)
{
    return a.val < b.val;
}

bool CheckRow(int row,int col,int mCol)
{
    for(int j=0;j<mCol;j++)
    {
        if(grass[row][j] == -1)continue;
        else if(grass[row][j] > grass[row][col])return false;
    }
    for(int j=0;j<mCol;j++)grass[row][j] = -1;
    return true;
}

bool CheckCol(int row,int col,int nRow)
{
    for(int i=0;i<nRow;i++)
    {
        if(grass[i][col] == -1)continue;
        else if(grass[i][col] > grass[row][col])return false;
    }
    for(int i=0;i<nRow;i++)grass[i][col] = -1;
    return true;
}

bool Check(int capcity,int nRow,int mCol)
{
    for(int i=0;i<capcity;i++)
    {
        int row = que[i].row;
        int col = que[i].col;

        if(grass[row][col] == -1)continue;

        if(CheckRow(row,col,mCol))continue;

        if(CheckCol(row,col,nRow))continue;
        else return false;
    }
    return true;
}

int main()
{
    freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

    int tCase;

    scanf("%d",&tCase);
    for(int tNum = 1;tNum<=tCase;tNum++)
    {
        int nRow,mCol;
        scanf("%d%d",&nRow,&mCol);
        for(int i=0;i<nRow;i++)
        {
            for(int j=0;j<mCol;j++){
                scanf("%d",grass[i]+j);
                que[i*mCol+j].row = i;
                que[i*mCol+j].col = j;
                que[i*mCol+j].val = grass[i][j];
            }
        }
        sort(que,que+nRow*mCol,cmp);

        if(Check(nRow*mCol,nRow,mCol))printf("Case #%d: YES\n",tNum);
        else printf("Case #%d: NO\n",tNum);
    }
    return 0;
}
