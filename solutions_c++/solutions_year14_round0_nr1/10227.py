#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int main()
{
bool present[17];
int t,x,y,tmp,coun,cas=0,ans;
scanf("%d",&t);
while(t--)
{
cas++;
scanf("%d",&x);
coun=0;
memset(present,0,sizeof(present));
for(int i=1;i<=4;i++)
{
    for(int j=1;j<=4;j++)
    {
    scanf("%d",&tmp);
    if(i==x)
    present[tmp]=true;
    }
}
scanf("%d",&y);
for(int i=1;i<=4;i++)
{
    for(int j=1;j<=4;j++)
    {
    scanf("%d",&tmp);
    if(i==y)
    {
        if(present[tmp])
        {
        ans=tmp;
        coun++;
        }

    }
    }
}
if(coun==1)
printf("Case #%d: %d\n",cas,ans);
else if(coun>1)
printf("Case #%d: Bad magician!\n",cas);
else
printf("Case #%d: Volunteer cheated!\n",cas);

}

return 0;
}
