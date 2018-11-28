#include<iostream>
#include<vector>
#include<stdio.h>
#include<cstring>
using namespace std;
int main()
{
bool b[17];
int t,x,y,tmp,coun,tes=0,ans;
scanf("%d",&t);
while(t--)
{
tes++;
scanf("%d",&x);
coun=0;
memset(b,0,sizeof(b));
for(int i=1;i<=4;i++)
{
    for(int j=1;j<=4;j++)
    {
    scanf("%d",&tmp);
    if(i==x)
    b[tmp]=true;
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
        if(b[tmp])
        {
        ans=tmp;
        coun++;
        }

    }
    }
}
if(coun==1)
printf("Case #%d: %d\n",tes,ans);
else if(coun>1)
printf("Case #%d: Bad magician!\n",tes);
else
printf("Case #%d: Volunteer cheated!\n",tes);

}

return 0;
}
