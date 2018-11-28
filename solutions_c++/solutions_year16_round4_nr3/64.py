#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int CURMASK;

int t;
int n,m;
int lovers[100111];

char grid[21][21];

void Decode(int mask)
{
    int i,j;
    int ctr=0;

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=m;j++)
        {
            if ( (mask&(1<<ctr))>0 )
            grid[i][j]='/';
            else
            grid[i][j]=92;

            ctr++;
        }
    }

    return;
}

vector<int> Graph[100111];
int id[21][21][2];
int num;

void Add(int a,int b)
{
    Graph[a].push_back(b);
    Graph[b].push_back(a);

    //cout<<"Edge "<<a<<"~"<<b<<endl;

    return;
}

void BuildGraph()
{
    int i,j;
    int ctr=0;

    for (i=1;i<=num;i++)
    {
        Graph[i].clear();
    }

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=m;j++)
        {
            if (j!=1)
            {
                if (grid[i][j]=='/')
                {
                    if (grid[i][j-1]=='/')
                    {
                        Add(id[i][j][0],id[i][j-1][1]);
                    }
                    else
                    {
                        Add(id[i][j][0],id[i][j-1][0]);
                    }
                }
                else
                {
                    if (grid[i][j-1]=='/')
                    {
                        Add(id[i][j][1],id[i][j-1][1]);
                    }
                    else
                    {
                        Add(id[i][j][1],id[i][j-1][0]);
                    }
                }
            }

            if (i!=1)
            {
                Add(id[i][j][0],id[i-1][j][1]);
            }
        }
    }

    ///Top
    for (i=1;i<=m;i++)
    {
        ctr++;

        Add(ctr,id[1][i][0]);
    }

    ///Right
    for (i=1;i<=n;i++)
    {
        ctr++;

        if (grid[i][m]=='/')
        Add(ctr,id[i][m][1]);
        else
        Add(ctr,id[i][m][0]);
    }

    ///Down
    for (i=m;i>=1;i--)
    {
        ctr++;

        Add(ctr,id[n][i][1]);
    }

    ///Left
    for (i=n;i>=1;i--)
    {
        ctr++;

        if (grid[i][1]=='/')
        Add(ctr,id[i][1][0]);
        else
        Add(ctr,id[i][1][1]);
    }

    return;
}

bool TFO[100111];
bool flag=false;

void DFS(int ver,int origin)
{
    if (TFO[ver])
    return;

    TFO[ver]=true;

    if (ver<=2*(n+m))
    {
        if (ver!=origin && ver!=lovers[origin])
        flag=true;
    }

    int i;

    for (i=0;i<Graph[ver].size();i++)
    {
        DFS(Graph[ver][i],origin);
    }

    return;
}

bool Check()
{
    int i,j;

    /*if (CURMASK==6)
    {
        cout<<"Testing:"<<endl;
        for (i=1;i<=n;i++)
        {
            for (j=1;j<=m;j++)
            {
                cout<<grid[i][j];
            }
            cout<<endl;
        }
        cout<<endl;
    }*/

    BuildGraph();

    for (i=1;i<=num;i++)
    {
        TFO[i]=false;
    }

    flag=false;

    for (i=1;i<=2*(n+m);i++)
    {
        if (!TFO[i])
        {
            DFS(i,i);

            if (flag || !TFO[ lovers[i] ])
            return false;
        }
    }

    //cout<<"True for "<<CURMASK<<endl;

    return true;
}

void Numerate()
{
    int i,j;

    num=2*(n+m);

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=m;j++)
        {
            num++;
            id[i][j][0]=num;

            num++;
            id[i][j][1]=num;
        }
    }

    return;
}

int main()
{
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);

    int test;
    int i,j;
    int a,b;
    int mask;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        fprintf(stderr,"Test %d\n",test);
        scanf("%d %d",&n,&m);

        Numerate();

        for (i=1;i<=(n+m);i++)
        {
            scanf("%d %d",&a,&b);

            lovers[a]=b;
            lovers[b]=a;
        }

        for (mask=0;mask<(1<<(n*m));mask++)
        {
            CURMASK=mask;

            Decode(mask);

            if (Check())
            break;
        }

        printf("Case #%d:\n",test);

        if (mask==(1<<(n*m)))
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            for (i=1;i<=n;i++)
            {
                for (j=1;j<=m;j++)
                {
                    printf("%c",grid[i][j]);
                }
                printf("\n");
            }
        }
    }

    return 0;
}
