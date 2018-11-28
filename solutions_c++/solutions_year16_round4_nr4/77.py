#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int t;
int n;
bool grid[27][27];

bool checkgrid[27][27];
char inp[27];

void Decode(int mask)
{
    int ctr=0;
    int i,j;

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            if ( (mask&(1<<ctr))>0 )
            checkgrid[i][j]=true;
            else
            checkgrid[i][j]=false;

            ctr++;
        }
    }

    return;
}

int order[27];
bool taken[27];
bool flag=false;

void Simulate(int ind)
{
    if (ind>n)
    return;

    int worker=order[ind];
    int i;
    bool canwork=false;

    //cout<<"Worker "<<worker<<endl;

    for (i=1;i<=n;i++)
    {
        if (checkgrid[worker][i] && !taken[i])
        {
            canwork=true;

            taken[i]=true;

            //cout<<"taking "<<i<<endl;

            Simulate(ind+1);

            taken[i]=false;

            //cout<<"Back to "<<worker<<endl;

            if (flag)
            return;
        }
    }

    if (!canwork)
    {
        //cout<<"turns out "<<worker<<" couldnt work"<<endl;
        flag=true;
    }

    return;
}

bool Check()
{
    int i,j;

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            if (!checkgrid[i][j] && grid[i][j])
            return false;
        }
    }

    /*for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            cout<<checkgrid[i][j];
        }
        cout<<endl;
    }
    cout<<endl;*/

    for (i=1;i<=n;i++)
    {
        order[i]=i;
    }

    flag=false;
    do
    {
        Simulate(1);

        if (flag)
        {
            //cout<<"F-ed up"<<endl;

            return false;
        }
    }while( next_permutation(order+1,order+1+n) );

    return true;
}

int mypopctr(int mask)
{
    int ctr=0;

    while(mask>0)
    {
        if (mask%2==1)
        ctr++;

        mask/=2;
    }

    return ctr;
}

int main()
{
    freopen("D-small.in","r",stdin);
    freopen("D-small.out","w",stdout);

    int i,j;
    int test;
    int mask;
    int val,bestval;
    int baseknow;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%d",&n);
        bestval=n*n;

        baseknow=0;
        for (i=1;i<=n;i++)
        {
            scanf("%s",inp+1);

            for (j=1;j<=n;j++)
            {
                if (inp[j]=='1')
                {
                    grid[i][j]=true;
                    baseknow++;
                }
                else
                grid[i][j]=false;
            }
        }

        for (mask=0;mask<(1<<(n*n));mask++)
        {
            Decode(mask);

            if (Check())
            {
                val=mypopctr(mask)-baseknow;

                if (val<bestval)
                bestval=val;
            }
        }

        printf("Case #%d: %d\n",test,bestval);
    }

    return 0;
}
