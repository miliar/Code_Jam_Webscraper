#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <string.h>
using namespace std;

int t;
int n,m;
char inps[10][21];
int L[10];
vector<int> groups[5];
int amount[1001];

string curstr;
set<string> myset;

int GetPrefixes(int grp)
{
    int i,j;

    myset.clear();

    for (i=0;i<groups[grp].size();i++)
    {
        curstr.clear();

        for (j=1;j<=L[ groups[grp][i] ];j++)
        {
            curstr.push_back( inps[ groups[grp][i] ][j] );

            myset.insert(curstr);
        }
    }

    return myset.size();
}

void Backtrack(int cur)
{
    int i;

    if (cur==m+1)
    {
        for (i=1;i<=n;i++)
        {
            if (groups[i].empty())
            return;
        }

        int ctr=0;

        for (i=1;i<=n;i++)
        {
            ctr+=GetPrefixes(i);
        }

        ctr+=n;

        amount[ctr]++;

        return;
    }

    for (i=1;i<=n;i++)
    {
        groups[i].push_back(cur);

        Backtrack(cur+1);

        groups[i].pop_back();
    }

    return;
}


int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-ans.txt","w",stdout);

    int test;
    int i;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        fprintf(stderr,"%d Done\n",test);

        memset(amount,0,sizeof(amount));

        scanf("%d %d",&m,&n);

        for (i=1;i<=m;i++)
        {
            scanf("%s",inps[i]+1);
            L[i]=strlen(inps[i]+1);
        }

        for (i=1;i<=n;i++)
        {
            groups[i].clear();
        }

        Backtrack(1);

        for (i=1000;i>=1;i--)
        {
            if (amount[i]>0)
            {
                printf("Case #%d: %d %d\n",test,i,amount[i]);
                break;
            }
        }
    }

    return 0;
}
