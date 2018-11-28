#include <iostream>
#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;
typedef long long Int;

int t;
int n,d;

int S,As,Cs,Rs;
int M,Am,Cm,Rm;

int salary[1000111];
int manager[1000111];

vector<int> Graph[1000111];

int MIN(int a,int b)
{
    if (a<b)
    return a;
    else
    return b;
}

int MAX(int a,int b)
{
    if (a>b)
    return a;
    else
    return b;
}

int TFO[1000111];
int Key=1;
int counter=0;
int bestcounter=0;

void Try(int ver,int limit)
{
    int i;

    TFO[ver]=Key;

    counter++;

    for (i=0;i<Graph[ver].size();i++)
    {
        if (TFO[ Graph[ver][i] ]==Key)
        continue;
        if (salary[ Graph[ver][i] ]<limit || salary[ Graph[ver][i] ]>limit+d)
        continue;

        Try(Graph[ver][i],limit);
    }

    if (ver!=1)
    if (TFO[ manager[ver] ]!=Key)
    {
        if (salary[ manager[ver] ]>=limit && salary[ manager[ver] ]<=limit+d)
        Try(manager[ver],limit);
    }

    return;
}

void DFS(int ver,int minsalary,int maxsalary)
{
    if (salary[ver]<minsalary && salary[ver]+d>=maxsalary) ///could be
    {
        Key++;
        counter=0;
        Try(ver,salary[ver]);

        if (counter>bestcounter)
        bestcounter=counter;
    }

    int i;

    for (i=0;i<Graph[ver].size();i++)
    {
        DFS(Graph[ver][i],MIN(minsalary,salary[ver]),MAX(maxsalary,salary[ver]));
    }

    return;
}

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-output.txt","w",stdout);

    int test;
    int i;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        bestcounter=0;

        scanf("%d %d",&n,&d);

        for (i=0;i<=n+2;i++)
        {
            Graph[i].clear();
        }

        scanf("%d %d %d %d",&S,&As,&Cs,&Rs);
        scanf("%d %d %d %d",&M,&Am,&Cm,&Rm);

        salary[1]=S;
        for (i=2;i<=n;i++)
        {
            salary[i]=(int)( ( (Int)salary[i-1]*(Int)As + (Int)Cs ) % (Int)Rs );
        }

        manager[1]=M;
        for (i=2;i<=n;i++)
        {
            manager[i]=(int)( ( (Int)manager[i-1]*(Int)Am + (Int)Cm ) % (Int)Rm );
        }

        for (i=2;i<=n;i++)
        {
            manager[i]=manager[i]%(i-1)+1;
        }

        for (i=2;i<=n;i++)
        {
            Graph[ manager[i] ].push_back(i);
        }

        memset(TFO,0,sizeof(TFO));
        Key=1;

        DFS(1,999999999,-1);

        printf("Case #%d: %d\n",test,bestcounter);
    }

    return 0;
}
