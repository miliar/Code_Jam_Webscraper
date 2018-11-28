#include<iostream>
#include<cstdio>
#include<fstream>

using namespace std;
int t,x,y;
int main()
{

freopen("C-small.in","r",stdin);
freopen("C-small.out","w",stdout);
    int a=1,b=4,c=9,d=121,e=484;
       scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d%d",&x,&y);
        int count=0;
        printf("Case #%d: ",i+1);

        if(a>=x&&a<=y)
        count++;
        if(b>=x&&b<=y)
        count++;
        if(c>=x&&c<=y)
        count++;
        if(d>=x&&d<=y)
        count++;
        if(e>=x&&e<=y)
        count++;

        printf("%d\n",count);
    }

}
