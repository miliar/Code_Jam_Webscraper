#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
#include<assert.h>

using namespace std;

char str[101][101];

bool checkstr(int in,int n)
{
    int i=0,k=0;
    if(in==0)
        return 1;
    while(1)
    {
        if(str[in][i]=='\0'&&str[0][k]=='\0')
        {
            return 1;
        }
        else if(str[in][i]=='\0'||str[0][k]=='\0')
        {
            return 0;
        }
        while(str[0][k]==str[0][k+1])
            k++;
        while(str[in][i]==str[in][i+1])
            i++;
        if(str[in][i]!=str[0][k])
        {
            return 0;
        }
        i++;
        k++;
    }
}

bool check(int n)
{
    for(int i=0;i<n;i++)
    {
        if(checkstr(i,n)==0)
        {
            return 0;
        }
    }
    return 1;
}

int cost(int i1,int i2,int n)
{
    if(i1==i2)
        return 0;
    int itr1=0,itr2=0;
    int ret=0;
    while(1)
    {
        if(str[i1][itr1]=='\0')
            return ret;
        while(str[i1][itr1]==str[i1][itr1+1]&&str[i2][itr2]==str[i2][itr2+1])
        {
            itr1++;
            itr2++;
        }
        while(str[i1][itr1]==str[i1][itr1+1])
        {
            itr1++;
            ret++;
        }
        while(str[i2][itr2]==str[i2][itr2+1])
        {
            itr2++;
            ret++;
        }
        itr1++;
        itr2++;
    }
}

int main()
{
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%s",str[i]);
        bool valid=check(n);
        if(valid==0)
        {
            printf("Case #%d: Fegla Won\n",t);
            continue;
        }
        int mincost=1000;
        for(int i=0;i<n;i++)
        {
            int sum=0;
            for(int j=0;j<n;j++)
            {
                sum+=cost(j,i,n);
            }
            if(sum<mincost)
                mincost=sum;
        }
        printf("Case #%d: %d\n",t,mincost);
    }

    return 0;
}
