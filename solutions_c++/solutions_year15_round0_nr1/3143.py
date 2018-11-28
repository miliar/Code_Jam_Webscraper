#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
FILE *fin,*fout;
int T,n;
char st[10000];
int main()
{
    fin=freopen("test.txt","r",stdin);
    fout=freopen("testout.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d",&n);
        scanf("%s",st);
        int sum=0;
        int ans=0;
        for(int i=0;i<=n;i++)
        {
            if(i>sum)
            {
                ans+=i-sum;
                sum=i;
            }
            sum+=st[i]-'0';
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
