#include <iostream>

using namespace std;

bool Parid(int x)
{
    int t=x;
    int line[10],cntl=0;
    while(t)
    {
        line[cntl++]=t%10;
        t/=10;
    }
    for(int i=0;i<=cntl/2-1;i++)
    if(line[i]!=line[cntl-1-i]) return false;
    return true;
}
int main()
{
     freopen("in.txt","r",stdin);
     freopen("out.txt","w",stdout);
    int cases,cas=1;
    scanf("%d",&cases);
    while(cases--)
    {
        int left,right;
        scanf("%d %d",&left,&right);
        int i,j;
        int cnt=0;
        for(i=1;i*i<=right;i++)
        {
            if(i*i<left) continue;
            if(Parid(i)&&Parid(i*i)) cnt++;
        }
        printf("Case #%d: %d\n",cas++,cnt);
    }
    return 0;
}
