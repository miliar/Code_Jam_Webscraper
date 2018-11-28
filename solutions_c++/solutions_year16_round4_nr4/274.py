#include<set>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<string>
#include<time.h>
#include<math.h>
#include<memory>
#include<vector>
#include<bitset>
#include<fstream>
#include<stdio.h>
#include<utility>
#include<sstream>
#include<string.h>
#include<iostream>
#include<stdlib.h>
#include<algorithm>
using namespace std;
char a[35][35];
int n;
int b[15];
bool used[15];
bool unok(int x)
{
    if (x==n) return false;
    int i;
    int sum=0;
    for (i=0;i<n;i++)
    {
        if (used[i]) continue;
        if (a[b[x]][i]=='1')
        {
            sum=1;
            used[i]=true;
            if (unok(x+1)) return true;
            used[i]=false;
        }
    }
    if (sum==0) return true;
    return false;
}
bool check()
{
    int i;
    for (i=0;i<n;i++)
    {
        b[i]=i;
        used[i]=false;
    }
    for (;;)
    {
        if (unok(0)) return false;
        if (!next_permutation(b,b+n)) return true;
    }
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    int zu;
    for (zu=0;zu<t;zu++)
    {
        printf("Case #%d: ",zu+1);
        int i;
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%s",a[i]);
        }
        int max_ans=10000;
        for (i=0;i<(1<<(n*n));i++)
        {
            int j;
            int sum=0;
            for (j=0;j<(n*n);j++)
            {
                int t1=j/n;
                int t2=j%n;
                if ((1<<j)&i) continue;
                if (a[t1][t2]=='1') break;
                sum++;
            }
            if (j!=n*n) continue;
            if (sum>=max_ans) continue;
            for (j=0;j<(n*n);j++)
            {
                int t1=j/n;
                int t2=j%n;
                if ((1<<j)&i) continue;
                a[t1][t2]='1';
            }
            if (check()) max_ans=sum;
            for (j=0;j<(n*n);j++)
            {
                int t1=j/n;
                int t2=j%n;
                if ((1<<j)&i) continue;
                a[t1][t2]='0';
            }
        }
        printf("%d\n",max_ans);
    }
    return 0;
}
