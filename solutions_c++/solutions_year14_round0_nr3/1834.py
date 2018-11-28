#include <iostream>
#include <stdio.h>
using namespace std;

int mina[7][7];
int R,C,M;
int chisla[6][6];
int br;
int otgR,otgC;
bool nameren;
bool TFO[7][7];

void DFS(int red,int kolona)
{
    if (red<1 || red>R || kolona<1 || kolona>C)
    return;
    if (TFO[red][kolona])
    return;

    TFO[red][kolona]=true;

    if (mina[red][kolona]==1)
    return;

    br++;

    if (chisla[red][kolona]>0)
    return;

    DFS(red-1,kolona);
    DFS(red-1,kolona+1);
    DFS(red,kolona+1);
    DFS(red+1,kolona+1);
    DFS(red+1,kolona);
    DFS(red+1,kolona-1);
    DFS(red,kolona-1);
    DFS(red-1,kolona-1);

    return;
}

bool Good()
{
    int i,j;

    for (i=1;i<=R;i++)
    {
        for (j=1;j<=C;j++)
        {
            if (mina[i][j]==1)
            {
                chisla[i][j]=-1;
            }
            else
            {
                chisla[i][j]=mina[i-1][j]+mina[i-1][j+1]+mina[i][j+1]+mina[i+1][j+1]+mina[i+1][j]+mina[i+1][j-1]+mina[i][j-1]+mina[i-1][j-1];
            }
        }
    }

    for (i=1;i<=R;i++)
    {
        for (j=1;j<=C;j++)
        {
            TFO[i][j]=false;
        }
    }

    for (i=1;i<=R;i++)
    {
        for (j=1;j<=C;j++)
        {
            if (mina[i][j]==0)
            {
                br=0;
                DFS(i,j);

                if (br!=R*C-M) return false;
                else
                {
                    otgR=i;
                    otgC=j;
                    return true;
                }
            }
        }
    }
}

void Backtracking(int red,int kolona,int mini)
{
    if (mini==0)
    {
        if ( Good() )
        {
            nameren=true;
        }

        return;
    }

    if (red>R)
    return;

    if ( (R-red)*C + (C-kolona+1) < mini )
    return;

    if (kolona!=C)
    {
        Backtracking(red,kolona+1,mini);
        if (nameren)
        return;

        mina[red][kolona]=1;

        Backtracking(red,kolona+1,mini-1);
        if (nameren)
        return;

        mina[red][kolona]=0;
    }
    else
    {
        Backtracking(red+1,1,mini);
        if (nameren)
        return;

        mina[red][kolona]=1;

        Backtracking(red+1,1,mini-1);
        if (nameren)
        return;

        mina[red][kolona]=0;
    }

    return;
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);

    int i,j,k;
    int t;

    cin>>t;

    for (i=1;i<=t;i++)
    {
        cin>>R>>C>>M;

        for (j=0;j<=R+1;j++)
        {
            for (k=0;k<=C+1;k++)
            {
                mina[j][k]=0;
            }
        }

        nameren=false;

        Backtracking(1,1,M);

        cout<<"Case #"<<i<<":"<<endl;

        if (!nameren)
        {
            cout<<"Impossible"<<endl;
            continue;
        }

        for (j=1;j<=R;j++)
        {
            for (k=1;k<=C;k++)
            {
                if (mina[j][k]==1)
                cout<<"*";
                else if (j==otgR && k==otgC)
                cout<<"c";
                else
                cout<<".";
            }
            cout<<endl;
        }
    }

    return 0;
}
