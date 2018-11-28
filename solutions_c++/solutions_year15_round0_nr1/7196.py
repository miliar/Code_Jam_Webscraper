#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int s,sum=0,maxx=0;
        scanf("%d",&s);
        char a[1010]={};
        scanf("%s",a);
        for(int j=0;j<=s;j++)
        {
            maxx=max(maxx,j-sum);
            sum+=a[j]-'0';
        }
        printf("Case #%d: %d\n",i,maxx);
    }
}
